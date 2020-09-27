"""
Author:     David Walshe
Date:       27 September 2020
"""

# Core Libs
from typing import Tuple
import logging
from time import perf_counter_ns

# 3rd Party
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def timeit(func: callable):
    """
    Simple timer function to record performance in nanoseconds.
    """
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        res = func(*args, **kwargs)
        end = perf_counter_ns()
        logger.info(f"{func.__name__} took {end - start}ns.")

        return res

    return wrapper


# ===========================================================================================
# "parse_in" functions.
# ===========================================================================================

def parse_in(input_file: str):
    """
    Reads an input file and returns a tuple of (num_rows, num_columns, matrix).

    :param input_file: The file to read data from.
    :return: A 3-element tuple of (num_rows, num_columns, matrix).
    """
    with open(input_file, "r") as fh:
        N, M = read_dimensions(fh.readline())
        string_matrix = fh.read()
        read_matrix(N, M, string_matrix)


def read_dimensions(line: str) -> Tuple[int, int]:
    """
    Reads the size of the minefield array from the passed line (first_line).

    :param line: The line to parse dimensions from.
    :return: The N (Height) and M (Width) of the array.
    """
    try:
        N, M = line.strip().split(" ")

        return int(N), int(M)

    except Exception as e:
        logger.error(f"Cannot parse N & M from first line of input file. \n{e.__str__()}")


@timeit
def read_matrix(N: int, M: int, lines: str) -> np.array:
    """
    Converts the input file data into a numpy array.


    :param N: The height of the input matrix.
    :param M: The width of the input matrix.
    :param lines: The textual data containing the array.
    :return: The data as an numpy array.
    """
    np.empty((N, M))



# ===========================================================================================
# "solve" functions.
# ===========================================================================================

def solve():
    pass


# ===========================================================================================
# "parse_out" functions.
# ===========================================================================================


def parse_out():
    pass


# ===========================================================================================
# "main" functions.
# ===========================================================================================


def main():
    parse_in("./input/input_1.txt")


if __name__ == '__main__':
    main()
