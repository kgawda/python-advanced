
from contextlib import contextmanager

@contextmanager
def ctx_mgr():
    print("Początek context mangera")
    yield "Hello!"
    print("Koniec context managera")

@contextmanager
def ctx_mgr2():
    # tu otwarcie jakiegoś zasobu
    try:
        yield "Hello!"
    except ZeroDivisionError as e:
        pass
    # finally:
    #   tu zamknięcie zasobu 

if __name__ == "__main__":
    with ctx_mgr2() as nazwa:
        print("Wewnątrz context mangera", nazwa)
        print(f"Poproszę o {2/0} piwa")
        print("i frytki")
    print("Dziękuję.")