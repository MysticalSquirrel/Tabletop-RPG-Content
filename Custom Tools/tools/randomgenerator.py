import random

print("Input the minimum number you want to randomize from. (Default: 0)")
n1 = input()

print("Input the maximum number you want to randomize between. (Default: 20)")
n2 = input()

if n1.isdigit() is False:
    n1 = 0
else:
    n1 = int(n1)
if n2.isdigit() is False:
    n2 = 20
else:
    n2 = int(n2)

print("The randomized number is:")
randomize = random.randrange(n1, n2, 1)
print(randomize)

export_file = open("../randomized_numbers.txt", "a")
export_file.write(str(randomize) + "\n")
export_file.close()
