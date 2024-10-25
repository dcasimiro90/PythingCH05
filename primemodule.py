def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to print all prime numbers less than n
def print_primes(n):
    for num in range(2, n):
        if is_prime(num):
            print(num, end=" ")
    print()

# Function to return a list of all prime numbers less than n
def get_primes(n):
    return [num for num in range(2, n) if is_prime(num)]