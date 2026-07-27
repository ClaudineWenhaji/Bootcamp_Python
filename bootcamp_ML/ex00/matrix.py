class Matrix:
    def __init__(self, values):  # Matrix's Initialization

        if isinstance(values, tuple):
            rows, columns = values
            self.data = [[0.0 for _ in range(columns)] for _ in range(rows)]
        elif isinstance(values, list):

            if not values or not all(isinstance(row, list) for row in values):
                raise ValueError("Invalid Matrix")

            length_row = len(values[0])

            if any(len(row) != length_row for row in values):
                raise ValueError("Rows must have the same lentgh")

            self.data = values
        else:
            raise TypeError(" Matrix must be initialized with a list or a tuple")
        
        self.shape = (len(self.data), len(self.data[0]))

    

    def __add__(self, other):

        if not isinstance(other, Matrix):   # verify other is a matrix
            raise TypeError("Addition requires another matrix")

        if self.shape != other.shape: 
            raise ValueError("Matrices must have the same shape")

        result = []
        for i in range(self.shape[0]):
            ligne = []
            for j in range(self.shape[1]):
                somme = self.data[i][j] + other.data[i][j]
                ligne.append(somme)
            result.append(ligne)

        if isinstance(other, Vector):
            return Vector(result)
        return Matrix(result)


    def __radd__(self, other):  # right addition  
        return self.__add__(other)


    def __sub__(self, other):

        if not isinstance(other, Matrix):
            raise TypeError(" Substraction requires anoter matrix")
        
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape")

        result = []
        for i in range(self.shape[0]):
            ligne = []
            for j in range(self.shape[1]):
                subs = self.data[i][j] - other.data[i][j]
                ligne.append(subs)
            result.append(ligne)

        if isinstance(other, Vector):
            return Vector(result)
        return Matrix(result)


    def __rsub__(self, other):
        return other.__sub__(self)

    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Division only by scalar")

        result = []
        for row in self.data:
            new_row = []
            for value in row:
                new_row.append(value / scalar)
            result.append(new_row)

        if isinstance(self, Vector):
            return Vector(result)
        return Matrix(result)


    def __rtruediv__(self, scalar): # rigth division
        raise TypeError("Scalar / Matrix is impossible")

    def __mul__(self, other):

        # matrix multiplication with scalar
        if isinstance(other, (int, float)):
            result = []

            for row in self.data:
                new_row = []

                for value in row:
                    new_row.append(value * other)

                result.append(new_row)

            return Matrix(result)


        # matrix multiplication with vector or matrix

        if isinstance(other, Matrix):

            if self.shape[1] != other.shape[0]:
                raise ValueError("Incompatible shapes")

            result = []

            for i in range(self.shape[0]):
                new_row = []

                for j in range(other.shape[1]):
                    somme = 0

                    for k in range(self.shape[1]):
                        somme += self.data[i][k] * other.data[k][j]

                    new_row.append(somme)

                result.append(new_row)

            return Matrix(result)

        raise TypeError('Unsupported multiplication')


    def __rmul__(self, other):
        if isinstance(self, (int, float)):
            return self * other
        raise TypeError("Unsupported multiplication")


    def T(self):
        rows, columns = self.shape
        transposed = []

        for j in range(columns):
            new_row = []

            for i in range(rows):
                new_row.append(self.data[i][j])

            transposed.append(new_row)

        return Matrix(transposed)


    def __str__(self):  # nicely readable
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"



class Vector(Matrix):

    def __init__(self, values):
        super().__init__(values)

        rows, columns = self.shape
        if rows != 1 and columns != 1:
            raise ValueError("Vector must be a row or column vector")

    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Dot product requires a vector")

        if self.shape != v.shape:
            raise ValueError("Vectors must have the same shape")

        result = 0
        if self.shape[0] == 1: # vector ligne
            for i in range(self.shape[1]):
                result += self.data[0][i] * v.data[0][i]
        else:   # vector column
            for i in range(self.shape[0]):
                result += self.data[i][0] * v.data[i][0]
        return result





    

    
