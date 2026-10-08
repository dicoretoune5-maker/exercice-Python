produit="clavier"
prix=19.90
quantite=3
taux_ava=0.2
#Calculer le total_ht puis total_ttc
total_ht = prix * quantite
total_ttc = total_ht + (total_ht * taux_ava)
print("Le total hors taxes est de : ", total_ht)