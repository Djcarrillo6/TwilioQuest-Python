
import sys

sys.argv.pop(0)

for arg in sys.argv:
    if (int(arg) % 3 == 0) and (int(arg) % 5 == 0):
        print("fizzbuzz")
    elif int(arg) % 5 == 0:
        print("buzz")
    elif int(arg) % 3 == 0:
        print("fizz")
    else:
        print(arg)
