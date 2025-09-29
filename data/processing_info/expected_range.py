"""
Dict of values for taxi data attributes
Many of these values chosen are conservative estimates that are on the fringe of
believability. Can be adjusted as seen fit as to not discount outliers.
"""

expected_ranges = {
    "trip_distance": {
        "min": 0.3,  # Proper trips useful for analysis unlikely to be this short
        "max": 200.0,  # Cap at 200 miles, anything above is likely false or leaves NYC
    },
    # We will remove (unknown) zone values, most of our analysis requires location
    # Impossible to impute with so many locations
    "PULocationID": {
        "min": 1,
        "max": 263,  # Number of TLC taxi zones w/o unknown
    },
    "DOLocationID": {"min": 1, "max": 263},
    # Remove negative fares and amounts
    # Not representative of the trips in which we seek to model
    "fare_amount": {"min": 0, "max": 10000.0},
    "total_amount": {
        "min": 0,  # Can be negative only in some voided trips
        "max": 10000.0,
    },
}
