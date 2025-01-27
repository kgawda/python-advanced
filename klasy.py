class Kura:
    jaja = 0

def kura_i_kurczak():
    kurczak = Kura()
    print(f"{kurczak.jaja = }")
    print(f"{vars(kurczak) = }")
    print(f"{vars(Kura) = }")

    print(">>> Kura.jaja = 1")
    Kura.jaja = 1
    print(f"{kurczak.jaja = }")
    print(f"{vars(kurczak) = }")
    print(f"{vars(Kura) = }")

    print(">>> kurczak.jaja = 2")
    kurczak.jaja = 2
    print(f"{kurczak.jaja = }")
    print(f"{vars(kurczak) = }")
    print(f"{vars(Kura) = }")

    print(">>> Kura.jaja = 3")
    Kura.jaja = 3
    print(f"{kurczak.jaja = }")
    print(f"{vars(kurczak) = }")
    print(f"{vars(Kura) = }")


class Test:
    def __getattribute__(self, name):
        return f"Atrybut {name}"

class Test2:
    def __getattribute__(self, name):
        print(f"Atrybut {name}")
        return self
    
class Test3:
    def __getattribute__(self, name):
        def f():
            print(name)
            return self
        return f

if __name__ == "__main__":
    obj = Test()
    print(obj.witaj)
    print(obj.milo_cie_widziec)

    obj = Test2()
    obj.hej.cześć.czołem

    obj = Test3()
    obj.hej().cześć().czołem()