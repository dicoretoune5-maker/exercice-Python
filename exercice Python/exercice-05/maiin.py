from outils import convertir_note, moyenne, mention
notes_brutes = ["12,5", "15", "abc", "9", "18,25"]
notes_valides = []
nb_ignorees = 0
for element in notes_brutes:
    valeur = convertir_note(element)
    if valeur is not None:
        notes_valides.append(valeur)
    else:
        nb_ignorees += 1

moy = moyenne(notes_valides)
mention_finale = mention(moy)
print(f"Notes ignorées : {nb_ignorees}")
print(f"Moyenne : {moy:.2f}")
print(f"Mention : {mention_finale}")