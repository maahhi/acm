#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    bala = n+1
    pain = 0
    chap = 0
    rast = n+1
    lese_k = []
    for yaroo in obstacles:
        r = yaroo[0]
        c = yaroo[1]
        if r == r_q : 
            if c > c_q and c < rast :
                rast = c
            if c < c_q and c > chap :
                chap = c
        elif c == c_q : 
            if r > r_q and r < bala :
                bala = r
            if r < r_q and r > pain :
                pain = r
        else:
            if c < c_q :
                if

    for yeki in 
        
    javab = 0
    javab += bala - pain -2
    javab += rast - chap -2
    print(bala,pain,rast,chap)
    return javab




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
