import string

import great_expectations as gx
import numpy as np
import pandas as pd

# The data context will allow us to access a bunch of utility and
# convenience methods; it's the entry point for GX in the Py API.
context = gx.get_context()

# Let's make some synthetic data for use in GX.

def create_random_records(n: int, missing_data_percent: float = 0.1) -> pd.DataFrame:
    """Create random records."""
    # We purposely put some malformed data in here.
    field_ints = np.random.randint(-100, 100, size=n)
    field_nonneg_int = np.random.randint(-10, 100, size=n)
    field_required_int = np.random.randint(-100, 100, size=n)
    field_float = np.random.rand(n)
    field_str = np.random.choice(list(string.ascii_lowercase), size=n, replace=True)

    fields = {
        "field_int": field_ints,
        "field_nonneg_int": field_nonneg_int,
        "field_required_int": field_required_int,
        "field_float": field_float,
        "field_str": field_str,
    }

    _df = pd.DataFrame(fields)

    # Create random nulls.
    _df = _df.mask(
        np.random.choice(
            [True, False],
            size=df.shape,
            p=[missing_data_percent, 1 - missing_data_percent],
        )
    )

    return _df

df = create_random_records(100)

# Create a validator for reading a dataframe.
# A validator stores Expectations about data it's
# associated with, and performing introspections on the data.

validator = context.sources.pandas_default.read_dataframe(df)

# Let's do a checkpoint, this allows us to repeat validation.

checkpoint = gx.checkpoint.SimpleCheckpoint(
    name="quickstart_checkpoint",
    data_context=context,
    validator=validator
)

# Run the checkpoint.
checkpoint_result = checkpoint.run()

# Gx compiles this stuff into a nice little data doc and opens a webpage.
context.build_data_docs()
