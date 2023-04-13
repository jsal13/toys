import re
from collections import defaultdict
from typing import Annotated

from pydantic import BaseModel, Field, ValidationError, validator


class UserData(BaseModel):
    """Represent a User's data."""

    id: int
    name: Annotated[str, Field(..., regex=r"[A-Za-z]+")]
    age: Annotated[int, Field(..., le=120, ge=10)]
    phone_number: str
    employed: bool = True

    # Classmethod: https://github.com/pydantic/pydantic/issues/1415
    @validator("phone_number")
    @classmethod
    def must_be_well_formatted(cls, val: str) -> str:
        """Validate that this is well-formatted."""
        if re.match(r"\(\d{3}\) \d{3}-\d{4}", val) is None:
            raise ValueError("Phone number must be well-formed.")
        return val


if __name__ == "__main__":
    # Create fake data with validation errors.
    names = ["Alice", "Bilbo", "Catherin3", "", "Dozer"]
    ages = [34, -100, 1000, 23, 24]
    phone_numbers = [
        "(732) 555-5555",
        "(732)555-5556",
        "(732) 555-5557",
        "(732) 555-5555",
        "7325555559",
    ]
    employed = [True, False, True, False, True]

    user_data = []
    errors: dict[int, list[ValidationError]] = defaultdict(list)
    for idx, name in enumerate(names):
        try:
            user_data.append(
                UserData(
                    id=idx,
                    name=name,
                    age=ages[idx],
                    phone_number=phone_numbers[idx],
                    employed=employed[idx],
                )
            )
        except ValidationError as e:
            errors[idx].append(e)

    print(user_data)
    print(errors)
