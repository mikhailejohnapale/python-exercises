# 1.If we list all the natural numbers below 10 that
# are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# multiples-3-5.py


def main():
    print("Enter Number : ")
    x = eval(input())

    total = 0
    for n in range(x):
        if n % 3 == 0 and n % 5 == 0:
            total = total + n
        elif n % 3 == 0:
            total = total + n
        elif n % 5 == 0:
            total = total + n
    print(total)

if __name__ == "__main__":
    main()
