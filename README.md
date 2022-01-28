# Nash Equilibria in Multi-Objective Normal-Form Games
This repository contains algorithms for calculating or learning (pure strategy) Nash Equilibria (NE) in Multi-Objective Normal-Form Games (MONFGs). We aim to add more algorithms to this repository over time as research into this area continues.


Below we present all algorithms and give an example of their output on the following MONFG with two objectives (x, y):

|  | A | B | C |
|---|:---:|:---:|:---:|
| **A** | (4, 1); (4, 0) | (1, 2); (3, 1) | (2, 1); (2, 2) |
| **B** | (3, 1); (3, 1) | (3, 2); (2, 2) | (1, 2); (1, 3) |
| **C** | (1, 2); (2, 2) | (2, 1); (1, 3) | (1, 3); (0, 4) |

Unless explicitly stated otherwise, we use the following utility functions:
 1) Player 1: u(x, y) = x² + y²
 2) Player 2: u(x, y) = x² + xy + y²


## Pure Strategy Nash Equilibria
The first algorithm in this repository is able to calculate all Pure Strategy Nash Equilibria (PSNE) in a MONFG when given only quasiconvex utility functions. Due to the theorems shown in the paper, the PSNE retrieved using this algorithm must necessarily represent all PSNE in the MONFG under ESR, SER and any blended setting.

The algorithm can be found in [PSNE.py](PSNE.py) and can easily be called from [main.py](main.py) by adding the ``--algorithm PSNE`` flag.

In the example MONFG, it successfully finds the PSNE of (A, A) and (C, C). The first PSNE leads to a utility of 17 for player 1 and 16 for player 2. The second PSNE leads to a utility of 10 for player 1 and 16 for player 2.

Note that this algorithm can easily be adapted to output only a sample PSNE (i.e. a subset or just the first).

## Iterated Best Response
Iterated Best Response (IBR) is a learning algorithm that was adapted from single-objective games to work with MONFGs as well. It is not guaranteed to find a Nash equilibrium as it can end up in cycles.

The algorithm can be found in [IBR.py](IBR.py) and can easily be called from [main.py](main.py) by adding the ``--algorithm IBR`` flag. We have implemented two variants, simultaneous and alternating IBR, that can also be selected using the flag ``--variant``.

In the example MONFG, it successfully finds the mixed strategy NE with strategy [0, 1, 0] for player 1 and [1/3, 1/3, 1/3] for player 2. This leads to a utility of 8.2222 for player 1 and 12 for player 2.

## Fictitious Play
Fictitious Play (FP) is a learning algorithm that was adapted from single-objective games to work with MONFGs as well. It is not guaranteed to find a Nash equilibrium as it can end up in cycles.

The algorithm can be found in [fictitious_play.py](fictitious_play.py) and can easily be called from [main.py](main.py) by adding the ``--algorithm FP`` flag. We have implemented two variants, simultaneous and alternating FP, that can also be selected using the flag ``--variant``.

In the example MONFG, it successfully finds the PSNE (A, A). This leads to a utility of 17 for player 1 and 16 for player 2.

## Cite
Please use the following citation if you use these algorithms in your work.
```
@misc{ropke2021nash,
      title={On Nash Equilibria in Normal-Form Games With Vectorial Payoffs}, 
      author={Willem Röpke and Diederik M. Roijers and Ann Nowé and Roxana Rădulescu},
      year={2021},
      eprint={2112.06500},
      archivePrefix={arXiv},
      primaryClass={cs.GT}
}
```