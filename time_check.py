import time

current_time = time.time()



def speed_calc_decorator(time_passed):
    def show_time_elapsed():
        start_time = time.time()
        time_passed()
        end_time = time.time()
        time_check=end_time - start_time
        return time_check

    return show_time_elapsed


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i



@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i



first_run=fast_function()
second_run=slow_function()

#how much fast function is faster than slow one

print(f"{second_run-first_run} s")