def northWestAngle(vect_A, vect_B, matr_C, matr_X):
    n = len(matr_X)
    m = len(matr_X[0])
    i, j = 0, 0
    while i < n and j < m:
        min_val = min(vect_A[i], vect_B[j])
        vect_A[i] -= min_val
        vect_B[j] -= min_val
        matr_X[i][j] = min_val
        if (vect_A[i] == 0):
            i += 1
        else:
            j += 1


def minCast(vect_A, vect_B, matr_C, matr_X):
    n = len(matr_X)
    m = len(matr_X[0])
    rowNotUsed = [True]*n
    colNotUsed = [True]*m
    sortArray = []
    for i in range(n):
        sortArray.extend([(matr_C[i][j], i, j) for j in range(m)])
    sortArray.sort(key=lambda x: x[0])
    for var in sortArray:
        i = var[1]
        j = var[2]
        if rowNotUsed[i] and colNotUsed[j]:
            min_val = min(vect_A[i], vect_B[j])
            vect_A[i] -= min_val
            vect_B[j] -= min_val
            matr_X[i][j] = min_val
            if (vect_A[i] == 0):
                rowNotUsed[i] = False
            else:
                colNotUsed[j] = False


def delCell(Vect, ind, coor):
    for i in range(len(Vect)):
        if Vect[i][coor] == ind:
            Vect.pop(i)
            break


def FogelApproximation(vect_A, vect_B, matr_C, matr_X):
    n = len(matr_X)
    m = len(matr_X[0])
    n0, m0 = n, m
    i0, j0 = 0, 0
    Rows = [[] for i in range(n)]
    Columns = [[] for j in range(m)]
    for i,vect_C in enumerate(matr_C):
        for j,var_C in enumerate(vect_C):
            Rows[i].append((var_C, i, j))
            Columns[j].append((var_C, i, j))
    for Row in Rows:
        Row.sort()
    for Column in Columns:
        Column.sort()

    if m > 1:
        min_Rows = [(Rows[i][1][0] - Rows[i][0][0], Rows[i][0][2]) for i in range(n)]
    else:
        min_Rows = [(-1, 0)]*m
    if n > 1:
        min_Columns = [(Columns[j][1][0] - Columns[j][0][0], Columns[j][0][1]) for j in range(m)]
    else:
        min_Columns = [(-1, 0)]*m

    while n0 and m0:
        if n0 + m0 == 2:
            for ind,val in enumerate(vect_A):
                if val:
                    i0 = ind
                    break
            for ind, val in enumerate(vect_B):
                if val:
                    j0 = ind
                    break
            min_val = min(vect_A[i0], vect_B[j0])
            vect_A[i0] -= min_val
            vect_B[j0] -= min_val
            matr_X[i0][j0] = min_val
            break

        max_val_Rows=max(min_Rows,key=lambda x:x[0])
        max_val_Columns=max(min_Columns,key=lambda x:x[0])
        if max_val_Rows[0]>max_val_Columns[0]:
            i0=min_Rows.index(max_val_Rows)
            j0=min_Rows[i][1]
        else:
            j0 = min_Columns.index(max_val_Columns)
            i0 = min_Columns[i][1]

        min_val = min(vect_A[i0], vect_B[j0])
        vect_A[i0] -= min_val
        vect_B[j0] -= min_val
        matr_X[i0][j0] = min_val
        if vect_A[i0] == 0:
            Rows[i0].clear()
            min_Rows[i0] = (-1, 0)
            n0-=1
            if n0 > 1:
                for j,Column in enumerate(Columns):
                    if Column:
                        delCell(Column, i0, 1)
                        min_Columns[j]=(Column[1][0] - Column[0][0], Column[0][1])
            else:
                min_Columns = [(-1, 0)]*m
        if vect_B[j0] == 0:
            Columns[j0].clear()
            min_Columns[j0] = (-1, 0)
            m0 -= 1
            if m0 > 1:
                for i,Row in enumerate(Rows):
                    if Row:
                        delCell(Row, j0, 2)
                        min_Rows[i]=(Row[1][0] - Row[0][0], Row[0][2])
            else:
                min_Columns = [(-1, 0)]*n
        if vect_A[i0] == vect_B[j0]:
            for i in range(n):
                if i != i0 and matr_X[i][j0] == -1:
                    matr_X[i][j0] = 0
                    break
