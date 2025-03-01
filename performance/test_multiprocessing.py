#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Please refer to:
https://zhuanlan.zhihu.com/p/56922793
"""

import argparse
import multiprocessing
import time
from typing import Any

import numpy as np


class ComputationTask(object):
    """
    The computation task, as a callable object.

    Attributes
    ----------
    task_name: string
        The name of the task to run.
    args: Any
        Parameters of each computation task
        which is an instance method of `ComputationTask`.
    """
    def __call__(self, task_name: str, *args: Any) -> Any:
        if task_name == "matrix":
            return self.dot_product_of_matrices(*args)
        elif task_name == "prime":
            return self.prime_numbers(*args)
        elif task_name == "fibonacci":
            return self.fibonacci_sequence(*args)
        else:
            raise ValueError(f'Invalid task name: "{task_name}"')

    def dot_product_of_matrices(self, matrix_size: int) -> Any:
        """
        Calculate the dot product of two arrays.

        Args
        ----
        matrix_size: integer
            The size of the matrix (NumPy array) to be created.
        """
        return np.dot(
            np.random.rand(matrix_size, matrix_size),
            np.random.rand(matrix_size, matrix_size)
        )

    def prime_numbers(self, prime_range: int) -> list:
        """
        Find prime numbers in the specified range.

        Args
        ----
        prime_range: integer
            The upper limit of the range of the prime numbers.
        """
        return [
            num
            for num in range(2, prime_range)
            if all(
                num % i != 0
                for i in range(2, int(num**0.5) + 1)
            )
        ]

    def fibonacci_sequence(self, sequence_length: int) -> list:
        """
        Calculate the Fibonacci sequence with the given length.

        Args
        ----
        sequence_length: integer
            The length of the Fibonacci sequence.
        """
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < sequence_length:
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence


def run_multi_tasks(type_of_tasks: str,
                    number_of_tasks: int,
                    *args: Any) -> None:
    """
    Run multiple processes.

    Args
    ----
    type_of_tasks: string
        The type of the task / tasks to run.
    number_of_tasks: integer
        The number of the task / tasks to run.
    args: Any
        Parameters of each computation task.
    """
    start_time = time.time()
    number_of_processes = number_of_tasks if number_of_tasks else multiprocessing.cpu_count()
    # TODO: Please reconsider the ternary operator.

    with multiprocessing.Pool(processes=number_of_processes) as pool:
        results = pool.starmap(
            ComputationTask(),
            [(type_of_tasks, *args) for _ in range(number_of_processes)]
        )
        # TODO: While identical jobs are running here,
        # it is expected to run various jobs at the same time
        # or to run one job in multiple threads
        # and shared memory (`threading`).

    for i, result in enumerate(results):
        print(f"Result from process {i + 1}: \n {result}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Number of processes: {number_of_processes}")
    print(f"Elapsed time: {elapsed_time} seconds")


def main() -> None:
    """
    The main function.
    """
    parser = argparse.ArgumentParser(
        prog="test_multiprocessing",
        description="Run multiple computation tasks.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--task-type",
        choices=["matrix", "prime", "fibonacci"],
        help="The type of the task / tasks to perform."
    )
    parser.add_argument(
        "--matrix-size",
        type=int,
        default=10,
        help="The size of the matrix (NumPy array) to be created."
    )
    parser.add_argument(
        "--prime-range",
        type=int,
        default=100,
        help="The upper limit of the range of the prime numbers."
    )
    parser.add_argument(
        "--sequence-length",
        type=int,
        default=10,
        help="The length of the Fibonacci sequence."
    )
    parser.add_argument(
        "--task-number",
        type=int,
        default=1,
        help="The number of the task / tasks to perform."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version="%(prog)s 0.2.1"
    )

    command_args = parser.parse_args()

    if command_args.task_type == "matrix":
        run_multi_tasks(
            command_args.task_type,
            command_args.task_number,
            command_args.matrix_size
        )

    elif command_args.task_type == "prime":
        run_multi_tasks(
            command_args.task_type,
            command_args.task_number,
            command_args.prime_range
        )

    elif command_args.task_type == "fibonacci":
        run_multi_tasks(
            command_args.task_type,
            command_args.task_number,
            command_args.sequence_length
        )

    else:
        parser.print_usage()


if __name__ == "__main__":

    main()
