from lab5b2 import generator_from_image
from lab5b3 import combine_images


def test_basic():
    """Tests that weight==1 picks gen1 and all other weights pick gen2."""

    hsv_data = [(0, 0, 0), (0, 0, 1), (0, 0, 0), (0, 0, 1)]

    def mask_fn(pixel):
        # Returnera exakt 1 om V==1, annars 0
        return 1 if pixel[2] == 1 else 0

    img1 = [(10, 10, 10), (11, 11, 11), (12, 12, 12), (13, 13, 13)]
    img2 = [(20, 20, 20), (21, 21, 21), (22, 22, 22), (23, 23, 23)]
    gen1 = generator_from_image(img1)
    gen2 = generator_from_image(img2)

    out = combine_images(hsv_data, mask_fn, gen1, gen2)
    assert out == [
        (20, 20, 20),  # mask 0 -> gen2
        (11, 11, 11),  # mask 1 -> gen1
        (22, 22, 22),  # mask 0 -> gen2
        (13, 13, 13),  # mask 1 -> gen1
    ]


def test_empty_hsv_list():
    """Tests that an empty HSV list produces an empty output."""

    out = combine_images(
        [], lambda p: 1, lambda i: (0, 0, 0), lambda i: (1, 1, 1)
    )
    assert out == []


def test_gen1_shorter_gen2():
    """Tests behavior when the first image generator runs out of pixels."""

    # tre 1:or, sista 0
    hsv_list = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 0)]

    def mask_fn(pixel):
        return 1 if pixel[2] == 1 else 0

    img1 = [(1, 1, 1), (2, 2, 2)]  # kortare än maskens tre 1:or
    img2 = [(9, 9, 9), (8, 8, 8), (7, 7, 7), (6, 6, 6)]
    gen1 = generator_from_image(img1)
    gen2 = generator_from_image(img2)

    out = combine_images(hsv_list, mask_fn, gen1, gen2)
    # index 0 -> gen1[0], index 1 -> gen1[1],
    # index 2 -> gen1[2] (över från gränsen -> 0),
    # index 3 -> gen2[3]
    assert out[0] == (1, 1, 1)
    assert out[1] == (2, 2, 2)
    assert out[2] == 0  # över från gränsen från gen1 ger 0
    assert out[3] == (6, 6, 6)  # mask 0 -> gen2


def test_generators_longer_mask():
    """Tests that extra generator data is ignored when HSV list is shorter."""  

    hsv_pixels = [(0, 0, 0)]  # längd 1

    def mask_fn(_):
        return 0  # välj gen2

    gen1 = generator_from_image([(1, 1, 1), (1, 1, 2), (1, 1, 3)])
    gen2 = generator_from_image([(2, 2, 2), (2, 2, 3)])
    out = combine_images(hsv_pixels, mask_fn, gen1, gen2)
    assert out == [(2, 2, 2)]


def test_float():
    """Tests that weight 1.0 is treated the same as integer 1."""

    hsv_pixels = [(0, 0, 123)] * 3

    def mask_fn(_):
        return 1.0

    gen1 = generator_from_image([(3, 3, 3)] * 3)
    gen2 = generator_from_image([(9, 9, 9)] * 3)
    out = combine_images(hsv_pixels, mask_fn, gen1, gen2)
    assert out == [(3, 3, 3), (3, 3, 3), (3, 3, 3)]


def test_non1_weight():
    """Tests that all non-1 weights select the second image generator."""

    for w in (0, 0.5, 2, -1, None, "1"):
        hsv_list = [(0, 0, 0), (0, 0, 0)]

        def mask_fn(_w=w):
            return _w

        gen1 = generator_from_image([(1, 1, 1), (1, 1, 1)])
        gen2 = generator_from_image([(7, 7, 7), (8, 8, 8)])

        out = combine_images(hsv_list, mask_fn, gen1, gen2)
        assert out == [(7, 7, 7), (8, 8, 8)]


def test_hsv_list_err():
    """Tests that invalid HSV entries cause the combine function to raise."""

    hsv_list = ["bad-entry"]  # inte en tuple -> vår mask_fn kastar TypeError

    def mask_fn(pixel):
        # Försök indexera som HSV-tuple -> str är indexerbar men vi
        # tvingar TypeError:
        if not isinstance(pixel, tuple):
            raise TypeError("mask pixel must be tuple")
        return 0

    raised = False

    def gen_black(i):
        return (0, 0, 0)

    def gen_white(i):
        return (255, 255, 255)

    try:
        combine_images(hsv_list, mask_fn, gen_black, gen_white)
    except TypeError:
        raised = True
    assert raised is True


def test_none():
    """Tests that passing None as HSV list results in a TypeError."""

    raised = False

    def gen_black(i):
        return (0, 0, 0)

    def gen_white(i):
        return (255, 255, 255)

    try:
        combine_images(None, lambda p: 1, gen_black, gen_white)
    except TypeError:
        raised = True
    assert raised is True


def test_combine_images():
    """Runs all combine-image tests and reports pass/fail counts."""

    tests = [
        test_basic,
        test_empty_hsv_list,
        test_gen1_shorter_gen2,
        test_generators_longer_mask,
        test_float,
        test_non1_weight,
        test_hsv_list_err,
        test_none,
    ]

    passed = 0
    failed = 0
    failed_names = []

    for t in tests:
        try:
            t()
            passed += 1
        except AssertionError:
            failed += 1
            failed_names.append(t.__name__)
        except Exception as e:
            failed += 1
            failed_names.append(
                f"{t.__name__} (unexpected: {type(e).__name__}: {e})"
            )

    total = passed + failed
    print(
        f"combine_images Test: Ran {total} tests:"
        + f" {passed} passed, {failed} failed."
    )
    if failed_names:
        print("Failed:", ", ".join(failed_names))


if __name__ == "__main__":
    test_combine_images()
