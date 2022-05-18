#--> Modular reduction
#-> Modular reduction of a polynomial in integer representation (max 64 bit) against a generating relation

import pyfiglet # ascii_banner
from operator import xor # for xor-operation

# ASCII - Banner
ascii_banner = pyfiglet.figlet_format("Modular Reduction")
print(ascii_banner)

# Input
InputPolynomial = "0"
ReducingPolynomial = "00"

while(len(InputPolynomial) < len(ReducingPolynomial)):

    print("The polynomial to be reduced shall be higher then the reducing polynomial")

    try:
        print("\nPlease enter a valid Hex-Number as (0x...): ")
        InputPolynomial = format(int(input("Polynomial to be modular reduced: "), 16), 'b') # Converting hex into int and then into binary
    except Exception as e:
        print("\nError: ", e)

    try:
        print("\nPlease enter a valid Hex-Number (0x...): ")
        ReducingPolynomial = format(int(input("Reducing polynomial: "), 16), 'b') # Converting hex into int and then into binary
    except Exception as e:
        print("\nError: ", e)    


# modular_reduction function
def modular_reduction(InputPolynomial, ReducingPolynomial):
    ResultPolynomial = InputPolynomial

    while(len(ResultPolynomial) >= len(ReducingPolynomial)):

        ReducingPolynomial_Temp = ReducingPolynomial # declaring a var for the reducing polynomial for temporary shifts to the left for xor and reset it every loop of modular reduction
        
        # adding 0's on the right side of the reducing polynomial until the polynomials have the same most-significant-bit (msb) index
        while(len(ResultPolynomial) != len(ReducingPolynomial_Temp)):
            ReducingPolynomial_Temp = ReducingPolynomial_Temp + "0"

        print("\nThe temporary reducing polynomial is: \n", ReducingPolynomial_Temp, "\n", hex(int(ReducingPolynomial_Temp, 2)))

        # XOR Operation
        ResultPolynomial = format(xor(int(ResultPolynomial, 2), int(ReducingPolynomial_Temp, 2)), 'b')
        print("\nYour temporary resulting polynomial is: \n", ResultPolynomial, "\n", hex(int(ResultPolynomial, 2)))



    print("\nThe Hex presentation of the resulting polynomial is: \n", hex(int(ResultPolynomial, 2))) # Hex presentation

    return ResultPolynomial


# calling the modular_reduction function
modular_reduction(InputPolynomial, ReducingPolynomial)