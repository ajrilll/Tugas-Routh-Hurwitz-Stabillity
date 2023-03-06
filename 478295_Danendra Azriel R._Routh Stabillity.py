import numpy as np

polynomial = input("Masukkan koefisien dari persamaan polinomial dipisah dengan spasi: ")
p = np.array(polynomial.split(), dtype=float)

def routh_hurwitz(p):
    n = len(p)
    rh = np.zeros((n, (n+1)//2))

    rh[0, :] = p[::2]
    rh[1, :] = p[1::2]

    for i in range(2, n):
        for j in range((n+1)//2):
            if j == 0:
                rh[i, j] = -1/rh[i-1, j] * np.linalg.det([[rh[i-1, j+1], p[i-1]], [rh[i-2, j], p[i-2]]])
            else:
                rh[i, j] = -1/rh[i-1, j] * np.linalg.det([[rh[i-1, j], rh[i-1, j-1]], [rh[i-2, j], rh[i-2, j-1]]])

    return rh

print("\nPersamaan polinomial: ")
print()
print(np.poly1d(p))
print("\nTable Routh-Hurwitz: ")
rh_table = routh_hurwitz(p)
print(rh_table)

K = float(input("\nMasukkan nilai K: "))

if np.all(rh_table[:, 0] > 0):
    print("\nSistem stabil.")
    print("Kutub loop tertutup terletak di setengah kiri bidang-s.")
    print("Sistem stabil asimtotik jika K > 0.")
elif np.all(np.sign(rh_table[:, 0]) == np.sign(rh_table[0, 0])):
    print("\nSistem tidak stabil.")
    print("Kutub loop tertutup terletak di bagian kanan bidang-s.")
    print("Sistem tidak stabil untuk semua nilai K.")
else:
    print("\nSistem sedikit stabil.")
    print("Kutub loop tertutup terletak pada sumbu imajiner.")
    print("Sistem stabil asimtotik untuk K > 0 dan tidak stabil untuk K < 0.")
