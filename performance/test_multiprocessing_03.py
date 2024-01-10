#!/usr/bin/env python
# -*- coding:utf-8 -*-

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


def run_multi_task(task_type: str, *args: Any) -> None:
    """
    Run multiple processes.

    Args
    ----
    task_type: string
        The type of the task to run.
    args: Any
        Parameters of each computation task.
    """
    start_time = time.time()
    number_of_processes = multiprocessing.cpu_count()
    # TODO: `number_of_processes` can be delivered
    # by a command-line argument.

    with multiprocessing.Pool(processes=number_of_processes) as pool:
        results = pool.starmap(
            ComputationTask(),
            [(task_type, *args) for _ in range(number_of_processes)]
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


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run multiple computation tasks."
    )
    parser.add_argument(
        "task_type",
        choices=["matrix", "prime", "fibonacci"],
        help="The type of the task to perform."
    )
    parser.add_argument(
        "--matrix_size",
        type=int,
        default=1000,
        help="The size of the matrix (NumPy array) to be created."
    )
    parser.add_argument(
        "--prime_range",
        type=int,
        default=1000,
        help="The upper limit of the range of the prime numbers."
    )
    parser.add_argument(
        "--sequence_length",
        type=int,
        default=20,
        help="The length of the Fibonacci sequence."
    )

    command_args = parser.parse_args()

    if command_args.task_type == "matrix":
        size_of_matrix = int(
            input("Please enter the size of the matrix: ")
        )
        run_multi_task(command_args.task_type, size_of_matrix)

    elif command_args.task_type == "prime":
        range_of_prime_numbers = int(
            input("Please enter the range of the prime numbers: ")
        )
        run_multi_task(command_args.task_type, range_of_prime_numbers)

    elif command_args.task_type == "fibonacci":
        length_of_fibonacci_sequence = int(
            input("Please enter the length of the Fibonacci sequence: ")
        )
        run_multi_task(command_args.task_type, length_of_fibonacci_sequence)
