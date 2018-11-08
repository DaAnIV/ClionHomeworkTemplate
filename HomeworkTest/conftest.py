import os
import py
import pytest
import subprocess


def pytest_addoption(parser):
    parser.addoption(
        "--print-actual-output", action="store_true", default=False, help="Prints the binary's output"
    )
    parser.addoption(
        "--print-expected-output", action="store_true", default=False, help="Prints the expected output"
    )


@pytest.fixture(scope="session")
def print_expected_output(request):
    return request.config.getoption("--print-expected-output")


@pytest.fixture(scope="session")
def print_actual_output(request):
    return request.config.getoption("--print-actual-output")


@pytest.fixture(scope="session")
def run_homework_and_assert(print_actual_output, print_expected_output, get_input_output, get_question_binary,
                            homework_runner):
    def __func(homework, question, input_output_index):
        input_data, expected_output = get_input_output(homework, question, input_output_index)
        actual_output = homework_runner(get_question_binary(homework, question), input_data)

        full_question_name = get_full_question_name(homework, question)
        if print_actual_output:
            print('{} actual output:'.format(full_question_name))
            log_to_bytes_console(actual_output)
        if print_expected_output:
            print('{} expected output:'.format(full_question_name))
            log_to_bytes_console(expected_output)

        assert actual_output == expected_output

    return __func


def log_to_bytes_console(str_bytes):
    print(str_bytes.decode('utf-8').replace('\r\n', '\n'))


@pytest.fixture(scope="session")
def homework_runner(request):
    def __runner(executable, input_content=''):
        process = subprocess.Popen([executable], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        out, err = process.communicate(input=input_content)
        return out

    return __runner


@pytest.fixture(scope="session")
def get_question_binary(request, build_dir):
    return lambda h, q: build_dir.join('{}.exe'.format(get_full_question_name(h, q))).strpath
    

@pytest.fixture(scope="session")
def build_dir(request):
    return py.path.local(os.getenv("BUILD_DIR"))
    
    
@pytest.fixture(scope="session")
def get_input_output(request, data_dir):
    def __getter(homework, question, index):
        full_question_name = get_full_question_name(homework, question)
        out_path = data_dir.join('{}out{}.txt'.format(full_question_name, index))
        in_path = data_dir.join('{}in{}.txt'.format(full_question_name, index))

        in_data = ""
        out_data = ""
        if in_path.exists():
            in_data = in_path.read(mode='rb')
        if out_path.exists():
            out_data = out_path.read(mode='rb')

        return in_data, out_data

    return __getter


def get_full_question_name(homework, question):
    return 'hw{}q{}'.format(homework, question)


@pytest.fixture(scope="session")
def data_dir():
    return py.path.local(os.getenv("DATA_DIR"))
