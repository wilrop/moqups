import argparse
import time
import numpy as np

import util
import games

from PSNE import find_all_psne
from IBR import iterated_best_response
from fictitious_play import fictitious_play


def execute_algorithm(args):
    """
    This function executes the requested algorithm with the arguments provided by the user.
    :param args: The provided arguments by the user.
    :return: /
    """
    start = time.time()  # Start measuring the time.

    if args.seed is not None:
        np.random.seed(args.seed)  # Set the numpy seed.

    if args.game == 'random':  # We get the game
        player_actions = tuple(args.player_actions)
        monfg = games.generate_random_monfg(player_actions, args.num_objectives, args.lower_bound, args.upper_bound)
    else:
        monfg = games.get_monfg(args.game)

    player_actions = monfg[0].shape[:-1]  # Get the number of actions available to each player.
    u_tpl = tuple([games.get_u(u_str) for u_str in args.u])

    algorithm = args.algorithm
    variant = args.variant
    iterations = args.iterations

    if algorithm == 'PSNE':
        psne_lst = find_all_psne(monfg, player_actions, u_tpl)
        util.print_psne(psne_lst)
    elif algorithm == 'IBR':
        ne, final_strategy = iterated_best_response(u_tpl, player_actions, monfg, max_iter=iterations, variant=variant)
        util.print_ne(ne, final_strategy)
    elif algorithm == 'FP':
        ne, final_strategy = fictitious_play(u_tpl, player_actions, monfg, max_iter=iterations, variant=variant)
        util.print_ne(ne, final_strategy)
    else:
        raise Exception('The requested algorithm does not exist')

    end = time.time()
    elapsed_secs = (end - start)
    print("Seconds elapsed: " + str(elapsed_secs))


if __name__ == '__main__':
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()

        parser.add_argument('--algorithm', type=str, default='PSNE', choices=['PSNE', 'FP', 'IBR'])
        parser.add_argument('--game', type=str, default='game1', help='The MONFG to play')
        parser.add_argument('--u', type=str, default=['u1', 'u1'], nargs='+', help="The utility functions to use.")
        parser.add_argument('--seed', type=int, help='The seed used in all randomisation')
        parser.add_argument('--player_actions', type=int, nargs='+', default=[5, 5],
                            help='The number of actions per player')
        parser.add_argument('--variant', type=str, default='alternating', choices=['simultaneous', 'alternating'],
                            help='The variant of the algorithm if applicable')
        parser.add_argument('--iterations', type=int, default=1000, help='The maximum number of iterations')
        parser.add_argument('--num_objectives', type=int, default=2,
                            help='The number of objectives for the random MONFG')
        parser.add_argument('--lower_bound', type=int, default=0, help='The lower reward bound')
        parser.add_argument('--upper_bound', type=int, default=5, help='The upper reward bound')

        args = parser.parse_args()
        execute_algorithm(args)
