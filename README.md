# ClionHomeworkTemplate

## How to use this template

1. Download or clone to your computer
2. Open the folder using clion and choose use the existing project if promoted.
3. Complete the code in the source files for homework 0 and 1.
4. Write your information in the students.txt file
5. On the right hand choose the HomeworkTest build configuration and run. 
   
   This should build and run the tests on your code. 
   It will also create a folder `for_gr++` which should contain the zips for homework 0 and 1.

## How to add a new homework question and tests

1. Create a source file by the name of `hw{}q{}.c` where after `hw` comes the homework number and after `q` comes the question number

2. Add to the `CMakeLists.txt` a call to create a target for this question. 

    For example to create the targets for homework 1 question 2 this is how it looks:
    ```
    create_homework_target(1 2)
    ```
   
 3. Add to the `CMakeLists.txt` a call to create a target for creation of the zip. 
    The zip will contain source files for that specific homework and the students.txt file
 
    For example to create the target for homework 1 this is how it looks:
    ```
    create_zip_target(1)
    ```

4. Put you input/output test files in `HomeworkTest/homework_resources`.
   They should be in the format `hw{}q{}in{}` for input and `hw{}q{}out{}` for output

5. In `HomeworkTest/test_homework.py` Copy one of the test methods and change the homework and question number. 
   You should also write how many different input/output files exist to test with using the `test_index` parameter.
   
    For example to create the target for homework 3 question 2 that has 9 different input/output combos this is how it looks:
    ```python
    # Test homework number 3 question number 2 with 9 different input/output combos
    @pytest.mark.parametrize("test_index", range(9))
    def test_hw3q2(run_homework_and_assert, test_index):
        run_homework_and_assert(3, 2, test_index)
    ```

5
