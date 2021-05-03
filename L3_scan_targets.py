import L1_lidar as lidar
import L2_vector as vec

import numpy as np

def scan():
    n = lidar.polarScan()
    #n = vec.getValid(scan)
    dist = n[:, 0]                               # store just first column
    angles = n[:, 1]                             # store just 2nd column
    #valid = np.where(dist < 2)                  # find values 16mm
    #dist = dist[valid]                            # get valid distances
    #angles = angles[valid]                           # get corresponding valid angles
    #output = np.vstack((myNums, myAng))             # recombine columns
    #n = output.T
    length = len(angles) - 1
    a = [None] * (length)
    d = [None] * (length)
    na = [None] * 20
    nd = [None] * 20
    for x in range(length):
        if abs(angles[x+1]-angles[x]) < 20 and abs(dist[x+1]-dist[x] < 0.2):
            a[x] = angles[x]
            d[x] = dist[x]
    #print(a)
    #print(d)
    #print(n)
    i = 0
    j = 1
    gatherAngles = 0
    gatherDist = 0
    for x in range(length-1):
        if a[x] != None and a[x+1] == None:
            gatherAngles = gatherAngles + a[x]
            gatherDist = gatherDist + d[x]
        elif a[x] != None and a[x+1] != None:
            gatherAngles = gatherAngles + a[x]
            gatherDist = gatherDist + d[x]
            j += 1
        elif a[x] == None and a[x+1] !=None:
            na[i] = gatherAngles/j
            nd[i] = gatherDist/j
            i += 1
            gatherAngles = 0
            gatherDist = 0
    na = list(filter(None, na))
    nd = list(filter(None, nd))
    output = np.vstack((nd, na))             # recombine columns
    n = output.T
    return n
    

