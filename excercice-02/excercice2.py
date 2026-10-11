temperature = float(input("Entrez la température: "))
if temperature < -3:
    print("gel")
elif temperature < 0:
    print("froid!")
elif temperature < 15:
    print("doux")
else: 
    print("chaud")
    # un année bissextile est divisible par 4 mais pas par 100, sauf si elle est divisible par 400
annee = int(input("Entrez une année: "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(annee, "est une année bissextile.")
