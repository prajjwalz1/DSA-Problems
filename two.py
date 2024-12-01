"""
Q.2. Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three, output "Fizz" instead of the number. For multiples of five, output 
"Buzz". For numbers that are multiples of both three and five, output "FizzBuzz".

"""

#program that will return the string representation of numbers beetween 1 to n, with the given condition of fizz buzz

def print_fizz_buzz(num):
    num_string=[]
    for n in range(1,num):
        if n%3==0 and n%5==0:
            num_string.append("fizz buzz")
        elif n%3==0:
            num_string.append("fizz")
        elif n%5==0:
            num_string.append("buzz")
        else:
            num_string.append(str(n))
    return num_string

if __name__ == "__main__":
    print(print_fizz_buzz(20))