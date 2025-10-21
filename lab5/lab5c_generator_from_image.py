# %%
from lab5a import cvimg_to_list
from lab5b2 import generator_from_image
import cv2

images = {
    "./test_images/saab_arena.jpg" : "Saab Arena",
    "./test_images/praca_liberdade.jpg" : "Praça da Liberdade",
    "./test_images/rio.jpg" : "Rio"
    }

def test_generator_from_image():

    for image in images:
        array_img = cv2.imread(image)
        list_img = cvimg_to_list(array_img)
        test = generator_from_image(list_img)

        data = {
            0 : list_img[0],
            -1 : list_img[-1],
            len(list_img) : IndexError,
            "" : TypeError,
            "a" : TypeError
        }

        for a in data:
            expected = data[a]

            if expected is IndexError:
                
                try:
                    test(a)
                    raise AssertionError(f"Expected IndexError for input {a},"
                            +f" but no error was raised. Got: {test(a)}")
                
                except IndexError:
                    print(f"Correctly raised IndexError for {a}")
                
                except Exception as e:
                    raise AssertionError(f"Expected IndexError but got {type(e).__name__} instead.")
                
            else:

                result = test(a)
                
                assert result == expected, ("Test Error: Image:" 
                +f"{images[image]} || Expected: {expected}|| Got: {result}.")

                print(f"Test succesfull: Image:{images[image]} || Expected: "
                    +f"{expected} || Got: {result}")

        # Summary banner shown only if all assertions pass
        print("""
            *~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~
               C  O  N  G  R  A  T  U  L  A  T  I  O  N  S !
            *~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~.^.~.*~
            """)
        print("\n                          All tests passed!")

test_generator_from_image()