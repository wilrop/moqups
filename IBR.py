import argparse
import time
import games
import util
import numpy as np
from best_response import best_response


def iterated_best_response(u_tpl, player_actions, monfg, max_iter=5000, joint_strategy=None):
    """
    This function executes the iterated best response algorithm on a given MONFG with accompanied utility functions.
    Note that at this point in time, this algorithm does not find cycles in the IBR dynamic.
    :param u_tpl: A tuple of utility functions.
    :param player_actions: A tuple of actions per player.
    :param monfg: A list of payoff matrices representing the MONFG.
    :param max_iter: The maximum amount of iterations to run IBR for.
    :param joint_strategy: Initial guess for the joint strategy.
    :return: Whether or not we reached a Nash equilibrium and the final joint strategy.
    """
    num_players = len(player_actions)
    if joint_strategy is None:
        joint_strategy = [np.full(num_actions, 1/num_actions) for num_actions in player_actions]
    nash_equilibrium = False  # The current joint strategy is not known to be a Nash equilibrium at this point.

    for iter in range(max_iter):
        print(f'Performing iteration {iter}')
        new_joint_strategy = []
        converged = True
        for player in range(num_players):
            u = u_tpl[player]
            payoff_matrix = monfg[player]
            br = best_response(u, player, payoff_matrix, joint_strategy)
            new_joint_strategy.append(br)
            if br.all() != joint_strategy[player].all():
                converged = False

        if converged:  # If everything already is a best-response to the joint strategy, we reached a NE.
            nash_equilibrium = True
            break
        else:
            joint_strategy = new_joint_strategy

    return nash_equilibrium, joint_strategy


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--game', type=str, default='game4',
                        choices=['game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9',
                                 'random'],
                        help="which MONFG to play")
    parser.add_argument('-u', type=str, default=['u1', 'u2'], choices=['u1', 'u2', 'u3', 'u4'], nargs='+',
                        help="Which utility functions to use per player.")
    parser.add_argument('--player_actions', type=int, nargs='+', default=[5, 5],
                        help='The number of actions per agent')
    parser.add_argument('--num_objectives', type=int, default=2, help="The number of objectives for the random MONFG")
    parser.add_argument('--lower_bound', type=int, default=0, help='The lower reward bound.')
    parser.add_argument('--upper_bound', type=int, default=5, help='The upper reward bound.')

    args = parser.parse_args()

    start = time.time()  # Start measuring the time.

    if args.game == 'random':
        player_actions = tuple(args.player_actions)
        monfg = games.generate_random_monfg(player_actions, args.num_objectives, args.lower_bound, args.upper_bound)
    else:
        monfg = games.get_monfg(args.game)

    player_actions = monfg[0].shape[:-1]  # Get the number of actions available to each player.
    u_tpl = tuple([games.get_u(u_str) for u_str in args.u])  # These must be quasiconvex to ensure correctness.

    # guess = [np.array([0, 1]), np.array([0, 1])]
    ne, joint_strategy = iterated_best_response(u_tpl, player_actions, monfg)
    if ne:
        util.print_ne(joint_strategy)
    else:
        print(f'No Nash equilibrium was found.')

    end = time.time()
    elapsed_secs = (end - start)
    print("Seconds elapsed: " + str(elapsed_secs))
