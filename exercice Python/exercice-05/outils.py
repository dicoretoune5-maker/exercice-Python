def convertir_note(texte):
    try:
        # Remplace la virgule décimale par un point pour Python (ex: "12,5" -> "12.5")
        texte_propre = texte.replace(",", ".")
        return float(texte_propre)
    except (ValueError, AttributeError):
        # Si le texte n'est pas un nombre (ex: "abc"), on renvoie None
        return None


def moyenne(valeurs):
    if not valeurs:
        return 0
    return sum(valeurs) / len(valeurs)


def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    return "Insuffisant"