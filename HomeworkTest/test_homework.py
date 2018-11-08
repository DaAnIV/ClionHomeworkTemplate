import os
import py
import pytest
import pprint


def test_hw0q1(run_homework_and_assert):
    run_homework_and_assert(0, 1, 1)


@pytest.mark.parametrize("input_output_index", range(1, 5))
def test_hw1q1(run_homework_and_assert, input_output_index):
    run_homework_and_assert(1, 1, input_output_index)


@pytest.mark.parametrize("input_output_index", range(1, 7))
def test_hw1q2(run_homework_and_assert, input_output_index):
    run_homework_and_assert(1, 2, input_output_index)