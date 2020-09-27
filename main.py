"""
Author:     David Walshe
Date:       27 September 2020
"""

# Core Libs
from typing import Tuple
import logging

# 3rd Party
import numpy as np


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_dimensions(line: str) -> Tuple[int, int]:
    """
    Reads the size of the minefield array from the passed line (first_line).

    :param line: The line to parse dimensions from.
    :return: The N (Height) and M (Width) of the array.
    """
    try:
        N, M = line.strip().split(" ")

        return N, M

    except Exception as e:
        logger.error(f"Cannot parse N & M from first line of input file. \n{e.__str__()}")


def parse_in(input_file: str) :
    """
    Reads an input file and returns a tuple of (num_rows, num_columns, matrix).

    :param input_file: The file to read data from.
    :return: A 3-element tuple of (num_rows, num_columns, matrix).
    """
    with open(input_file, "r") as fh:
        print(read_dimensions(fh.readline()))


def solve():
    pass


def parse_out():
    pass


def main():
    parse_in("./input/input_1.txt")


if __name__ == '__main__':
    main()
