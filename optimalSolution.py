from copy import deepcopy

from transportTask import taskFunc


def checkOptimal(vect_A, vect_B, matr_C, matr_X):
    n, m = len(vect_A), len(vect_B)
    count = n + m - 1
    switch = 0

    rowQueue = []
    columnQueue = []

    rowPotentials = [None] * n
    columnPotentials = [None] * m

    rowPotentials[0] = 0
    rowQueue.append(0)

    while count:
        if switch == 1:
            for i in range(n):
                if rowPotentials[i] == None:
                    for j in columnQueue:
                        if matr_X[i][j] != -1 and rowPotentials[i] == None:
                            rowPotentials[i] = matr_C[i][j] - columnPotentials[j]
                            count -= 1
                            rowQueue.append(i)
            columnQueue.clear()
        else:
            for j in range(m):
                if columnPotentials[j] == None:
                    for i in rowQueue:
                        if matr_X[i][j] != -1 and columnPotentials[j] == None:
                            columnPotentials[j] = matr_C[i][j] - rowPotentials[i]
                            count -= 1
                            columnQueue.append(j)
            rowQueue.clear()
        switch = 1 - switch
    min_val = (matr_C[0][0] - rowPotentials[0] - columnPotentials[0], 0, 0)
    for i, vect_C in enumerate(matr_C):
        for j, var_C in enumerate(vect_C):
            temp = (var_C - rowPotentials[i] - columnPotentials[j], i, j)
            min_val = min_val if min_val <= temp else temp
    if min_val[0] < 0:
        return min_val[1:3]
    return (-1, -1)


def dfsBasis(matr_X, m, v, list_v, pos0, min_val, switch):
    flag = False
    print((v // m, v % m))
    if switch == 1:
        min_vert = min(matr_X[v // m][v % m], min_val)
        if min_vert < min_val:
            flag = True
    else:
        min_vert = min_val
    if list_v[v] == pos0:
        if flag:
            matr_X[v // m][v % m] = -1
        else:
            matr_X[v // m][v % m] -= min_vert
        return min_vert
    min_vert = dfsBasis(matr_X, m, list_v[v], list_v, pos0, min_vert, 1 - switch)
    if switch == 1:
        matr_X[v // m][v % m] += min_vert
    else:
        if matr_X[v // m][v % m] == min_vert and flag:
            matr_X[v // m][v % m] = -1
        else:
            matr_X[v // m][v % m] -= min_vert
    return min_vert


def newBasisVar(vect_A, vect_B, matr_C, matr_X, i0, j0):
    n, m = len(vect_A), len(vect_B)

    list_Vertex = {}
    col_Edges = {}
    row_Edges = {}
    matr_X[i0][j0] = 0
    for i, vect_X in enumerate(matr_X):
        for j, var_X in enumerate(vect_X):
            if var_X != -1:
                list_Vertex[i * m + j] = None
                col_Edges[i * m + j] = []
                row_Edges[i * m + j] = []
    for key in list_Vertex:
        for i in range(n):
            if (i == key // m):
                continue
            if matr_X[i][key % m] != -1:
                col_Edges[key].append(i * m + key % m)
        for j in range(m):
            if (j == key % m):
                continue
            if matr_X[key // m][j] != -1:
                row_Edges[key].append(key - key % m + j)
    switch = 0
    pos0 = i0 * m + j0
    list_Vertex[pos0] = -1
    vertexQueue = [pos0]
    vertexQueueNext = []
    flag = True
    while flag:
        for v in vertexQueue:
            if switch == 0:
                for pos in row_Edges[v]:
                    if list_Vertex[pos] == -1:
                        list_Vertex[pos] = v
                        flag = False
                    list_Vertex[pos] = v
                    vertexQueueNext.append(pos)
            else:
                for pos in col_Edges[v]:
                    if list_Vertex[pos] == -1:
                        list_Vertex[pos] = v
                        flag = False
                    list_Vertex[pos] = v
                    vertexQueueNext.append(pos)
            if not flag:
                break
        switch = 1 - switch
        vertexQueue.clear()
        vertexQueue = vertexQueueNext.copy()
        vertexQueueNext.clear()
    v = pos0
    v_next = list_Vertex[v]
    v_min = v_next
    min_val = matr_X[v_min // m][v_min % m]
    switch = 0
    while True:
        if switch == 1 and matr_X[v // m][v % m] < min_val:
            min_val = matr_X[v // m][v % m]
            v_min = v
        switch = 1 - switch
        v = v_next
        v_next = list_Vertex[v]
        if v == pos0:
            break
    switch = 0
    v = pos0
    v_next = list_Vertex[v]
    while True:
        if v == v_min:
            matr_X[v // m][v % m] = -1
        elif switch == 1:
            matr_X[v // m][v % m] -= min_val
        else:
            matr_X[v // m][v % m] += min_val
        switch = 1 - switch
        v = v_next
        v_next = list_Vertex[v]
        if v == pos0:
            break


def optimalSolution(user_data):
    n, m, vect_A, vect_B, matr_C, matr_X = deepcopy(user_data)
    res = 0
    i, j = checkOptimal(vect_A, vect_B, matr_C, matr_X)
    while i != -1:
        res += 1
        newBasisVar(vect_A, vect_B, matr_C, matr_X, i, j)
        i, j = checkOptimal(vect_A, vect_B, matr_C, matr_X)
    txt = taskFunc(matr_C, matr_X)
    return (n, m, vect_A, vect_B, matr_C, matr_X, txt, res)
