import time

def time_log_execution(function):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {function.__name__}: {execution_time} seconds")
        return result
    return wrapper
@time_log_execution
def my_function():
    
    pass

my_function()  


#OUTPUT:-Execution time of my_function: 0.0 seconds
