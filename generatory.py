class Inventory:
    def __init__(self, products):
        self.products = products

    def __iter__(self):
        return InventoryIterator(self)


class InventoryIterator:
    def __init__(self, inventory):
        self.inventory = inventory
        self.iteration_count = 0

    def __next__(self):
        try:
            result = self.inventory.products[self.iteration_count]
        except IndexError:
            raise StopIteration()
        self.iteration_count += 1
        return result
    
    def __iter__(self):
        return self


if __name__ == "__main__":
    a = Inventory(["masło", "chleb", "ser"])
    for x in a:
        for y in a:
            print(x, y)

    
