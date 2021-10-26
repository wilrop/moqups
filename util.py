def print_psne(psne_lst):
    """
    This function will pretty print the list of PSNE.
    :param psne_lst: A list of PSNE.
    :return: /
    """
    print('There are a total of ' + repr(len(psne_lst)) + ' pure strategy Nash equilibria')
    for psne in psne_lst:
        print(repr(psne))


def print_ne(ne):
    """
    This function will pretty print a Nash equilibrium
    :param ne: The joint strategy.
    :return: /
    """
    print('The Nash equilibrium that was found is the joint strategy ' + repr(ne))


def print_all_ne(ne_lst):
    """
    This function will pretty print the list of Nash equilibria.
    :param ne_lst: A list of Nash equilibria.
    :return: /
    """
    print('There are a total of ' + repr(len(ne_lst)) + ' Nash equilibria')
    for ne in ne_lst:
        print(repr(ne))


def print_start(algorithm):
    """
    This function will pretty print the introduction to an algorithm.
    :param algorithm: The name of the algorithm.
    :return: /
    """
    print(f'Executing the {algorithm} algorithm')
    print(f'-----------------------------------------------------')
