from lab5c2_generator import generator_from_image


def combine_images(list_hsv_pixels, mask_function, gen1, gen2):

    if not isinstance(list_hsv_pixels, (list, tuple)):
        raise TypeError("list_hsv_pixels must be a list or tuple")
    if not callable(mask_function):
        raise TypeError("mask_function must be callable")
    if not callable(gen1) or not callable(gen2):
        raise TypeError("gen1 and gen2 must be callable")

    comb_img = []
    for index in range(len(list_hsv_pixels)):
        try:
            weight = mask_function(list_hsv_pixels[index])
            if weight == 1:
                pixel = gen1(index)
            else:
                pixel = gen2(index)
            comb_img.append(pixel)
        except Exception as e:
            raise RuntimeError(f"combine_images failed at index {index}: {e}")

    return comb_img


# Nya tester ----------------------------------------------
def test_mask_err():
    """Testar combine_images funktionen, om den kastar RuntimeError
      när mask_function misslyckas på någon anledning.

    Säkerställer också att det ursprungliga felet (ValueError) bevaras
      som orsak.
    """
    hsv_pixels = [(0, 0, 0)]

    def bad_mask(pixel):
        raise ValueError("mask failure")

    raised = False
    try:
        combine_images(
            hsv_pixels, bad_mask, lambda i: (0, 0, 0), lambda i: (1, 1, 1)
        )
    except RuntimeError as e:
        # Säkerställer att det ursprungliga felet sparas som orsak
        #  till RuntimeError
        assert isinstance(e.__cause__, ValueError)
        raised = True
    assert raised is True


def test_gen_err():
    """Testar att combine_images funktionen kastar RuntimeError när en av
      generatorfunktion (gen1 eller gen2) misslyckas, till exempel vid
      IndexError.

    Kontrollerar även att det ursprungliga felet bevaras.
    """
    hsv_pixels = [(0, 0, 0), (0, 0, 0)]

    def mask1(pixel):
        return 1  # väljer gen1

    gen1 = generator_from_image(
        [(10, 10, 10)]
    )  # längd 1 -> index 1 ger IndexError
    gen2 = generator_from_image([(20, 20, 20), (21, 21, 21)])
    raised = False
    try:
        combine_images(hsv_pixels, mask1, gen1, gen2)
    except RuntimeError as e:
        assert isinstance(e.__cause__, IndexError)
        raised = True
    assert raised is True


def test_ok():
    """
    Testar att combine_images funktionen fungerar som vanligt i ett normallt
    inmätning.

    Verifierar att rätt generator väljs beroende på mask_function och
    att resultatet innehåller rätt förväntade pixlar.
    """
    hsv_pixels = [(0, 0, 1), (0, 0, 0)]

    def mask(pixel):
        return 1 if pixel[2] == 1 else 0

    gen1 = generator_from_image([(1, 1, 1), (2, 2, 2)])
    gen2 = generator_from_image([(9, 9, 9), (8, 8, 8)])
    out = combine_images(hsv_pixels, mask, gen1, gen2)
    assert out == [(1, 1, 1), (8, 8, 8)]


def run_all():
    """Testar combine_images funktionen med alla tidigare test funktioner:
    test_mask_err, test_gen_err och test_ok.
    Skappar även en rapport av testning, där det visar antalet tester,
    antalet godkända tester och antalet (och vilken) icke godkända tester.
    """
    tests = [
        test_mask_err,
        test_gen_err,
        test_ok,
    ]
    p = f = 0  # p = passed; f = failed.
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
    print(f"combine_images Test: Ran {p + f} tests: {p} passed, {f} failed.")
    if names:
        print("Failed:", ", ".join(names))


if __name__ == "__main__":
    run_all()
