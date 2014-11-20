#-------------------------------------------------------------------------------
# Name:        ClassicFactorization.py
# Purpose:
#
# Notes:       Factors an int number into a factor list in cordon format.
#
# References:
#
# Author:      User
#
# Created:     11/20/2014
# Copyright:   None
# Licence:     Public Domain
#
#-------------------------------------------------------------------------------

    # Main #
def main():

        # Main Code
    print("Factor/Cordon List: %s") %(f_Factors(91))
    help(f_Factors)
#-----------Basement------------

    # Functions #
        # Normal Functions
def f_Factors(v_Num):
    """Syntax: (int); Returns: A str list;
    Desc.: Factors an int number into a factor list in cordon format.
    Test: print("Factor/Cordon List: %s") %(f_Factors(91))"""
    return sorted(list(set(reduce(list.__add__,([i, v_Num//i] for i in xrange(1, int(v_Num**0.5) + 1)\
                     if v_Num % i == 0)))))

    # Main Loop #
if __name__ == '__main__':
    main()
