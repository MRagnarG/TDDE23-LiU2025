
#4a
# %%

def split_it(txt:str)->str:


    fall1 = ""
    fall2 = ""

    for char in txt:

        if char.islower() or char in ("_", "."):
            fall1 += char
        
        elif char.isupper() or char.isspace() or char == "|":
            fall2 += char
    
    return (fall1,fall2)


def split_rec(txt:str)->str:

    if not txt:
        return "", ""
    
    fall1 = ""
    fall2 = ""

    char = txt[0]
    f1, f2 = split_rec(txt[1:])

    if char.islower() or char in ("_", "."):
        fall1 += char

    elif char.isupper() or char.isspace() or char == "|":
        fall2 += char

    fall1 += f1
    fall2 += f2

    return fall1, fall2
