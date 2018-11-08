cmake_minimum_required(VERSION 3.12)
project(ClionHomework)

set(CMAKE_C_FLAGS "-std=c99 ${CMAKE_C_FLAGS}")
set(CMAKE_CXX_STANDARD 14)

function(create_zip output_file input_files working_dir)
    add_custom_command(
            COMMAND ${CMAKE_COMMAND} -E tar "cf" "${output_file}" --format=zip -- ${input_files}
            WORKING_DIRECTORY "${working_dir}"
            OUTPUT  "${output_file}"
            DEPENDS ${input_files}
            COMMENT "Zipping to ${output_file}."
    )
endfunction()

set(STUDENTS_FILE students.txt)

function(create_zip_target homework)
    set(out_zip_dir for_gr++)
    set(out_zip ${out_zip_dir}/hw${homework}.zip)
    file(GLOB in_source_files "${CMAKE_CURRENT_SOURCE_DIR}/hw${homework}q*.c")
    set(input_files ${in_source_files} ${STUDENTS_FILE})

    file(MAKE_DIRECTORY ${out_zip_dir})

    add_custom_command(
            COMMAND ${CMAKE_COMMAND} -E tar "cf" "${out_zip}" --format=zip -- ${input_files}
            WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
            OUTPUT  "${out_zip}"
            DEPENDS ${input_files}
            COMMENT "Zipping to ${out_zip}."
    )
    add_custom_target(
            zip_hw${homework} ALL
            DEPENDS ${out_zip}
    )
endfunction()

function(create_homework_target homework question)
    set(name hw${homework}q${question})
    add_executable(${name} ${name}.c)
endfunction()

# Homework 0
create_homework_target(0 1)
create_zip_target(0)

# Homework 1
create_homework_target(1 1)
create_homework_target(1 2)
create_zip_target(1)