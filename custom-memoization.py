fibonacci_cache = {}

def fibonacci_memo(num):
    if num in fibonacci_cache:
        return fibonacci_cache[num]

    if num == 1:
        value = 1
    elif num == 2:
        value = 1
    elif num > 2:
        value = (fibonacci_memo(num - 1) + fibonacci_memo(num - 2))

    fibonacci_cache[num] = value
    return value

for i in range(1, 201):
    print(fibonacci_memo(i))