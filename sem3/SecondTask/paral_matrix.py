import random
from multiprocessing import Pool
from timeit import default_timer
start_time = default_timer()
def pmatrix(matrix1,matrix2,r1,c1,r2,c2):
    s = 0
    A = matrix1
    B = matrix2
    t = []
    C = []
    if len(B) != len(A[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1 = len(A)
        c1 = len(A[0])
        r2 = c1
        c2 = len(B[0])
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + A[z][i] * B[i][j]
                t.append(s)
                s = 0
            C.append(t)
            t = []
    return C
r1 = int(1000)
c1 = int(1000)
r2 = int(1000)
c2 = int(1000)
matrix1 = [[random.randint(0, 10) for i in range(r1)] for j in range(c1)]
matrix2 = [[random.randint(0, 10) for k in range(r2)] for l in range(c2)]
if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map_async(pmatrix(matrix1,matrix2,r1,c1,r2,c2),matrix1)
    pool.close()
    pool.join()
    stop_time = default_timer()
    print(stop_time-start_time)