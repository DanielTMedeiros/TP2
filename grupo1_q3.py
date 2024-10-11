import concurrent.futures
from numba import njit

@njit
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return [n for n in range(start, end) if is_prime(n)]

def main():
    start = 10**6
    end = 10**6 + 5000
    num_workers = 4

    step = (end - start) // num_workers
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(num_workers)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(lambda r: find_primes(*r), ranges)

    all_primes = [prime for result in results for prime in result]
    print(f"Números primos encontrados: {len(all_primes)}")

if __name__ == "__main__":
    main()
