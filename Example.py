# Example Python
print "Example Arithmatic Programming"

number = raw_input("Enter a number: ")
number = int(number)
number2 = raw_input("Enter another number:")
number2 = int(number2)
number3 = raw_input("Enter another number:")
number3 = int(number3)
# this function does multiplication
def multiplication(num, num2, num3):
    product = num * num2 * num3
    print "%r * %r * %r = %r" % (num, num2, num3, product)

def addition(num, num2):
    sum = num + num2
    print "%r + %r = %r" % (num, num2, sum)

def subtraction(number, number2):
    sum = number - number2
    print "%r-%r = %r" % (number, number2, sum)

def division(num, num2):
    if(num != 0):
        quotient = num / num2
        print "%r / %r = %r" % (num, num2, quotient)
    else:
        print "ERROR! Can't divide by zero!"

def pythagorean(a_squared, b_squared):
    c_squared = (a_squared * a_squared) + (b_squared * b_squared)
    print "%r squared + %r squared = %r" % (a_squared, b_squared, c_squared)


def main():
    multiplication(number, number2, number3)
    addition(number, number2)
    subtraction(number, number2)
    division(number, number2)
    pythagorean(number,number2)

main()