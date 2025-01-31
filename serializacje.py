from dataclasses import asdict, dataclass, fields
from numbers import Number
from typing import TypedDict

@dataclass
class ClimateData:
    temperature: Number
    humidity: Number

    def to_farenheit(self):
        return 43


def get_climate() -> ClimateData:
    temperature = 22.0
    humidity = 50.0

    return ClimateData(
        temperature=temperature,
        humidity=humidity,
    )  

if __name__ == "__main__":
    climate = get_climate()
    d = asdict(climate)
    print(ClimateData(**d))
