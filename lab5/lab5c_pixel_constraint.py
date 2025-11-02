from lab5b1 import pixel_constraint


def test_basic():
    # Testar pixel inom alla tre intervall -> 1, annars 0.
    is_in = pixel_constraint(10, 20, 30, 40, 50, 60)
    assert is_in((15, 35, 55)) == 1
    assert is_in((9, 35, 55)) == 0  # H under min
    assert is_in((21, 35, 55)) == 0  # H över max
    assert is_in((15, 29, 55)) == 0  # S under min
    assert is_in((15, 41, 55)) == 0  # S över max
    assert is_in((15, 35, 49)) == 0  # V under min
    assert is_in((15, 35, 61)) == 0  # V över max


def test_limits():
    # Testar och bekräftar att gränserna är inkluderande (>= och <=).
    is_in = pixel_constraint(10, 20, 30, 40, 50, 60)
    assert is_in((10, 30, 50)) == 1  # vänstergränser
    assert is_in((20, 40, 60)) == 1  # högergränser
    assert is_in((11, 30, 50)) == 1
    assert is_in((19, 40, 60)) == 1


def test_extrema_hsv():
    #  - HSV values behandlas från 0 till 255. Testa 0 och 255.
    #  - Negativa värden och >255 ska ge 0 (utanför intervall).
    is_in = pixel_constraint(0, 255, 0, 255, 0, 255)
    assert is_in((0, 0, 0)) == 1
    assert is_in((255, 255, 255)) == 1
    assert is_in((-1, 100, 100)) == 0
    assert is_in((100, 100, 300)) == 0


def test_tuple_error():
    #  Testa att Felaktig input (fel tuple-längd) ska leda till ValueError,
    #  eftersom funktionen packar upp (h, s, v) ur pixel.
    is_in = pixel_constraint(0, 255, 0, 255, 0, 255)
    raised = False
    try:
        is_in((10, 20))  # endast 2 element
    except ValueError:
        raised = True
    assert raised is True


def test_type_value_error():
    #  Testar Felaktig typ (t.ex. None eller str) bör orsaka
    #  TypeError eller ValueError vid jämförelser.
    is_in = pixel_constraint(0, 10, 0, 10, 0, 10)

    def expect_type_error(pixel):
        raised = False
        try:
            is_in(pixel)
        except (TypeError, ValueError):
            raised = True
        return raised

    assert expect_type_error(None) is True
    assert expect_type_error("not-a-tuple") is True  # ValueError
    assert (
        expect_type_error((1, "x", 3)) is True
    )  # str jämförs mot int -> TypeError


def test_float_values():
    #   TEstar om float ges in (t.ex. efter beräkningar),
    #   jämförelsen fungerar i Python.
    is_in = pixel_constraint(0, 10, 0, 10, 0, 10)
    assert is_in((5.0, 10.0, 0.0)) == 1
    assert is_in((10.1, 5.0, 5.0)) == 0  # utanför H


def test_pixel_constraint():
    tests = [
        test_basic,
        test_limits,
        test_extrema_hsv,
        test_tuple_error,
        test_type_value_error,
        test_float_values,
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
            # Ovän­tade fel räknas som fail och skrivs ut för diagnos.
            failed += 1
            failed_names.append(
                f"{t.__name__} (unexpected: {type(e).__name__}: {e})"
            )

    total = passed + failed
    print(
        f"pixel_constraint Test: Ran {total} tests: "+
        f"{passed} passed, {failed} failed."
    )
    if failed_names:
        print("Failed:", ", ".join(failed_names))


if __name__ == "__main__":
    test_pixel_constraint()
