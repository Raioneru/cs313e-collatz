import sys

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

    if i > j:
        temp = j
        j = i
        i = temp
    assert j > i
        
    v = 0
        
    for x in range(i, j+1):
        assert x > 0
        c=1
        
        while x > 1:
            if (x % 2) == 0:
                x = (x // 2)
                c+= 1
            else:
                x = ((3 * x) + 1)/2
                c += 2

        if c > v:
            v = c
        
    return v

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
        
collatz_solve(sys.stdin, sys.stdout)
