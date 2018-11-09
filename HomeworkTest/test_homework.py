import pytest


@pytest.mark.parametrize("test_index", range(1))
def test_hw0q1(run_homework_and_assert, test_index):
    run_homework_and_assert(0, 1, test_index)


@pytest.mark.parametrize("test_index", range(4))
def test_hw1q1(run_homework_and_assert, test_index):
    run_homework_and_assert(1, 1, test_index)


@pytest.mark.parametrize("test_index", range(6))
def test_hw1q2(run_homework_and_assert, test_index):
    run_homework_and_assert(1, 2, test_index)
