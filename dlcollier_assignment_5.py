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


