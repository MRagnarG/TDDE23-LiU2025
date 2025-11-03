def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    def is_in_interval(pixel):
        # Grundläggande validering
        if not isinstance(pixel, (tuple, list)):
            raise TypeError("pixel must be a tuple or list")
        if len(pixel) != 3:
            raise ValueError("pixel must have exactly 3 components (H,S,V)")

        h, s, v = pixel

        # Komponenttyper
        for comp in (h, s, v):
            if not isinstance(comp, (int, float)):
                raise TypeError("pixel components must be numeric")

        return (
            1
            if (
                hlow <= h <= hhigh
                and slow <= s <= shigh
                and vlow <= v <= vhigh
            )
            else 0
        )

    return is_in_interval


# Nya tester -----------------------------------------


def test_not_tuple():
    """Testar pixel_constraint funktionen med fel inmätning i inre funktionen
    is_in_interval, där inmätning borde vara en tupel."""
    is_in = pixel_constraint(0, 255, 0, 255, 0, 255)
    for wrong in (None, "str", 123):
        raised = False
        try:
            is_in(wrong)
        except TypeError:
            raised = True
        assert raised is True


def test_len_error():
    """Testar pixel_constraint funktionen med fel inmätning i inre funktionen
    is_in_interval, där inmätning borde vara en tupel med tre tal."""
    is_in = pixel_constraint(0, 255, 0, 255, 0, 255)
    for bad in ((), (1,), (1, 2), (1, 2, 3, 4)):
        raised = False
        try:
            is_in(bad)
        except ValueError:
            raised = True
        assert raised is True


def test_not_num():
    """Testar pixel_constraint funktionen med fel inmätning i inre funktionen
    is_in_interval, där alla element i tupel borde vara (int/float)"""
    is_in = pixel_constraint(0, 255, 0, 255, 0, 255)
    for bad in (("a", 1, 2), (1, "b", 2), (1, 2, object())):
        raised = False
        try:
            is_in(bad)
        except TypeError:
            raised = True
        assert raised is True


def run_all():
    """Testar pixel_constraint funktionen med alla tidigare test funktioner:
    test_not_tuple, test_len_error och test_not_num.
    Skappar även en rapport av testning, där det visar antalet tester,
    antalet godkända tester och antalet (och vilken) icke godkända tester.
    """
    tests = [
        test_not_tuple,
        test_len_error,
        test_not_num,
    ]
    p = f = 0  # p = passed; f = failed
    names = []
    for t in tests:
        try:
            t()
            p += 1
        except AssertionError:
            f += 1
            names.append(t.__name__)
        except Exception as e:
            f += 1
            names.append(f"{t.__name__} (unexpected: {type(e).__name__}: {e})")
    print(f"pixel_constraint Test: Ran {p + f} tests: {p} passed, {f} failed.")
    if names:
        print("Failed:", ", ".join(names))


if __name__ == "__main__":
    run_all()
