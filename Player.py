import numpy as np
from best_response import best_response


class IBRPlayer:
    """
    A class implementing a player that learns using the iterated best response algorithm.
    """
    def __init__(self, id, u, num_actions, payoff_matrix, init_strategy=None):
        self.id = id
        self.u = u
        self.num_actions = num_actions
        self.payoff_matrix = payoff_matrix
        if init_strategy is None:
            self.strategy = np.full(self.num_actions, 1 / self.num_actions)
        else:
            self.strategy = init_strategy

    def update_strategy(self, joint_strategy):
        """
        This function updates the current strategy of the player by calculating a best response to the other players'
        strategies.
        :param joint_strategy: The current joint strategy of all players.
        :return: Whether the strategy has converged and the best response strategy.
        """
        br = best_response(self.u, self.id, self.payoff_matrix, joint_strategy)
        if (br == self.strategy).all():
            done = True
        else:
            done = False
        self.strategy = br
        return done, br


class FPPlayer:
    """
    A class implementing a player that learns using fictitious play.
    """
    def __init__(self, id, u, player_actions, payoff_matrix, init_strategy=None):
        self.id = id
        self.u = u
        self.player_actions = player_actions
        self.num_actions = player_actions[id]
        self.payoff_matrix = payoff_matrix
        if init_strategy is None:
            self.strategy = np.full(self.num_actions, 1 / self.num_actions)
        else:
            self.strategy = init_strategy
        self.empirical_strategies = [np.zeros(num_actions) for num_actions in player_actions]

    def select_action(self):
        """
        Select a random action using the current strategy.
        :return: An action.
        """
        return np.random.choice(range(self.num_actions), p=self.strategy)

    def calc_joint_strategy(self):
        """
        This function calculates the empirical joint strategy.
        :return: The joint strategy.
        """
        joint_strategy = []
        for player_actions in self.empirical_strategies:
            strategy = player_actions / np.sum(player_actions)
            joint_strategy.append(strategy)
        return joint_strategy

    def update_strategy(self):
        """
        This function updates the strategy of the player by calculating a best response to the empirical joint strategy.
        :return: Whether the strategy has converged and the best response strategy.
        """
        joint_strategy = self.calc_joint_strategy()
        br = best_response(self.u, self.id, self.payoff_matrix, joint_strategy)
        if (br == self.strategy).all():
            done = True
        else:
            done = False
        self.strategy = br
        return done, br

    def update_joint_states(self, actions):
        """
        Update the empirical strategy of all players.
        :param actions: The actions that are taken by the players.
        :return: /
        """
        for player, action in enumerate(actions):
            self.empirical_strategies[player][action] += 1
