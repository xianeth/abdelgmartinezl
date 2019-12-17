Dicc_espanol_ingles = { "casa" : "house", "carro" : "car","libro": "book","celular":"cellphone","cartera":"wallet"}

print("\n Elige cualquiera de las palabras en  la lista a traducir a ingles:")
Palabras = ["casa","carro","libro","celular","cartera"]
print(Palabras)

entrada = input ("\n Ingrese la palabra que desea traducir a ingles:")

if entrada == Palabras [0]: print ("\n  casa traducido a ingles es:", Dicc_espanol_ingles.get("casa"))
elif entrada == Palabras [1]: print ("\n carro traducido a ingles es:", Dicc_espanol_ingles.get("carro"))
elif entrada == Palabras [2]: print ("\n  libro traducido a ingles es:", Dicc_espanol_ingles.get("libro"))
elif entrada == Palabras [3]: print ("\n celular traducido a ingles es:", Dicc_espanol_ingles.get("celular"))
elif entrada == Palabras [4]: print ("\n cartera  traducido a ingles es:", Dicc_espanol_ingles.get("cartera"))

else: print("\n Esta palabra aun no esta disponible")