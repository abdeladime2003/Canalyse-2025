import pandas as pd # type: ignore
import numpy as np # type: ignore
problemes = ['Santé', 'Transport', 'Hébergement', 'Logistique', 'Communication']
sous_problemes = {
    'Santé': ['Manque de personnel', 'Coûts élevés des soins médicaux','Manque d\'équipements médicaux adéquats', 'Autre'],
    'Transport': ['Offres de transport insuffisantes', 'Coûts élevés des transports', 'Retard de transport', 'Autre'],
    'Hébergement': ['Problème de qualité de l\'hôtel', 'Coûts élevés', 'Autre'],
    'Logistique': ['Difficultés de restauration', 'Problèmes de sécurité', 'Insuffisance des infrastructures touristiques', 'Autre'],
    'Communication': ['Barrière linguistique', 'Difficulté à obtenir des informations', 'Autre']
}

nombre_touristes = 100000

age = np.random.randint(18, 70, size=nombre_touristes)
nationalite = np.random.choice(['France', 'Allemagne', 'Espagne', 'Italie', 'États-Unis', 'Royaume-Uni', 'Chine', 'Japon', 'Canada', 'Brésil'], size=nombre_touristes)
sexe = np.random.choice(['Homme', 'Femme'], size=nombre_touristes)
lieu_residence = np.random.choice(['Agadir', 'Casablanca', 'Marrakech', 'Fes', 'Tanger', 'Rabat','Autre'], size=nombre_touristes)

problemes_rencontres = np.random.choice(problemes, size=nombre_touristes)

sous_problemes_rencontres = []
for probleme in problemes_rencontres:
    sous_problemes_rencontres.append(np.random.choice(sous_problemes[probleme]))

data = {
    'Age': age,
    'Nationalité': nationalite,
    'Sexe': sexe,
    'Lieu de résidence': lieu_residence,
    'Problème général': problemes_rencontres,
    'Sous-problème spécifique': sous_problemes_rencontres
}

df = pd.DataFrame(data)
df.to_csv("./data.csv")