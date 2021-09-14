import numpy as np
import games


def reduce_monfg(monfg, player_actions, u_tpl):
    """
    This function will reduce the MONFG to an NFG as a list of payoff matrices.
    :param monfg: The input MONFG.
    :param player_actions: A tuple of the amount of actions per player.
    :param u_tpl: A tuple of utility functions.
    :return: An NFG.
    """
    nfg = []  # Collect the payoff matrices.
    for u in u_tpl:
        scalarised_payoff = games.scalarise_matrix(monfg, u, player_actions)  # Scalarise the MONFG.
        nfg.append(scalarised_payoff)
    return nfg


# Works only for two player games now
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
            max_idx = list(idx)
            del max_idx[player]  # Find the opponent strategy that corresponds with this joint strategy.
            max = maxima[max_idx]  # Get the payoff of the best response to this opponent strategy.
            if payoffs[idx] >= max:  # If the payoff of this joint strategy is equal or greater.
                best_response_matrix[idx] = True  # It is a best response to the opponent strategies.

        best_responses.append(best_response_matrix)

    nash_equilibria = np.logical_and(best_responses[0], best_responses[1])  # Best response to a best response is NE.
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


def print_psne(psne_lst):
    """
    This function will pretty print the list of PSNE.
    :param psne_lst: A list of PSNE.
    :return: /
    """
    print('There are a total of ' + repr(len(psne_lst)) + ' pure strategy Nash equilibria')
    for psne in psne_lst:
        print(repr(psne))


if __name__ == '__main__':
    u_tpl = (games.u1, games.u2)
    monfg = games.get_payoff_matrix('game1')
    player_actions = monfg.shape[:-1]  # Get the number of actions available to each player.
    psne_lst = find_all_psne(monfg, player_actions, u_tpl)
    print_psne(psne_lst)
