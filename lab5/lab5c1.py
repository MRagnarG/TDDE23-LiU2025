# %%
from lab5c_combine_images import test_combine_images
from lab5c_generator_from_image import test_generator_from_image
from lab5c_pixel_constraint import test_pixel_constraint

def test_all():
    test_combine_images
    test_pixel_constraint
    test_generator_from_image
    print("\nAll tests have passed.")

if __name__ == "__main__":
    test_all()