from main_task import main_task_solver
from task2 import task2_solver
from time import time

input_file_name = 'input.yml'
output_file_name = "test.tf"

sum1=0
sum2=0

for i in range(100):
    task1_start = time()
    main_task_solver(input_file_name, output_file_name)

    sum1 += time() - task1_start

for i in range(100):
    task2_start = time()
    task2_solver(input_file_name, output_file_name)

    sum2 += time() - task2_start

print("Стократная скорость выполнения для обязательного задания: " + str(sum1*100))
print("Стократная скорость выполнения для второго задания: " + str(sum2*100))