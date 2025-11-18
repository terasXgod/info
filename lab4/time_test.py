from main_task import main_task_solver
from task2 import task2_solver
from time import time

input_file_name = 'input.yml'
output_file_name = "test.tf"

task2_start = time()
task2_solver(input_file_name, output_file_name)
print("Скорость выполнения для второго задания: " + str(time() - task2_start))

task1_start = time()
main_task_solver(input_file_name, output_file_name)
print("Скорость выполнения для первого задания: " + str(time() - task1_start))
