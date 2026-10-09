ventes = [
    {"produit": "café", "prix": 2.5, "quantité": 120},
    {"produit": "thé", "prix": 2.0, "quantité": 80},
    {"produit": "chocolat", "prix": 3.5, "quantité": 45}
]
# 01. construire un dictionnaire par produit ver prix * quantité
ca_par_produit = {
    vente["produit"]: vente["prix"] * vente["quantité"]
    for vente in ventes
}
print("chiffre d'affaires par produit:", ca_par_produit)
# calculer le chiffre d'affaires total
total_ca = sum(ca_par_produit.values())
print("chiffre d'affaires total:", total_ca)
# 03.Trouver le produit qui rapporte le plus
produit_plus_rentable = max(ca_par_produit, key=ca_par_produit.get)
print("Le produit le plus rentable est:", produit_plus_rentable, "avec un chiffre d'affaires de", ca_par_produit[produit_plus_rentable])