"""
Utility functions for preprocessing sdfs.
"""

import pyspark.sql.functions as F


def report_null(sdf, name):
    """
    Prints the number of missing values for each column in a sdf.
    """
    print(f"\n Results for {name}")
    overall_nulls = 0
    for col in sdf.columns:
        null_count = sdf.filter(sdf[col].isNull()).count()
        overall_nulls += null_count
        # Report null values
        if null_count > 0:
            print(f"{name}, {col}: {null_count:,} missing values")
    print(overall_nulls)


def is_expected(sdf, schema):
    """
    Checks for invalid values based on expected ranges/allowed values.
    Returns a dict of column:invalid count, as well as a column condition object
    representing the logical OR of all invalid value checks.
    """

    results = {}
    combined_cond = None

    for column, constraints in schema.items():
        cond = None
        if "min" in constraints:
            cond_min = F.col(column) < constraints["min"]
            cond = cond_min if cond is None else (cond | cond_min)
        if "max" in constraints:
            cond_max = F.col(column) > constraints["max"]
            cond = cond_max if cond is None else (cond | cond_max)
        if (
            "allowed_values" in constraints
            and constraints["allowed_values"] is not None
        ):
            cond_allowed = ~F.col(column).isin(constraints["allowed_values"])
            cond = cond_allowed if cond is None else (cond | cond_allowed)
        if cond is not None:
            combined_cond = cond if combined_cond is None else (combined_cond | cond)
            count = sdf.filter(cond).count()
            results[column] = count
            print(f"Column '{column}': {count:,} Invalid values found.")

    return results, combined_cond
