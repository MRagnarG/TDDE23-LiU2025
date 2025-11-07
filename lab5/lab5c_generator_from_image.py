# Testar generator_from_image
from lab5b2 import generator_from_image


def test_basic():
    """Tests that valid indices return the corresponding pixels."""

    img = [(1, 2, 3), (4, 5, 6)]
    gen = generator_from_image(img)
    assert gen(0) == (1, 2, 3)
    assert gen(1) == (4, 5, 6)


def test_limits():
    """Tests that indices beyond the image length return 0."""

    img = [(10, 20, 30)]
    gen = generator_from_image(img)
    assert gen(1) == 0
    assert gen(100) == 0


def test_negative():
    """Tests that negative indices access pixels from the end."""

    img = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
    gen = generator_from_image(img)
    assert gen(-1) == (3, 3, 3)
    assert gen(-2) == (2, 2, 2)


def test_empty_list():
    """Tests behavior when the underlying image list is empty."""

    img = []
    gen = generator_from_image(img)
    assert gen(0) == 0
    assert gen(5) == 0
    # Negativa index på tom lista ger IndexError;
    # men funktionen gör liståtkomst direkt
    raised = False
    try:
        _ = gen(-1)  # detta försöker img[-1] och bör ge IndexError
    except IndexError:
        raised = True
    assert raised is True


def test_mutation_visibility():
    """Tests that the generator sees mutations to the underlying list."""

    img = [(0, 0, 0)]
    gen = generator_from_image(img)
    assert gen(0) == (0, 0, 0)
    # Ändra underliggande data:
    img[0] = (9, 9, 9)
    assert gen(0) == (9, 9, 9)


def test_type_handling():
    """Tests that non-integer indices lead to a type-related error."""

    img = [(7, 7, 7)]
    gen = generator_from_image(img)

    def expect_type_or_value_error(idx):
        ok = False
        try:
            gen(idx)
        except (TypeError, ValueError):
            ok = True
        return ok

    assert expect_type_or_value_error(0.5) is True
    assert expect_type_or_value_error("0") is True


def test_generator_from_image():
    """Runs all generator tests and reports pass/fail counts."""

    tests = [
        test_basic,
        test_limits,
        test_negative,
        test_empty_list,
        test_mutation_visibility,
        test_type_handling,
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
            failed_names.append(f"{t.__name__}" + 
                        f" (unexpected: {type(e).__name__}: {e})")

    total = passed + failed
    print(f"generator_from_image Test: Ran {total} tests:" +
          f" {passed} passed, {failed} failed.")
    if failed_names:
        print("Failed:", ", ".join(failed_names))
    
    pass


