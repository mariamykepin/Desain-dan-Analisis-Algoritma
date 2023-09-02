print("Tukarlah posisi manggis dan pisang.")

x = 'manggis'
y = 'pisang' 

print("Sebelum ditukar posisi :")
print("Piring 1 : ", x)
print("Piring 2 : ", y)


def tukarPosisi(x, y):
    temp = x
    x = y
    y = temp
    return x, y

x, y = tukarPosisi(x, y)

print("Sesudah ditukar posisi:")
print("Piring 1 :", x)
print("Piring 2 :", y)
