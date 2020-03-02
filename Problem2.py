import queue
import numpy

def smallestMultiple(k,digits):
    matrix = []
    for i in range(k):
        matrix.insert(i, [0]*len(digits))
    matrix[0] = digits


    for i in range(1, k):
        for r in range(len(digits)):
            matrix[i][r] = (10 * i + digits[r]) % k

    matrix.insert(k+1, digits)



    return MinString(matrix,len(matrix) - 1)

def MinString(DFA,startstate):
    queue = []


    # array of indexes, 0 = not discovered, 1 = discovered.
    discovered = [0] * len(DFA)
    discovered[startstate] = 1

    parent = [0] * len(DFA)

    label = [""] * len(DFA)

    queue.append(startstate)
    overallcount = 0

    while(len(queue) != 0):
        curr = queue.pop(0)
        count = 0
        for transition in DFA[curr]:
            next = transition
            if next == 0:
                parent[next] = curr
                break
            elif discovered[next] == 0:
                discovered[next] = 1
                parent[next] = curr


                queue.append(next)
                label[next] = str(DFA[0][count])
                #What does this do? its in the pseudocode

            count += 1
            overallcount += 1

    if(next != 0):
        print("no valid solution")
        return parent
    else:
        output = ""
        while(next != len(DFA) - 1):
            output += label[next]
            next = parent[next]
        print(output)















