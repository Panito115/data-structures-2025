from memory_profiler import profile

class Car:
    def __init__(self, model: str, kms: int):
        self.model = model
        self.kms = kms

    def __repr__(self):
        return f'Modelo: {self.model} | KM: {self.kms}'

    def broom(self, distance: int):
        self.kms += distance

@profile
def test_cars():
    daily = Car('Porsche 911', 0)
    print(daily)
    daily.broom(50)
    print(daily)

    daily = Car('Toyota Rav4', 0)
    print(daily)
    daily.broom(1000)
    print(daily)

    daily = Car('Mercedez AMG', 100)
    print(daily)
    daily.broom(2200)
    print(daily)

if __name__ == "__main__":
    test_cars()
