#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

cache =[0]*1226
startC=1
endC=1225

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]


def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    global startC, endC
    
    collatz(startC,endC,cache)
    v = cycle_length(i,j,cache, endC)

    return v

def collatz(start,end,cache):
    v=0
    for num in range (start, end+1):
        origNum= num
        c = 1
        while num> 1:
            if (num % 2) != 0:
                num = num+(num//2) +1
                c+=2
                
            else:
                num = (num // 2)
                c+=1
        if c>v:
            v=c
        cache[origNum]=c
        
    


def cycle_length(i,j, cache, endC):
    maxCycle=0

    if i>j:
        temp = j
        j = i
        i = temp
    assert j >= i
    
    for num in range (i, j+1):
        c=0
        assert i > 0
        while num > endC:
            if (num % 2) != 0:
                num = num+(num//2) +1
                c+=2
                
            else:
                num = (num // 2)
                c+=1
                
        if num<=endC:
            c+=cache[num]
            
            if c > maxCycle:
                maxCycle = c
    assert maxCycle > 0
    return maxCycle



def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")


def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
