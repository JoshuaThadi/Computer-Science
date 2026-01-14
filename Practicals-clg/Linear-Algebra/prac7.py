# find the orthogonal projection of vector a on b

import numpy as np
def oprojection(of_vec, on_vec):
    x1 = np.array(of_vec)
    x2 = np.array(on_vec)
    print(f"1st Vector a = {x1}")
    print(f"2nd vector b = {x2}")
    scale = np.dot(x2, x1)/np.dot(x2, x2)
    vec = scale * x2
    print("Projection of a on b = ", vec)
print(oprojection([2, 4],[8, 6]))
