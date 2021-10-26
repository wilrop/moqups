import numpy as np
from best_response import best_response


class IBRAgent:
    def __init__(self, id, u, num_actions, payoff_matrix, init_strategy=None):
        self.id = id
        self.u = u
        self.num_actions = num_actions
        self.payoff_matrix = payoff_matrix
        if init_strategy is None:
            self.strategy = np.full(self.num_actions, 1 / self.num_actions)
        else:
            self.strategy = init_strategy

    def update_policy(self, joint_strategy):
        br = best_response(self.u, self.id, self.payoff_matrix, joint_strategy)
        if (br == self.strategy).all():
            done = True
        else:
            done = False
        self.strategy = br
        return done, br


class FPAgent:
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
        self.joint_states = np.zeros(player_actions)

    def calc_joint_strategy(self):
        joint_strategy = []
        for player_actions in self.joint_states:
            strategy = player_actions / np.sum(player_actions)
            joint_strategy.append(strategy)
        return joint_strategy

    def update_policy(self):
        joint_strategy = self.calc_joint_strategy()
        br = best_response(self.u, self.id, self.payoff_matrix, joint_strategy)
        if (br == self.strategy).all():
            done = True
        else:
            done = False
        self.strategy = br
        return done, br

    def update_joint_states(self, actions):
        for player, action in enumerate(actions):
            self.joint_states[player, action] += 1
