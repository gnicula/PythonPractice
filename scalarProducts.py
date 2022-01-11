import numpy as np

def dotMultiplier(a:list, b:list):
    # output = np.dot(np.array(a), np.array(b))
    output = np.array(a) @ np.array(b).T
    return output


def main():
    size = int(input("Enter the number of rows in the vector: "))

    lstA = []
    lstB = []
    
    valA = input("Enter the first vector separated by commas: ")
    valA = valA.strip().split(",")
    
    for i in range(0, size):
        lstA.append(int(valA[i]))
    
    valB = input("Enter the second vector separated by commas: ")
    valB = valB.strip().split(",")

    for i in range(0, size): 
        lstB.append(int(valB[i]))
    
    print (lstA)
    print (lstB)
    print(dotMultiplier(lstA, lstB))


if __name__ == "__main__":
    main()