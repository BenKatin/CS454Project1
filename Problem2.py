import queue

def smallestMultiple(k,digits):
    matrix = []
    for i in range(k):
        matrix.insert(i, [0]*len(digits))
    matrix[0] = digits


    for i in range(1, k):
        for r in range(len(digits)):
            matrix[i][r] = (10 * i + digits[r]) % k

    matrix.insert(k+1, digits)
    return matrix

def MinString(DFA,startstate):
    print()