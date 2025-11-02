

from random import randint as r_int

def generate_hsv_max_min_data():
    """Generate randomized HSV intervals and test pixels for pixel_constraint.

    Each key in the returned dictionary is a 6-element tuple representing
        the HSV min/max bounds:
            (hlow, hhigh, slow, shigh, vlow, vhigh)

        Each value is another dictionary mapping test pixels (h, s, v) to the
        expected output (1 if inside interval, 0 otherwise).

        Returns:
            Dict[Tuple[int, int, int, int, int, int],
            Dict[Tuple[int, int, int], int]]:
                A mapping from HSV intervals to their test pixels and expected
                  results.

    """
    data_dict = {}

    # Generates a random number of tests between 4 and 6
    for n in range(r_int(4, 7)):
        test_data = []

        for h_or_s_or_v in range(3):  # Iterate over H, S, and V components
            for min_max in range(2):  # Each component has a (min, max) pair
                # Ensure the max value is at least 2 greater than its min
                # and never exceeds 254 (to keep future test pixels valid)
                if min_max == 1:
                    last_index = len(test_data) - 1
                    last_number = test_data[last_index]
                    test_data.append(r_int(last_number + 2, 254))
                else:
                    # Ensure the min value isn't 0 and doesn't pass 252 (to
                    # keep future test pixels valid and leave a gap to max)
                    test_data.append(r_int(2, 252))

        data_results = {}

        # Generates three different tests
        for results in range(3):
            test_pixel = []

            for min_v, max_v in zip(test_data[::2], test_data[1::2]):
                # Valid pixel in interval
                if results == 0:
                    test_pixel.append(r_int(min_v + 1, max_v - 1))

                # Two invalid pixels in inteval, one above and another under.
                if results == 1:
                    test_pixel.append(r_int(0, min_v - 1))
                if results == 2:
                    test_pixel.append(r_int(max_v + 1, 255))

            # Expected results to each tested pixel.
            if results == 0:
                data_results[tuple(test_pixel)] = 1
            else:
                data_results[tuple(test_pixel)] = 0

        data_dict[tuple(test_data)] = data_results

    return data_dict
