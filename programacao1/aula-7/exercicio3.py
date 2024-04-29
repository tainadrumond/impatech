import time
import math

start_time = time.time()
for i in range(1000000):
    2**0.5
end_time = time.time()
duration = end_time - start_time
print(f'Usando x**0.5: {duration}')


start_time = time.time()
for i in range(1000000):
    math.sqrt(2)
end_time = time.time()
duration = end_time - start_time
print(f'Usando math.sqrt(x): {duration}')