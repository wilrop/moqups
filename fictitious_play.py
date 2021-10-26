import argparse
import time
import games
import util
import numpy as np

from Player import FPPlayer


def fictitious_play(u_tpl, player_actions, monfg, max_iter=1000, init_joint_strategy=None, variant='simultaneous'):
    """
    This function executes the fictitious play algorithm on a given MONFG with accompanied utility functions.
    Note that the simultaneous and alternating variants are not equivalent in general. In the simultaneous variant, all
    players calculate their best-response strategy simultaneously. The alternating variant does it by alternating.
    Note that at this point in time, this algorithm does not find cycles.
    :param u_tpl: A tuple of utility functions.
    :param player_actions: A tuple of actions per player.
    :param monfg: A list of payoff matrices representing the MONFG.
    :param max_iter: The maximum amount of iterations to run IBR for.
    :param init_joint_strategy: Initial guess for the joint strategy.
    :param variant: The variant to use. This is either simultaneous or alternating.
    :return: Whether or not we reached a Nash equilibrium and the final joint strategy.
    """
    def simultaneous_variant():
        """
        This function will execute one iteration of the simultaneous fictitious play variant.
        :return: Whether the policies have converged and the new joint strategy.
        """
        converged = True
        actions = []

        for player in players:  # Collect actions.
            actions.append(player.select_action())

        for player in players:  # Update the empirical state distributions.
            player.update_joint_states(actions)

        for id, player in enumerate(players):  # Update the policies simultaneously.
            done, br = player.update_strategy()
            joint_strategy[id] = br  # Update the joint strategy.
            if not done:
                converged = False

        return converged, joint_strategy

    def alternating_variant():
        """
        This function will execute one iteration of the alternating fictitious play variant.
        :return: Whether the policies have converged and the new joint strategy.
        """
        converged = True

        for id, player in enumerate(players):  # Loop once over each player to update with alternating.
            actions = []

            for player in players:  # Collect actions.
                actions.append(player.select_action())

            for player in players:  # Update the empirical state distributions.
                player.update_joint_states(actions)

            done, br = player.update_strategy()  # Update the current player's policy.
            joint_strategy[id] = br  # Update the joint strategy.
            if not done:
                converged = False

        return converged, joint_strategy

    util.print_start('Fictitious Play')

    players = []  # A list to hold all the players.
    joint_strategy = []  # A list to hold the current joint strategy.

    for player, u in enumerate(u_tpl):  # Loop over all players to create a new FPAgent object.
        payoff_matrix = monfg[player]
        init_strategy = None
        if init_joint_strategy is not None:
            init_strategy = init_joint_strategy[player]
        player = FPPlayer(player, u, player_actions, payoff_matrix, init_strategy)
        players.append(player)
        joint_strategy.append(player.strategy)

    nash_equilibrium = False  # The current joint strategy is not known to be a Nash equilibrium at this point.

    if variant == 'simultaneous':
        execute_iteration = simultaneous_variant
    else:
        execute_iteration = alternating_variant

    for i in range(max_iter):
        print(f'Performing iteration {i}')
        converged, joint_strategy = execute_iteration()

        if converged:  # If everything already is a best-response to the joint strategy, we reached a NE.
            nash_equilibrium = True
            break

    return nash_equilibrium, joint_strategy


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--game', type=str, default='game1',
                        choices=['game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9',
                                 'random'],
                        help="which MONFG to play")
    parser.add_argument('--variant', type=str, default='simultaneous', choices=['simultaneous', 'alternating'])
    parser.add_argument('--iterations', type=int, default=1000, help="The maximum number of iterations.")
    parser.add_argument('-u', type=str, default=['u1', 'u2'], choices=['u1', 'u2', 'u3', 'u4'], nargs='+',
                        help="Which utility functions to use per player.")
    parser.add_argument('--player_actions', type=int, nargs='+', default=[5, 5],
                        help='The number of actions per player')
    parser.add_argument('--num_objectives', type=int, default=2, help="The number of objectives for the random MONFG.")
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
    u_tpl = tuple([games.get_u(u_str) for u_str in args.u])
    variant = args.variant
    iterations = args.iterations

    # guess = [np.array([0, 1]), np.array([0, 1])]
    ne, final_strategy = fictitious_play(u_tpl, player_actions, monfg, max_iter=iterations, variant=variant)
    util.print_ne(ne, final_strategy)

    end = time.time()
    elapsed_secs = (end - start)
    print("Seconds elapsed: " + str(elapsed_secs))
