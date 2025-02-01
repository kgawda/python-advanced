# Dzień 1

## wraps()
Napisać własną implementację functools.wraps (wystarczy, że będzie kopiować `__qualname__` i `__doc__`)

## Context Manger łapiący wydruki
Napisać context manager pozwalający na testowanie wydruków w danym bloku kodu
Wydruki (np. print) w ramach testowanego kodu mają być zbierane (zamiast wyrzucane na ekran) i drukowane na koniec, w podsumowaniu.

Przykładowe użycie:
```python
with collect_printouts():
    print("test 1")
    print("test 2")
print("Test zakończony")
```

Wydruk powinien wyglądać mniej więcej tak:
```
Zebrane wydruki: "test 1\ntest2\n"
Test zakończony
```


A jak łapać wydruki? Bez Context Mnagera wyglądało by to tak:
```python
import io
import sys

mock_stdout = io.StringIO()
sys.stdout = mock_stdout  # [1]
# od tego momentu wszystkie wydruki z print() trafią do mock_stdout zamianst na ekran
# ... tu testowany kod ...
mock_stdout.seek(0)
printouts = mock_stdout.read()  # wszystkie zebrane wydruki jako str trafiają do zmiennej printouts
print("Zebrane wydruki:", repr(printouts))  # [2]
```

Zagadka: Dlaczego print z linii [2] się nie drukuje? Żeby rozwiązać ten problem trzeba "zapamiętać" gdzieś oryginalną wartość sys.stdout (okolice linijki [1]), a potem ją przywrócić.


## Przypomnieć sobie virtualenvs (venv)



# Dzień 2/3

## Cz. 1: Przerobić Position na dataclass
Sprawdzić czy wtedy można usunąć dotychczasową implementację `__eq__`.

Dokumentacja: <https://docs.python.org/3/library/dataclasses.html>

## Cz. 3:
Spróbować użyć dla Position `@dataclass(slots=True)` i czy da się użyć w tym przypadku.
Sprawdzić czy wpływnęło to na użycie pamięci przez program.

## Cz. 2: 
Sprawdzić co znaczy `@dataclass(frozen=True)` (może być razem z `slots=True`) i czy da się użyć na Position. (Hint: jeśli zmieniamy zawartosć `.x` i `.y` poza `__init__`, to raczej nie zadziała).
Jeśli zmiana była możliwa: sprawdzić wpływ na czas działania programu.
