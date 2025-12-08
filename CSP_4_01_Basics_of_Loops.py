#All questions must use a loop for full points.
import random


def oddNumbers(n):
    if n < 1:
        return ""

    result = ""
    # Loop through numbers from 1 to n
    for i in range(1, n + 1, 1):
        # Check if number is odd
        if i % 2 == 1:
            result += str(i) + " "
    result = result.strip()
    return result


def backwards(n):
    result = " "
    for i in range(n, 0, -1):

        result = result + str(i) + " "

    result = result.strip()

    return result


def randomRepeating():
    roll = random.randint(0,10)
    tries =1
    while roll <10:
        tries = tries + 1
    return "it took "+tries+"to get to a ten"
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    print(f"it took {tries} tries to get a 10")
def randomRange(n):
    import random
    # Generate first number to start
    highest = random.randint(1, 100)
    lowest = highest

    for i in range(2, n + 1):
        num = random.randint(1, 100)
        print("Roll", i, ":", num)

        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

        return highest and lowest


def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word



def fizzBuzzContinuous(n):
    x = ""
    for i in range(1,n+1,1):
        if i%3==0 and i%5==0:
           x = x + "fizzbuzz "
        elif i % 3 == 0:
            x = x + "fizz "
        elif i%5 ==0:
            x = x + "buzz "
        else:
             x = x + str(i)+" "
    return x[:-1]
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """

def collatz(n):
    out = ""
    while n != 1:
        out += f"{n} "
        if n %2 ==0:
            n = n//2
        else:
            n = n*3 + 1
    return out+ "1"

print(collatz(15))

def fibonacci(n):
    if n == 0:
        return ""
    if n == 1:
        return "0"

    result = "0 1"
    prev = 0
    current = 1

    for i in range(2, n, 1):
        next_num = prev + current
        result += " " + str(next_num)
        prev = current
        current = next_num

    return result


#print(fibonacci(300))