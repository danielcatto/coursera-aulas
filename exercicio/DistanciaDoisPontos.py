import math
xa = float(input("Primeiro ponto para X: "))
ya = float(input("Segundo ponto para Y: "))

xb = float(input("Primeiro ponto para X: "))
yb = float(input("Segundo ponto para Y: "))




if (xa < ya and yb < yb):
   x = xa - xa
   y = yb - yb
else:
   x = xb - xa
   y = yb - ya

xy = (x**2) + (y**2)
d = math.sqrt(xy)

if (d >10):
   print("longe,")
else:
   print("perto")
