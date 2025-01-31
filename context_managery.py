from contextlib import contextmanager
import io
import sys


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

## Prosta wersja:
# @contextmanager
# def collect_printouts():
#     mock_stdout = io.StringIO()
#     original_stdout = sys.stdout
#     sys.stdout = mock_stdout
#     yield
#     sys.stdout = original_stdout
#     mock_stdout.seek(0)
#     printouts = mock_stdout.read()  # wszystkie zebrane wydruki jako str trafiają do zmiennej printouts
#     print("Zebrane wydruki:", repr(printouts)) 


@contextmanager
def collect_printouts():
    mock_stdout = io.StringIO()
    original_stdout = sys.stdout

    def get_printouts():
        mock_stdout.seek(0)
        return mock_stdout.read()
    
    sys.stdout = mock_stdout
    try:
        yield get_printouts
    finally:
        sys.stdout = original_stdout


if __name__ == "__main__":
    with ctx_mgr2() as nazwa:
        print("Wewnątrz context mangera", nazwa)
        print(f"Poproszę o {2/0} piwa")
        print("i frytki")
    print("Dziękuję.")

    with collect_printouts() as get_printouts:
        print("test 1")
        print("test 2")
    printouts = get_printouts()
    print("Test zakończony. Wydruki:", repr(printouts))

