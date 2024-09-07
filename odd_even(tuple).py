import random

tuple_size = 15
random_tuple = tuple(random.randint(1, 100) for _ in range(tuple_size))
even_count = sum(1 for num in random_tuple if num % 2 == 0)
odd_count = tuple_size - even_count

print(f'The generated tuple is: {random_tuple}')
print(f'The count of even numbers is: {even_count}')
print(f'The count of odd numbers is: {odd_count}')
