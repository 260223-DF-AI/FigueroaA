from functools import wraps, lru_cache
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        return total_time
    return wrapper
    

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}(", end="")
        for index, param in enumerate(args):
            print(f"{param}", end="")
            if index < len(args) - 1:
                print(", ", end="")
        print(")")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
    
def retry(max_attempts=3, delay=1, exceptions=(Exception,)):

    if max_attempts < 1:
        raise ValueError("attempts must be greater than 1")
    if delay < 0:
        raise ValueError("delay time must be a positive number")
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            attempts = max_attempts
            while (attempts > 0):
                try:
                    func(*args, **kwargs)
                except exceptions as e:
                    print(e)

                attempts -= 1
                time.sleep(delay)
            return wrapper

def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    def cache_decorator(func):
        def wrapper(*args, **kwargs):
            cached_func = lru_cache(maxsize=max_size)(func())
            cached_func(*args, **kwargs)
            print(cached_func.cache_info())
            print(cached_func.cache_clear())

            return wrapper
    