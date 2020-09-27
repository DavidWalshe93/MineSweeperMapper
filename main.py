"""
Author:     David Walshe
Date:       27 September 2020
"""

# Core Libs
from typing import Tuple
import logging
import logging.config
from time import perf_counter_ns

# 3rd Party
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def timeit(stage_name: str = None):
    """
    Simple timer function to record performance in nanoseconds.

    :param stage_name: Mark the beginning of a stage.
    """
    def _timeit(func: callable):

        def wrapper(*args, **kwargs):
            if stage_name is not None:
                logger.info(f"====================================")
                logger.info(f"Stage: {stage_name}")
                logger.info(f"====================================")
            start = perf_counter_ns()
            res = func(*args, **kwargs)
            end = perf_counter_ns()
            logger.info(f"{func.__name__} took {end - start}ns.")

            return res

        return wrapper

    return _timeit


# ===========================================================================================
# "parse_in" functions.
# ===========================================================================================

@timeit("Parse In")
def parse_in(input_file: str):
    """
    Reads an input file and returns a tuple of (num_rows, num_columns, matrix).

    :param input_file: The file to read data from.
    :return: A 3-element tuple of (num_rows, num_columns, matrix).
    """
    with open(input_file, "r") as fh:
        num_rows, num_columns = read_dimensions(fh.readline())
        string_matrix = fh.read()
        matrix = read_matrix(num_rows, num_columns, string_matrix)

        return num_rows, num_columns, matrix


@timeit()
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


@timeit()
def read_matrix(N: int, M: int, string_matrix: str) -> np.array:
    """
    Converts the input file data into a numpy array.


    :param N: The height of the input matrix.
    :param M: The width of the input matrix.
    :param string_matrix: The textual data containing the array.
    :return: The data as an numpy array.
    """
    items = string_matrix.strip().replace("\n", " ").split(" ")
    matrix = np.array(items)

    # Reshape the array into the desired size.
    return matrix.reshape((N, M))


# ===========================================================================================
# "solve" functions.
# ===========================================================================================

@timeit(stage_name="Solve")
def solve(num_rows: int, num_columns: int, matrix: np.array):
    """
    Solves the minefield plotting from a given input matrix, matrix.

    :param num_rows: The number of row in the matrix.
    :param num_columns: The number of columns in the matrix.
    :param matrix: The matrix to process.
    :return: The Matrix mapping output.
    """

    # Create empty minefield for population.
    matrix_sol = np.full((num_rows, num_columns), fill_value="0", dtype=str)

    x_locations, y_locations = np.where(matrix == "y")

    # If there is no mines return empty matrix.
    if x_locations is not None and y_locations is not None:

        for x, y in zip(x_locations, y_locations):
            # Mark Mine
            matrix_sol[x, y] = "x"

            # For each surrounding mine column.
            for i in range(x-1, x+2):
                # Check within X-axis bounds.
                if 0 <= i < num_rows:
                    # For each surrounding mine row.
                    for j in range(y-1, y+2):
                        # Check within Y-axis bounds
                        if 0 <= j < num_columns:
                            # Obtain current item value to update.
                            current_value = matrix_sol[i, j]
                            # Only update if the item is not a mine.
                            if current_value != "x":
                                # Convert to a int for addition.
                                current_value = int(current_value)
                                current_value += 1
                                # Reassign updated value.
                                matrix_sol[i, j] = current_value

    return matrix_sol


# ===========================================================================================
# "parse_out" functions.
# ===========================================================================================


def parse_out():
    pass


# ===========================================================================================
# "main" functions.
# ===========================================================================================


def main():
    N, M, matrix = parse_in("./input/input_1.txt")
    matrix_sol = solve(N, M, matrix)


if __name__ == '__main__':
    main()
