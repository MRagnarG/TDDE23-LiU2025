# %%
from lab5a import cvimg_to_list
from lab5b2 import generator_from_image
import cv2
# %%
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
            len(list_img) : 0,
            "" : TypeError,
            "a" : TypeError
        }

        for index_test in data:
            expected = data[index_test]

            if expected in (IndexError, TypeError):
                
                try:
                    test(index_test)
                    raise AssertionError(f"Expected IndexError for input"
                        +f"{index_test}, but no error was raised."
                        +f" Got: {test(index_test)}")
                
                except IndexError:
                    print(f"Correctly raised IndexError for {index_test} .")

                except TypeError:
                    print(f"Correctly raised TypeError for {index_test} .")
                
                
            else:

                result = test(index_test)
                
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