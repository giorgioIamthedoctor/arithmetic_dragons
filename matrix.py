
class Matrix:
    mat = []
    newmat = []
    sumdet = 0
    def __init__(self,m,n = None):
        if n == None:
            self.mat = m
        else:
            self.mat = [[0 for k in range(n)] for l in range(m)]
            self.newmat = self.mat[:]
            print(self.mat)
    def  __add__(self, other):
        for k in range(len(self.mat)-1):
            for l in range(len(self.mat[k])-1):
                self.newmat[k][l] = self.mat[k][l] + other.mat[k][l]
        return self.newmat
    def set(self,i,j,value):
        try:
            self.mat[i][j] = value
        except:
            print("Что-то пошло не так")
    def razdel(self,matr):
        for i in range(len(matr[0])-1):
            for l in range(1,len(matr)-1):
                matr[i + 1][l] *= matr[i][0] * ((-1) ** i)
            self.determ(matr[0:i][i+1:] + matr[i+1:][i+1:])
    def determ(self,matrixx):
        if len(matrixx) != 2:
            self.determ(self.razdel(matrixx))
        else:
            self.sumdet += matrixx[0][0]*matrixx[1][1] - matrixx[0][1]*matrixx[1][0]
    def __eq__(self, other):
        return self.mat == other
    def get(self,i,j):
        return self.mat[i][j]
    def determinant(self):
        self.determ(self.mat)