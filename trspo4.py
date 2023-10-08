import itertools
import concurrent.futures

def collatz(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def calculate_collatz_numbers(N, num_threads):
    numbers = list(range(1, N + 1))

    def calculate_collatz_range(start, end):
        total_steps = 0
        for n in itertools.islice(numbers, start, end):
            total_steps += collatz(n)
        return total_steps

    chunk_size = N // num_threads
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(lambda chunk: calculate_collatz_range(*chunk), chunks))

    return sum(results)

def main():
    N = int(input("Введіть N: "))
    num_threads = int(input("Введіть кількість потоків: "))

    total_steps = calculate_collatz_numbers(N, num_threads)
    average_steps = total_steps / N
    print("Середня кількість кроків:", average_steps)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    end_time = time.time()
    print("Час виконання:", end_time - start_time)
