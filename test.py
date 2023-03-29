import sys
import numpy as np
def countOn():
    A = np.array([1,23,5])
    B = np.array([1,1,5])
    print(A)
    print(B)
def printName(name):
    print("My name is",name)
def main(name):
    print("dd")
    printName(name)
    countOn()

if __name__ == "__main__":
    main(sys.argv[1])