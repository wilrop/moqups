# Pure Strategy Nash Equilibria in Multi-Objective Games
This repository contains the MOQUPS algorithm which computes all pure strategy Nash equilibria (PSNE) in Multi-Objective Normal-Form Games (MONFGs). We present the algorithm below and give an example of its output on the following MONFG with two objectives (x, y):

|  | A | B | C |
|---|:---:|:---:|:---:|
| **A** | (4, 1); (4, 0) | (1, 2); (3, 1) | (2, 1); (2, 2) |
| **B** | (3, 1); (3, 1) | (3, 2); (2, 2) | (1, 2); (1, 3) |
| **C** | (1, 2); (2, 2) | (2, 1); (1, 3) | (1, 3); (0, 4) |

We use the following utility functions:
 1) Player 1: u(x, y) = x² + y²
 2) Player 2: u(x, y) = x² + xy + y²


## MOQUPS
MOQUPS, Multi-Objective and Quasiconvex Utilities for Pure Strategies, is able to compute all PSNE in an MONFG when given only quasiconvex utility functions. Due to the theorems shown in the paper, the PSNE retrieved using this algorithm must necessarily represent all PSNE in the MONFG under ESR, SER and any blended setting.

The algorithm is found in [moqups.py](moqups.py) and can be called using several parameters. For an overview of all parameters, execute the following command ``python moqups.py --help``.

In the example MONFG, it successfully finds the PSNE of (A, A) and (C, C). The first PSNE leads to a utility of 17 for player 1 and 16 for player 2. The second PSNE leads to a utility of 10 for player 1 and 16 for player 2.

Note that this algorithm can easily be adapted to output a sample PSNE by, for example, returning the first PSNE that is found.

## Cite
Please use the following citation if you use this algorithm in your work.
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