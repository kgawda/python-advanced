import time
import functools

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
    @functools.wraps(f)
    def f_with_timing(*args, **kwargs):
        return time_it(f, *args, **kwargs)
    return f_with_timing


if __name__ == "__main__":
    timed_f = add_timing(testowa)
    x = timed_f()  # Tu następuje wykonanie "testowa" i wydruk ile to trwało
    print(f"Funkcja zwróciła {x}")  # np. 123

    @add_timing
    def testowa2():
        "Funkcja testowa"
        time.sleep(1)
        return 234
    
    print(f"Funkcja {testowa2.__qualname__} zwróciła {testowa2()}")
    print("Docstring funkcji testowej:", testowa2.__doc__)


"""
>>> @dekorator
... def add(a, b):
...  return a + b

### ... znaczy tyle samo co:

>>> def add(a, b):
...  return a + b
... 
>>> add = dekorator(add)

"""