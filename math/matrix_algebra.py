# Matrix Algebra

import numpy as np
from scipy.linalg import expm
# Do not change these variables
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work

dimensions = {
    'A': np.shape(A),
    'B': np.shape(B),
    'C': np.shape(C),
    'D': np.shape(D),
    'u': np.shape(u),
    'v': np.shape(v)
}

# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6

u_plus_v = u+v            # u+v
u_minus_v = u-v           # u-v
alpha_times_u = alpha * u       # alpha * u, alpha = 6
u_dot_v = np.dot(u,v)             # u . v
norm_u = np.linalg.norm(u)              # ||u|| 


# Q3: compute the following and assign to variables below:
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
try:
    A_plus_C = A + C            # A + C    
except ValueError:
    A_plus_C = None

try:
    A_minus_Ctranspose = A - np.transpose(C)   # A - C.T
except ValueError:
    A_minus_Ctranspose = None

try:    
    Ctranspose_plus_3D = np.transpose(C) + 3*D   # C.T + 3*D
except ValueError:
    Ctranspose_plus_3D = None
    
try:
    B_times_A = B * A             # B*A
except ValueError:
    B_times_A = None

try:
    B_times_Atranspose = B * np.transpose(A)   # B*A.T
except ValueError:
    B_times_Atranspose = None

    # Q4: (bonus)
try: 
    B_times_C = B*C            # B*C
except ValueError:
    B_times_C = None

try: 
    C_times_B = C*B            # C*B
except ValueError:
    C_times_B = None

try:
    B_exp_4 = expm(B,4)     # B^4
except ValueError:
    B_exp_4 = None
    
try:
    A_times_Atranspose = A*np.transpose(A)    # A*A.T
except ValueError:
    A_times_Atranspose = None

try:
    Dtranspose_times_D = np.transpose(D) *D   # D.T*D
except ValueError:
    Dtranspose_times_D = None
