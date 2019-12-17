import re

nombre = "Ángela nañez"

str = nombre

reg = re.findall("[Áñ]", str)

print(reg)

if (reg):
  print(" Se encuentran las coincidencias Á y ñ ")
else:
  print("No hay coincidencias")


