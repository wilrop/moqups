import numpy as np


# Game 1: A 3-action 2-player game with team rewards.
# This game has two PSNE using u1 and u2: [0, 0], [2, 2]
# Checked for correctness using Gambit.
monfg1 = [
    np.array([[(4, 0), (3, 1), (2, 2)],
              [(3, 1), (2, 2), (1, 3)],
              [(2, 2), (1, 3), (0, 4)]]),
    np.array([[(4, 0), (3, 1), (2, 2)],
              [(3, 1), (2, 2), (1, 3)],
              [(2, 2), (1, 3), (0, 4)]])
]

# Game 2: A 2-action 2-player game with team rewards.
# This game has two PSNE using u1 and u2: [0, 0], [1, 1]
# Checked for correctness using Gambit.
monfg2 = [
    np.array([[(4, 0), (2, 2)],
              [(2, 2), (0, 4)]]),
    np.array([[(4, 0), (2, 2)],
              [(2, 2), (0, 4)]])
]

# Game 3: A 2-action 2-player game with team rewards.
# This game has one PSNE using u1 and u2: [0, 0]
# Checked for correctness using Gambit.
monfg3 = [
    np.array([[(4, 0), (3, 1)],
              [(3, 1), (2, 2)]]),
    np.array([[(4, 0), (3, 1)],
              [(3, 1), (2, 2)]])
]

# Game 4: A 2-action 2-player game with team rewards.
# This game has two PSNE using u1 and u2: [0, 0], [1, 1]
# Checked for correctness using Gambit.
monfg4 = [
    np.array([[(4, 1), (1, 2)],
              [(3, 1), (3, 2)]]),
    np.array([[(4, 1), (1, 2)],
              [(3, 1), (3, 2)]])
]

# Game 5: A 3-action 2-player game with team rewards.
# This game has three PSNE using u1 and u2: [0, 0], [1, 1], [2, 2]
# Checked for correctness using Gambit.
monfg5 = [
    np.array([[(4, 1), (1, 2), (2, 1)],
              [(3, 1), (3, 2), (1, 2)],
              [(1, 2), (2, 1), (1, 3)]]),
    np.array([[(4, 1), (1, 2), (2, 1)],
              [(3, 1), (3, 2), (1, 2)],
              [(1, 2), (2, 1), (1, 3)]])
]

# Game 6: A 3-action 2-player game with individual rewards.
# This game has two PSNE using u1 and u2: [0, 0], [2, 2]
# Checked for correctness using Gambit.
monfg6 = [
    np.array([[(4, 1), (1, 2), (2, 1)],
              [(3, 1), (3, 2), (1, 2)],
              [(1, 2), (2, 1), (1, 3)]]),
    np.array([[(4, 0), (3, 1), (2, 2)],
              [(3, 1), (2, 2), (1, 3)],
              [(2, 2), (1, 3), (0, 4)]])
]

# Game 7: A 3-action 2-player game with individual rewards.
# This game has no PSNE using u1 and u2.
# Checked for correctness using Gambit.
monfg7 = [
    np.array([[(2, 3), (3, 2), (1, 1)],
              [(2, 5), (0, 2), (5, 2)],
              [(1, 3), (4, 0), (1, 3)]]),
    np.array([[(0, 3), (1, 2), (2, 1)],
              [(2, 2), (3, 2), (1, 2)],
              [(3, 1), (0, 3), (1, 0)]])
]

# Game 8: A 2-action 3-player game with individual rewards.
# This game has two PSNE using u1, u2 and u3: [0, 1, 1], [1, 0, 1]
# Checked for correctness by hand.
monfg8 = [
    np.array([[[(1, 0), (2, 1)],
               [(3, 0), (1, 2)]],
              [[(0, 2), (2, 2)],
               [(3, 1), (2, 0)]]]),
    np.array([[[(2, 0), (0, 2)],
               [(1, 1), (1, 2)]],
              [[(0, 0), (1, 2)],
               [(2, 1), (0, 0)]]]),
    np.array([[[(1, 2), (2, 1)],
               [(0, 1), (2, 2)]],
              [[(1, 1), (0, 3)],
               [(1, 1), (1, 2)]]])
]

# Game 9: A 3-player game where player 1 has 3 actions, player 2 has 2 and player 3 has 3, with individual rewards.
# This game has three PSNE using u1, u2 and u3: [0, 1, 1], [1, 0, 2], [1, 1, 0]
# Checked for correctness by hand.
monfg9 = [
    np.array([[[(1, 0), (2, 1), (1, 2)],
               [(3, 0), (1, 2), (2, 2)]],
              [[(0, 2), (2, 2), (3, 0)],
               [(3, 1), (2, 0), (0, 1)]],
              [[(1, 1), (0, 0), (2, 1)],
               [(1, 2), (2, 0), (3, 0)]]]),
    np.array([[[(0, 2), (0, 1), (1, 1)],
               [(1, 3), (2, 2), (2, 2)]],
              [[(0, 2), (2, 0), (3, 0)],
               [(3, 1), (1, 0), (2, 1)]],
              [[(2, 2), (2, 1), (2, 0)],
               [(0, 1), (1, 3), (1, 1)]]]),
    np.array([[[(1, 3), (1, 1), (2, 2)],
               [(2, 1), (2, 3), (2, 0)]],
              [[(0, 2), (1, 1), (3, 1)],
               [(3, 1), (2, 1), (2, 1)]],
              [[(0, 1), (1, 0), (0, 0)],
               [(1, 1), (2, 1), (1, 1)]]])
]


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
    utility = vector[0] ** 2 + vector[0] * vector[1] + vector[1] ** 2
    return utility


def u3(vector):
    """
    This function calculates the utility for an agent.
    :param vector: The reward vector.
    :return: The utility for an agent.
    """
    utility = vector[0] ** 2 + vector[1]
    return utility


def u4(vector):
    """
    This function calculates the utility for an agent.
    :param vector: The reward vector.
    :return: The utility for an agent.
    """
    utility = vector[0] + vector[1] ** 2
    return utility


def get_monfg(game):
    """
    This function will provide the correct multi-objective normal-form game based on the game that is requested.
    :param game: The current game.
    :return: A list of payoff matrices.
    """
    if game == 'game1':
        monfg = monfg1
    elif game == 'game2':
        monfg = monfg2
    elif game == 'game3':
        monfg = monfg3
    elif game == 'game4':
        monfg = monfg4
    elif game == 'game5':
        monfg = monfg5
    elif game == 'game6':
        monfg = monfg6
    elif game == 'game7':
        monfg = monfg7
    elif game == 'game8':
        monfg = monfg8
    elif game == 'game9':
        monfg = monfg9
    else:
        raise Exception("The provided game does not exist.")

    return monfg
