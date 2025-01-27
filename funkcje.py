import time

def testowa():
    time.sleep(1)
    return 123

def time_it(f, *args, **kwargs):
    t0 = time.perf_counter()
    reusutl = f(*args, **kwargs)
    t1 = time.perf_counter()
    print(f"Wywołanie {f.__name__} zajęło {t1 - t0:.2f} s")
    return reusutl

def add_timing(f):
    def f_with_timing(*args, **kwargs):
        return time_it(f, *args, **kwargs)
    return f_with_timing


if __name__ == "__main__":
    timed_f = add_timing(testowa)
    x = timed_f()  # Tu następuje wykonanie "testowa" i wydruk ile to trwało
    print(f"Funkcja zwróciła {x}")  # np. 123
