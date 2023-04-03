import json
import random
from datetime import datetime, timedelta
from enum import Enum, auto

import numpy as np
from pydantic import Field
from pydantic.dataclasses import dataclass

NUM_SENSORS = 10


class Power(Enum):
    """Enum for ``Power`` field in ``Signal``."""

    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()


@dataclass
class Signal:
    """
    Single ``Signal`` for use in a data stream.

    ``heat_index`` is the target variable for any ML/DS kind of stuff.
    0 <= heat_index <= 1.

    Note: We cannot constrain the datetime to a certain type because of the following:
    https://github.com/pydantic/pydantic/issues/156
    """

    sensor_id: int
    value_1: int
    value_2: float
    value_3: float
    power: Power
    heat_index: float
    dt: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_json(self) -> str:
        """Convert dataclass values to json."""
        # Remove "__pydantic_initialized__" from the dict.
        values = self.__dict__.copy()
        del values["__pydantic_initialised__"]

        return json.dumps(values, default=lambda x: x.name)

    def to_csv(self) -> str:
        """Convert dataclass values to csv."""
        # Remove "__pydantic_initialized__" from the dict.
        values = self.__dict__.copy()
        del values["__pydantic_initialised__"]

        return (
            f"{self.sensor_id},{self.value_1},{self.value_2},{self.value_3},"
            + f"{self.power},{self.heat_index},{self.dt}"
        )


def generate_signal() -> Signal:
    """Generate a single signal."""

    def _create_signal_target_variable(
        value_1: int, value_2: float, value_3: float, power: Power
    ) -> float:
        """Create an example target variable for signal given the other values."""
        epsilon = np.random.normal(0, 0.05)

        if (value_1 < 0) and (value_2 < 0) and (power in [Power.LOW]):
            return np.clip(epsilon, 0.0, 1.0)

        if (value_1 > 10) and (value_2 > 1.96) and (power == Power.HIGH):
            return np.clip(1 - epsilon, 0.0, 1.0)

        sigmoid = 1 / (1 + np.exp(-(value_2**3 + value_3)))
        if power == Power.LOW:
            sigmoid *= 0.25
        elif power == power.MEDIUM:
            sigmoid *= 0.75

        return round(np.clip(sigmoid, 0.0, 1.0), 4)

    value_1 = random.randint(-20, 20)
    value_2 = round(np.random.normal(), 4)
    value_3 = round(np.random.normal(), 4)
    power = random.choice([Power.LOW, Power.MEDIUM, Power.HIGH])
    dt = (datetime.now() + timedelta(seconds=random.randint(-10, 10))).strftime(
        ("%Y-%m-%d %H:%M:%S")
    )

    heat_index = _create_signal_target_variable(
        value_1=value_1, value_2=value_2, value_3=value_3, power=power
    )

    return Signal(
        sensor_id=np.random.randint(1, NUM_SENSORS),
        value_1=value_1,
        value_2=value_2,
        value_3=value_3,
        power=power,
        heat_index=heat_index,
        dt=dt,
    )


if __name__ == "__main__":
    # while True:
    #     time.sleep(2)
    #     # print(generate_signal().to_json())
    #     # Do something with this!

    with open("./data.csv", "w+", encoding="utf-8") as f:
        f.write("sensor_id,value_1,value_2,value_3,power,heat_index,dt\n")
        f.write("\n".join(generate_signal().to_csv() for i in range(10000)))
