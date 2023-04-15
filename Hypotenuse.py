# Compute the Hypotenuse
# Write a function that takes the lengths of the two shorter sides of a right triangle asits parameters. 
# Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. 
# Include a main program that reads the lengths of the shorter sides of a right triangle from the user, 
# uses your function to compute the length of the hypotenuse, and displays the result.

import math
# tạo hàm tính canh huyền c của tam giác vuông, sử dụng công thức toán căn bậc 2
def hypotenuse(a,b):
    a_squared = pow(a,2)
    b_squared = pow(b,2)
    c_squared = a_squared + b_squared
    c = math.sqrt(c_squared)
    return c

#Tạo hàm nhập giá trị các cạnh a,b, in ra giá trị cạnh huyền c và làm tròn
def result():
    a,b = None, None;
    while True:
        try:
            a = int(input("Enter the length of side A: "))
            b = int(input("Enter the length of side B: "))
            c = hypotenuse(a,b)
            c1= round(c);
            print("The length of the hypotenuse is: ", c1)
            action = input("Do you want to continue: (Y/N)");
            if action == 'N' or action == "n":
                break;
        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    result()