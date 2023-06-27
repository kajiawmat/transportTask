from copy import deepcopy


def toCloseSystem(vect_A, vect_B, matr_C, matr_X):
    n, m = len(vect_A), len(vect_B)
    dif_sum = sum(vect_A) - sum(vect_B)
    if dif_sum > 0:
        vect_B.append(0)
        for i in range(n):
            matr_C[i] += (0,)
            matr_X[i] += (vect_A[i],) if vect_A[i] else (-1,)
            vect_A[i] = 0
    elif dif_sum < 0:
        vect_A.append(0)
        matr_C.append(tuple(0 for j in range(m)))
        matr_X.append([vect_B[j] if vect_B[j] else -1 for j in range(m)])
        for j in range(m):
            vect_B[j] = 0


def fillBasis(matr_X):
    n = len(matr_X)
    m = len(matr_X[0])
    count = 0
    for vect_X in matr_X:
        for var_X in vect_X:
            if var_X != -1:
                count += 1
    for vect_X in matr_X:
        for ind, val in enumerate(vect_X):
            if count >= n + m - 1:
                return
            if val == -1:
                vect_X[ind] = 0
                count += 1


def sum_lists(list_of_lists):
    res = []
    for list in list_of_lists:
        res.extend(list)
    return res


def taskFunc(matr_C, matr_X):
    res = 'F = ' + ' + '.join(
        sum_lists([[f'{matr_C[i][j]}*{val_X}' for j, val_X in enumerate(vect_X) if val_X != -1] for i, vect_X in
                   enumerate(matr_X)])
    )
    res += ' = ' + str(sum(
        sum_lists([[matr_C[i][j] * val_X for j, val_X in enumerate(vect_X) if val_X != -1] for i, vect_X in
                   enumerate(matr_X)])
    ))
    return res


def transportTask(func, user_data):
    n, m, vect_A, vect_B, matr_C = deepcopy(user_data)
    matr_C = list(map(tuple, matr_C))
    matr_X = [[-1] * m for i in range(n)]
    func(vect_A, vect_B, matr_C, matr_X)
    toCloseSystem(vect_A, vect_B, matr_C, matr_X)
    fillBasis(matr_X)
    txt = taskFunc(matr_C, matr_X)
    return (n, m, vect_A, vect_B, matr_C, matr_X, txt)
