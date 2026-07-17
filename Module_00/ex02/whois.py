import sys

if len(sys.argv) == 1:
    sys.exit(0)

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

try:
    n = int(sys.argv[1])  # int transforms the argument into an integer
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if n == 0:
    print("I'm Zero")
elif n % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")



#try:
#    # Code qui peut provoquer une erreur
#except TypeErreur:
#    # Code exécuté si cette erreur arrive