# Mapping of roman numerals to equivalent decimal values.
# Includes each roman numeral and the subtractive value of one significant
# numeral smaller.
MAP = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)


def integer_to_roman(integer):
    result_numeral = ''

    # Iterate over the roman numberals from most to least significant digit.
    for numeral, decimal in MAP:
        # Add this digit to the `result_numeral` the number of times it may be
        # consumed. This is integer math, so the remainer of this division will
        # be the number of times this digit may be added to the number with the
        # remainder omitted.

        # Determine the number of times to repeat this digit.
        times = (integer / decimal)

        # Add this digit that many times to the result.
        result_numeral += numeral * times

        # Decrement our remaining count by the above value.
        integer -= (times * decimal)

    return result_numeral
