import numpy as np

# Game 1: The (im)balancing act game. There are no NE under SER.
payoff1 = np.array([[(4, 0), (3, 1), (2, 2)],
                    [(3, 1), (2, 2), (1, 3)],
                    [(2, 2), (1, 3), (0, 4)]])

# Game 2: The (im)balancing act game without M. There are no NE under SER.
payoff2 = np.array([[(4, 0),  (2, 2)],
                    [(2, 2),  (0, 4)]])

# Game 3: The (im)balancing act game without R. (L, M) is a pure NE under SER.
payoff3 = np.array([[(4, 0), (3, 1)],
                    [(3, 1), (2, 2)]])

# Game 4: A two action game. There are NE under SER for (L,L) and (M,M).
payoff4 = np.array([[(4, 1), (1, 2)],
                    [(3, 1), (3, 2)]])

# Game 5: A three action game. There are  NE under SER for (L,L), (M,M) and (R,R).
payoff5 = np.array([[(4, 1), (1, 2), (2, 1)],
                    [(3, 1), (3, 2), (1, 2)],
                    [(1, 2), (2, 1), (1, 3)]])


def u1(vector):
    """
    This function calculates the utility for agent 1.
    :param vector: The reward vector.
    :return: The utility for agent 1.
    """
    utility = vector[0] ** 2 + vector[1] ** 2
    return utility


def u2(vector):
    """
    This function calculates the utility for an agent.
    :param vector: The reward vector.
    :return: The utility for an agent.
    """
    utility = vector[0] ** 2 + vector[0]*vector[1] + vector[1] ** 2
    return utility


def get_payoff_matrix(game):
    """
    This function will provide the correct payoff game based on the game we play.
    :param game: The current game.
    :return: A payoff matrix.
    """
    if game == 'game1':
        payoff_matrix = payoff1
    elif game == 'game2':
        payoff_matrix = payoff2
    elif game == 'game3':
        payoff_matrix = payoff3
    elif game == 'game4':
        payoff_matrix = payoff4
    elif game == 'game5':
        payoff_matrix = payoff5
    else:
        raise Exception("The provided game does not exist.")

    return payoff_matrix


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

    for i in range(num_strategies):
        idx = np.unravel_index(i, player_actions)
        utility = u(payoff_matrix[idx])
        scalarised_matrix[idx] = utility

    return scalarised_matrix
