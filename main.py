import numpy as np

def current(array):
    lst = np.array(array)

    return lst

def alternative(array):
    lst = np.array(array)
    
    return lst

def addeach(current, alternative):
    newarray = []
    if len(current) >= len(alternative):
        for x in range(len(current)):
            if x < len(alternative):
                newarray.append(current[x] + alternative[x])
            else:
                newarray.append(current[x])
    else:
        for x in range(len(alternative)):
            if x < len(current):
                newarray.append(current[x] + alternative[x])
            else:
                newarray.append(alternative[x])

    return newarray 
def subeach(current, alternative):
    newarray = []
    if len(current) >= len(alternative):
        for x in range(len(current)):
            if x < range(len(current)):
                newarray.append(current[x] - alternative[x])
            else:
                newarray.append(current[x])
    else:
        for x in range(len(alternative)):
            if x < len(current):
                newarray.append(current[x] - alternative[x])
            else:
                newarray.append(alternative[x])

    return newarray
def muleach(current, alternative):
    newarray = []
    if len(current) >= len(alternative):
        for x in range(len(current)):
            if x < len(alternative):
                newarray.append(current[x] * alternative[x])
            else:
                newarray.append(current[x])

    else:
        for x in range(len(alternative)):
            if x < len(current):
                newarray.append(current[x] * alternative[x])
            else:
                newarray.append(alternative[x])

    return newarray
def gaussianElimination(array):
    elimination_array = []
    for y in array:
        #print(y)
        count = 0
        while array[-1][0] != 0:
            count = count + 1
            if count == 10:
                break
            for x in range(len(y)):
                if array[-1][x] > 0:
                    array[-1][x] = array[-1][x] - array[0][x]
                elif array[-1][x] < 0:
                    
                else:
                    print(array[-1])
    
    print(array[-1])
        

    
cur = current([5,2,1,3])
nxt = alternative([6,2,3,5,9])

#print(addeach(cur,nxt))
#print(subeach(cur,nxt))
#print(muleach(cur,nxt))

arr= [[5,3,2], 
      [2,3,1]]

gaussianElimination(arr)