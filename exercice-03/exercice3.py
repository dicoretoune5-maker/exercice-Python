from matplotlib.pylab import append


temperatures = [12.5,14,9.5,17,21,19.5, 11]
# 01. Afficher la moyenne arrondie à 2 décimales, le maximum et le minimum de la liste
moyenne = round(sum(temperatures) / len(temperatures), 2)
maximum = max(temperatures)
minimum = min(temperatures)

print("Moyenne:", moyenne)
print("Maximum:", maximum)
print("Minimum:", minimum)
# 02. Compter avec une boucle les jours au dessus de 15 degrés 
jours_au_dessus_de_15 = 0

for temperature in temperatures:
    if temperature > 15:
        jours_au_dessus_de_15 += 1

print("Nombre de jours au dessus de 15 degrés:", jours_au_dessus_de_15)
# 03. Construire la liste un fahrenheit : f=C * 9/5 + 32
fahrenheit = []
for c in temperatures:
    f = c * 9/5 + 32
    fahrenheit.append(f)
print(fahrenheit)
