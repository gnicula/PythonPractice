import numpy as np

def readInput():
    size = int(input("Enter the size of the square matrix: "))
    matrA = list()
    vectB = list()
    print("Enter the matrix one row at a time, separated by commas")
    for i in range(size):
        rowStr = input()
        rowStr = rowStr.strip().split(",")[:size]
        rowStr = [float(x) for x in rowStr]
        matrA.append(rowStr)
    
    vectB = input("Enter the vector sepearated by commas: ")
    vectB = [float(x) for x in vectB.strip().split(",")][:size]
    
    return np.array(matrA), np.array(vectB)[np.newaxis].T

def main():
    a, b = readInput()
    # print(b)
    if np.linalg.det(a) == 0:
        print("System has an infinite number of solutions. Here is the best approximation ")
        print(np.linalg.lstsq(a, b, rcond = None)[0])

    else:
        print(np.linalg.inv(a) @ b)

if __name__ == "__main__":
    main()