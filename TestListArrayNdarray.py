import array
import numpy as np

def main():
    # List
    thisIsList = [0, 1, 2, 'a', 'b', [0, 1]] # it can contain any, including the other list
    print(thisIsList)
    thisIsList.append('aho')
    print(thisIsList)
    # how to use slice, start:end:step, start is included but stop is excluded, step can be omitted 
    print(thisIsList[0:3])
    print(thisIsList[::3])
    print(thisIsList[5][1])

    # Array
    thisIsArray = array.array('f', [0.0, 1.0, 2.0, 3.0, 4.0]) # it can contain the same data type, and is one dimensional
    print(thisIsArray)

    # Ndarray
    thisIsNdarray = np.array([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0]], dtype = float) #it can contain same data type, and it can be N dimensional
    print(thisIsNdarray)
    thisIsNdarray = thisIsNdarray.reshape(4,3) # change to 3 x 4 matrix
    print(thisIsNdarray)
    thisIsNdarray = thisIsNdarray.reshape(3,4) # change back to 4 x 3 matrix
    print(thisIsNdarray)
    # how to use slice
    print(thisIsNdarray[1, :]) # get index = 1 row of any column
    print(thisIsNdarray[:, 2]) # get index = 2 column of any row
    print(thisIsNdarray[:,0:3:2]) # get index 0 and 2 columns of any row
    thisIsNdarray[:,:] = 0.0 # set all to 0
    print(thisIsNdarray)
    thisIsNdarray[0:2,:] = 1.0 #set index 1 and 2 row of any column to 1.0 
    print(thisIsNdarray)
    thisIsNdarray[:,2] = 2.0 # set index 2 column of any row to 2.0 
    print(thisIsNdarray)
    # how to initialize
    thisIsNdarray = np.arange(0.0, 12.0, 1.0, dtype = float).reshape(3,4) # does same as the first initialization
    print(thisIsNdarray)
    thisIsNdarray = np.zeros((3, 4), dtype = float) # if no default value is necessary, 'empty' method can be used
    print(thisIsNdarray)

if __name__ == "__main__":
    main()