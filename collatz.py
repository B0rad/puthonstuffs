# def collatz(number):
#     if number % 2 == 0:
#         return number 
#         print(int(number // 2))
#     else:
#         print(int(3 * number + 1))
#         return 3 * number + 1

# collatz(input())


def is_even():
    x = int(input("Enter number"))
    if x % 2 == 0:
        return x, "is an even number"
    else:
        return x, "is not an even number"
print(is_even())