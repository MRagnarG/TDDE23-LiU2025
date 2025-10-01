# %%

def basfall(valid_exp : list | str, interp : dict)-> str :
    """
    Function that takes an argument (list | str) and a condition (dict) and 
    checks if they are valid to furhter usage.
    """
    #Check if valid_exp is empty.
    if not valid_exp:
        return
    
    #Check if interp is empty, if yes, fyll it with lista's items.
    if not interp:
        new_dict = {}
        for item in valid_exp:
            if item not in ("AND", "OR", "NOT") and not isinstance(item,list):
                new_dict[item] = item
        return interpret(valid_exp,new_dict)
    
    
def work_with_op(valid_exp : list | str, interp : dict)-> str:

    """
    Works with a valid expression with operations and with a interpretation.
    """

    # checks if ""NOT" is in lista and we have most 2 elements on the lsit. 
    # If yes, invert value of rec. of second element.   
    if valid_exp[0] == "NOT" and len(valid_exp) == 2:
        if interpret(valid_exp[1], interp) == "true":
            return "false"
        else:
            return "true" 
            
    #checks if lenght is 3
    if len(valid_exp) == 3:

        #defines 3 variables to the elements on list, which 2 are rec.
        left = interpret(valid_exp[0], interp)
        operation = valid_exp[1]
        right = interpret(valid_exp[2], interp)

        #work with AND
        if operation == "AND":
            if left == "true" and right == "true":
                return "true"
            else:
                return "false"

        #work with OR    
        if operation == "OR":
            if left == "true" or right == "true":
                return "true"
            else:
                return "false"

    
def valid_exp_is_list (valid_exp : list , interp : dict)-> str:

    """
    Works with a valid expression (list) and with a interpretation (dict).
    Returns "true" or "false" as str.
    """

    # Create a variable to the first item of the list.
    first_in_list = valid_exp[0]
        
     # if only one element in valid_exp and this element in interp, 
     # return value.    
    if len(valid_exp) == 1 and isinstance(first_in_list, str):
        return interpret(valid_exp[0], interp)
    
    work_with_op(valid_exp, interp)


def valid_exp_is_str (valid_exp : str , interp : dict)-> str:

    """
    Works with a valid expression (str) and with a interpretation (dict).
    Returns "true" or "false" as str.
    """

    if valid_exp in interp.keys():
            return interp[valid_exp] 
    
    if valid_exp == "true":
        return "true"
    
    if valid_exp == "false":
        return "false"
            
    
def interpret(valid_exp : list | str, interp : dict)->str:
    """
    Main function that will take a expression (str | list) and a 
    interpretation (dict) and checks if the expression is valid or not.
    """
    
    basfall(valid_exp, interp)

    # Works this flow if the valid_exp is a list.
    if isinstance(valid_exp,list):
        valid_exp_is_list(valid_exp, interp)
        
    # Works this flow if the valid_exp is a str.
    else:
        valid_exp_is_str(valid_exp, interp)

        