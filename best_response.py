import games
import numpy as np
import scipy.optimize as opt

'''
def calc_expected_vec(policy, returns):
    """
    This method calculates the expected vector for a policy and matrix of reward vectors.
    :param policy: The policy.
    :param returns: The matrix of reward vectors.
    :return: The expected vector when applying this policy on the reward vectors.
    """
    return policy @ returns


def calc_ser(self, policy, returns):
    """
    This method calculates the scalarised expected returns for a policy and returns.
    :param policy: An action distribution.
    :param returns: A array of reward vectors.
    :return: The SER.
    """
    expected_vec = calc_expected_vec(policy, returns)
    ser = u(expected_vec)
    return ser


def objective(strategy):
    """
    The objective to minimize for.
    :param policy: The current guess for optimal policy.
    :return: The negative SER from this policy because we want to minimize it.
    """
    returns = q_table[state]
    return - calc_ser(policy, returns)
'''


def best_response(u, player, payoff_matrix, joint_strategy):
    """
    This function calculates a best response given a payoff matrix and the opponent strategies.
    :param u: The utility function.
    :param payoff_matrix: The payoff matrix.
    :param op_strategies: The opponent strategies. This looks as follows [[p1,1, .., p1,k], ..., [pi,1, ..., pi,l]]
    :return: A best response strategy.
    """
    num_objectives = payoff_matrix.shape[-1]
    num_actions = len(joint_strategy[player])
    num_players = len(joint_strategy)
    opponents = np.delete(np.arange(num_players), player)
    expected_returns = payoff_matrix

    for opponent in opponents:  # Loop over all opponent strategies.
        strategy = joint_strategy[opponent]  # Get this opponent's strategy.

        # We reshape this strategy to be able to multiply along the correct axis for weighting expected returns.
        # For example if you end up in [1, 2] or [2, 3] with 50% probability.
        # We calculate the individual expected returns first: [0.5, 1] or [1, 1.5]
        dim_array = np.ones((1, expected_returns.ndim), int).ravel()
        dim_array[opponent] = -1
        strategy_reshaped = strategy.reshape(dim_array)

        expected_returns = expected_returns * strategy_reshaped  # Calculate the probability of a joint state occurring.
        # We now take the sum of the weighted returns to get the expected returns.
        # We need keepdims=True to make sure that the opponent still exists at the correct axis, their action space is
        # just reduced to one action resulting in the expected return now.
        expected_returns = np.sum(expected_returns, axis=opponent, keepdims=True)

    expected_returns = expected_returns.reshape(num_actions, num_objectives)
    print(expected_returns)
    best_response = np.zeros(3)
    return best_response


if __name__ == '__main__':
    u = games.u1
    monfg = games.get_monfg('game9')
    player_actions = monfg[0].shape[:-1]  # Get the number of actions available to each player.
    player = 1
    strategy = [np.array([0.5, 0.3, 0.2]), np.array([0.2, 0.8]), np.array([1., 0., 0.])]  # Necessary for NumPy.
    best_response(u, player, monfg[player], strategy)
