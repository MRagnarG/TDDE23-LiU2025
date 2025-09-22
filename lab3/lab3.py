# Lab3A

from math import fabs, isqrt

def new_board()->dict:
    """
    Simple function that will return a empty dictionary to use
    as a game "database".
    """
    
    return {}

def is_free(board:dict, c:int, r:int)->bool:
    """
    Function that will check if a specific place, formed by
    column x row, is free on a virtual board game.

    board: Supports dict
    c: Supports Int
    r: Supports Int
    """

    return (c,r) not in board.keys()

def place_piece(board:dict, c:int, r:int, player:str)->bool:
    """
    Function that will, if possible, place a piece on the game.

    board: Supports dict - where the "database" is
    c: Supports Int
    r: Supports Int
    player: Supports Str
    """

    if is_free(board, c, r):
        board[(c,r)] = player
        return True
    else:
        return False

def get_piece(board:dict, c:int, r:int):
    """
    Function that will return which player has a piece on a 
    specific position. If there's no piece there, will return
    False.

    board:Supprots dict
    c: Supports int
    r: Supports int
    """
    if not is_free(board, c,r):
        return board[(c,r)]
    else:
        return False

def remove_piece(board:dict, c:int, r:int)->bool:

    """
    Function that, if there's a piece on a specific position,
    will remove it from the game (dict) and return True. 
    Otherwise, will return False.

    board: Supports dict
    c: Supports int
    r: Supports int
    """

    if not is_free(board, c,r):
        board.pop((c,r))
        return True
    else:
        return False

def move_piece(board:dict, c1:int, r1:int, c2:int, r2:int)->bool:

    """
    Function that will move a piece from a specific position,
    to a future specific position. Checks first if future position
    is free and if there's a piece on the original position.
    Return True and moves the piece if conditions are met,
    otherwise, returns False.

    board: Supports dict
    c1: Supports int
    r1: Supports int
    c2: Supports int
    r2: Supports int
    """

    if is_free(board, c2, r2) and not is_free(board, c1,r1):
        board[(c2,r2)] = board.pop((c1, r1))
        return True
    else:
        return False
    
def nearest_piece(board:dict, c:int, r:int)->tuple:

    """
    Function that will check if which is the nearest piece.
    Uses Pythagoras theorem to calculate the distance.
    It returns the coordinates of the neares peace, in the
    format of (column, row), beeing column and row two integers.

    board: Supports dict
    c: Supports int
    r: Supports int
    """
    
    distance = 1000000000000
    nearest = ()

    for p in board.keys():
        (kolumn, rad) = p
        c1 = fabs(c- kolumn)
        c2 = fabs(r-rad)

        temp_dis = isqrt(int(c1)**2+int(c2)**2)
        if temp_dis < distance:
            distance = temp_dis
            nearest = p

    return nearest

def count(board:dict, c_or_r:str, plats:int, player:str)->int:

    """
    Function that will count how many pieces of a certain
    player are on a specific row or column. Return the 
    ammount.

    board: Supports dict
    c_or_r: Supports str
    plats: Supports int
    player: Supports str
    """

    counter = 0
    for p in board.keys():
        (c,r) = p

        if c_or_r == "column" and c == plats and get_piece(board, c, r) == player:
            counter += 1
    
        elif c_or_r == "row" and r == plats and get_piece(board, c, r) == player:
            counter += 1
    
    return counter

# LAB3B


def factorial (x:int)->int:
    """
    Function that will calculate the factorial of a number.
    Works through recurssion.
    If the input comes to 1, then return 1 and finish the recurssion.

    x: Supports int
    """
    if x <= 1:
        return 1
    
    return x * factorial(x-1)

def fac_div(n:int, k:int)->int:
    """
    Function that, given two different positive integer numbers n,k for which n>k, 
    will proceed to multiply n with all the numbers between n and k.
    n*n-1*n-2*...*k+1 . 
    Usefull for factorial divisions, where you have n!/k! .
    Works though recurssion

    n: Supports Int 
    k: Supports Int

    """

    if n == k+1:
        return k+1
    
    return n * fac_div(n-1, k)

def choose (n:int,k:int)->int:
    """
    Function to binomial coefficients. "Combinations of n taken k at a time".
    Given two different positive integers, n,k , for wich n>k, will proceed to
    calculate all the different options to perfom such choice. If n = k, will
    return 1. It's optimized to take big values as n and k.

    n: Supports Int
    k: Supports Int
    """
    if n==k:
        return 1

    diff = n-k

    if k > diff:
        numerator = fac_div(n, k)
        return numerator//factorial(diff)
    else:
        numerator = fac_div(n,diff)
        return numerator//factorial(k)
