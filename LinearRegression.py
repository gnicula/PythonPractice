import numpy as np
import matplotlib.pyplot as plt

def buildSet(isInference=False):
    size = int(input("input the size of your dataset: "))
    arr = list()
    if isInference:
        print("Enter each data point feature: ")
    else:
        print("Enter each datapoint by itself, with each feature separated by commas: ")

    for i in range(size):
        str = input()
        str = [float(x) for x in str.strip().split(",")]
        arr.append(str)

    return np.array(arr)


def buildModel(data):
    a = data[:, :-1] # Slices all features into one arr
    b = data[:, -1:] # Slices the labels into an arr
    v1 = np.ones_like(b) # Creates a list of all 1's with the size of b
    a = np.append(a, v1, axis=1) # Appends the 1 bias vector to the end of the features

    model, _, _, _ = np.linalg.lstsq(a, b, rcond=None) # Finds the least square of the features and the labels.
    return model


def inference(model, b):

    # print(model[:-1,:])
    # print(np.repeat(model[-1:,:], b.shape[0], axis = 1))
    # print(model[:-1,:] @ b.T)
    predictions = model[:-1,:] @ b.T + np.repeat(model[-1:,:], b.shape[0], axis = 1) # multiplies the model with with predictions transposed,
    return predictions                                                               # to get the expected value.

def plot(model, trainingData, infIn, preds):
    xD = trainingData[:,0]
    yD = trainingData[:,1]
    if model.shape[0] > 2:
        print("Cannot plot more than two dimensions. ")
    else:
        x = np.squeeze(infIn)
        y = np.squeeze(preds)
        plt.figure(figsize = (8,8))
        
        plt.plot(x, y, 'r', label='Fitted line')
        plt.scatter(x, y, marker='o', color='b')
        plt.scatter(xD, yD, marker='o', color='g')
        plt.show()


def main():
    a = buildSet()
    
    model = buildModel(a)
    b = buildSet(True)
    pred = inference(model, b)

    plot(model, a, b, pred)
    


if __name__ == "__main__":
    main()
