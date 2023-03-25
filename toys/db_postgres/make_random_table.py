from datetime import timedelta, date
from typing import Any

import numpy as np

CREATE_TABLE_QUERY = """
CREATE TABLE sensors (
    id          serial PRIMARY KEY,
    sensor_id   integer NOT NULL,
    dt          date,
    value1      integer,
    value2      float,
    value3      float,
    value4      varchar(5)
);
"""

INSERT_QUERY = """
INSERT INTO sensors (sensor_id, dt, value1, value2, value3, value4) VALUES
"""


def generate_random_sensor_reading(
    num_sensors: int, num_readings: int
) -> list[tuple[Any, ...]]:
    """Generate random SensorReading."""

    sensor_ids = np.array([], dtype=np.int64)
    date_val = np.array([])
    value1 = np.array([], dtype=np.int64)
    value2 = np.array([])
    value3 = np.array([])
    value4 = np.array([])

    for sensor_id in range(1, num_sensors + 1):
        sensor_ids = np.concatenate(
            [sensor_ids, np.ones(num_readings).astype(np.int64) * sensor_id]
        )
        date_val = np.concatenate(
            [
                date_val,
                [
                    (date.today() + timedelta(days=n)).isoformat()
                    for n in range(num_readings)
                ],
            ]
        )
        value1 = np.concatenate([value1, np.random.randint(-10, 10, size=num_readings)])
        value2 = np.concatenate([value2, np.random.random(num_readings)])
        value3 = np.concatenate([value3, np.random.normal(0, 1, num_readings)])
        value4 = np.concatenate(
            [
                value4,
                np.random.choice(["LOW", "MED", "HIGH"], size=num_readings, replace=True),
            ]
        )

    vals = list(
        zip(
            sensor_ids.tolist(),
            date_val.tolist(),
            value1.tolist(),
            value2.tolist(),
            value3.tolist(),
            value4.tolist(),
        )
    )

    return vals


if __name__ == "__main__":
    readings = generate_random_sensor_reading(num_sensors=5, num_readings=50)

    INSERT_LINES = ",\n".join(
        [
            (
                f"({int(float(row[0]))}, '{row[1]}', "
                f"{int(float(row[2]))}, {row[3]}, {row[4]}, '{row[5]}')"
            )
            for row in readings
        ]
    )

    with open("./init.sql", "w+", encoding="utf-8") as f:
        f.write(CREATE_TABLE_QUERY)
        f.write(INSERT_QUERY + INSERT_LINES + ";")
