#chal 1

print("=== Challenge 1: Collatz Conjecture ===")
number = int(input("Enter starting number: "))
steps = 0

print("Sequence:", number, end=" ")

while number != 1:
    if number % 2 == 0:   
        number = number // 2
    else:                 
        number = number * 3 + 1
    print(number, end=" ")
    steps = steps + 1

print("\nSteps:", steps)

#chal 2

print("\n === Challenge 2: Prime Number Checker ===")

number2 = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {number2-1}...")

isPrime = True
divisor = 0

for x in range(2, number2):
    if number2 % x == 0:
        isPrime = False
        divisor = x
        break

if isPrime == True:
    print(f"{number2} is prime!")
else:
    print(f"{number2} is not prime (divisible by {divisor})")