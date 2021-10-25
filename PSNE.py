import time
import argparse
import numpy as np
import games
import util


def scalarise_matrix(payoff_matrix, u, player_actions):
    """
    This function will scalarise a matrix according to a given utility function.
    :param payoff_matrix: The input payoffs.
    :param u: A utility function.
    :param player_actions: A tuple with the number of actions for each player.
    :return: The scalarised game.
    """
    scalarised_matrix = np.zeros(player_actions)
    num_strategies = np.prod(player_actions)

    for i in range(num_strategies):  # Loop over all possible strategies.
        idx = np.unravel_index(i, player_actions)  # Get the strategy from the flat index.
        utility = u(payoff_matrix[idx])
        scalarised_matrix[idx] = utility

    return scalarised_matrix


def reduce_monfg(monfg, player_actions, u_tpl):
    """
    This function will reduce the MONFG to an NFG as a list of payoff matrices.
    :param monfg: The input MONFG.
    :param player_actions: A tuple of the amount of actions per player.
    :param u_tpl: A tuple of utility functions.
    :return: An NFG.
    """
    nfg = []  # Collect the payoff matrices.
    for player, u in enumerate(u_tpl):
        scalarised_payoff = scalarise_matrix(monfg[player], u, player_actions)  # Scalarise the MONFG.
        nfg.append(scalarised_payoff)
    return nfg


def calc_nfg_psne(nfg, player_actions):
    """
    This function will calculate the PSNE from the scalarised game.
    :param nfg: The scalarised MONFG.
    :param player_actions: A tuple of the amount of actions per player.
    :return: A list of PSNE.
    """
    best_responses = []  # Collect the best response matrices.
    num_strategies = np.prod(player_actions)  # The number of possible pure strategies.

    for player, payoffs in enumerate(nfg):
        best_response_matrix = np.zeros(player_actions, dtype=bool)  # Initialise a new boolean best response matrix.
        maxima = np.amax(nfg[player], axis=player)  # The payoffs of the best responses to all other players strategies.
        for i in range(num_strategies):  # Loop over all joint strategies.
            idx = np.unravel_index(i, player_actions)  # Get the correctly shaped index of this strategy.
            opp_strat = list(idx)  # Turn the index into a list for the next operation.
            del opp_strat[player]  # Find the opponent strategy that corresponds with this joint strategy.
            opp_strat = tuple(opp_strat)  # Turn it back into a tuple.
            max = maxima[opp_strat]  # Get the payoff of the best response to this opponent strategy.
            if payoffs[idx] >= max:  # If the payoff of this joint strategy is equal or greater.
                best_response_matrix[idx] = True  # It is a best response to the opponent strategies.

        best_responses.append(best_response_matrix)

    nash_equilibria = np.ones(player_actions, dtype=bool)  # Initialise a new matrix holding the PSNE.
    for i in range(len(best_responses)):
        nash_equilibria = np.logical_and(nash_equilibria,
                                         best_responses[i])  # Best response to all best responses is a NE.

    psne = np.argwhere(nash_equilibria)  # Get the action profiles that result in these PSNE.
    return psne


def find_all_psne(monfg, player_actions, u_tpl):
    """
    This function will find all Pure Strategy Nash Equilibria (PSNE).
    :param monfg: An input MONFG.
    :param player_actions: A tuple of the amount of actions per player.
    :param u_tpl: A tuple of utility functions.
    :return: A list of PSNE.
    """
    nfg = reduce_monfg(monfg, player_actions, u_tpl)  # Reduce the MONFG to an NFG.
    psne_lst = calc_nfg_psne(nfg, player_actions)  # Calculate the PSNE from these payoff matrices.
    return psne_lst


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--game', type=str, default='game1',
                        choices=['game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9',
                                 'random'],
                        help="which MONFG to play")
    parser.add_argument('-u', type=str, default=['u1', 'u2'], choices=['u1', 'u2', 'u3', 'u4'], nargs='+',
                        help="Which utility functions to use per player.")
    parser.add_argument('--player_actions', type=int, nargs='+', default=[3, 3],
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

    psne_lst = find_all_psne(monfg, player_actions, u_tpl)
    util.print_psne(psne_lst)

    end = time.time()
    elapsed_secs = (end - start)
    print("Seconds elapsed: " + str(elapsed_secs))
