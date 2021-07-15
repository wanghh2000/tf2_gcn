import numpy as np
from scipy.sparse.csr import csr_matrix

if __name__ == "__main__":
    # 所有值的行索引
    row = np.array([0, 0, 1, 2, 2, 2])
    # 所有值的列索引
    col = np.array([0, 2, 2, 0, 1, 2])
    # 所有非零数值
    data = np.array([1, 2, 3, 4, 5, 6]) 
    # 类似稀疏矩阵,输出得到的是矩阵中非0的行列坐标及值
    csr_maxtrix = csr_matrix((data, (row, col)), shape=(3, 3))
    print(csr_maxtrix)
    print('##############################################')
    maxtrix = csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
    print(type(maxtrix))
    print(maxtrix)
# array([[1, 0, 2],
#        [0, 0, 3],
#        [4, 5, 6]])