def generator_from_image(img):

    if not isinstance(img, (list, tuple)):
        raise TypeError("img must be a list or tuple of pixels")

    def pixel_color(index):
        # Typkontroll
        if not isinstance(index, int):
            raise TypeError("index must be an int")

        # Övre gräns (>= len) -> IndexError
        if index >= len(img):
            raise IndexError("index out of range")

        return img[index]

    return pixel_color


# nya tester --------------------------------------


def test_index_error():
    """Testar generator_from_image funktionen. Testar inre funktionen
    pixel_color, där man förväntar sig ett gilltig index value, men här
    testar vi med ogilltiga int tal för index.
    """
    img = [(1, 2, 3)]
    gen = generator_from_image(img)
    # index == len(img) -> IndexError
    try:
        gen(1)
        assert False, "Expected IndexError but none was raised"
    except IndexError:
        pass


def test_index_type_error():
    """Testar generator_from_image funktionen. Testar inre funktionen
    pixel_color, där man förväntar sig ett gilltig index (int), men här
    testar vi med ogilltiga index typer.
    """
    img = [(1, 2, 3)]
    gen = generator_from_image(img)
    for bad in (0.5, "1", None):
        try:
            gen(bad)
            assert False, "Expected TypeError but none was raised"
        except TypeError:
            pass


def test_neg_index():
    """Testar generator_from_image funktionen. Testar inre funktionen
    pixel_color, där man förväntar sig att negativa index ska returnera
    rätt (baklänges) pixel från listan.
    """
    img = [(1, 1, 1), (2, 2, 2)]
    gen = generator_from_image(img)
    assert gen(-1) == (2, 2, 2)


def run_all():
    """Testar generator_from_image funktionen med alla tidigare test
     funktioner:
    test_index_error, test_index_type_error och test_neg_index.
    Skappar även en rapport av testning, där det visar antalet tester,
    antalet godkända tester och antalet (och vilken) icke godkända tester.
    """
    tests = [
        test_index_error,
        test_index_type_error,
        test_neg_index,
    ]
    p = f = 0  # p = passed ; f = failed
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
    print(
        f"generator_from_image Test: Ran {p + f} tests: {p} passed, {f} failed."
    )
    if names:
        print("Failed:", ", ".join(names))


if __name__ == "__main__":
    run_all()
