import pandas as pd
import numpy as np

problemes = ['Santé', 'Transport', 'Hébergement', 'Logistique', 'Communication']
sous_problemes = {
    "Santé": [
        "Manque de médicaments essentiels",
        "Longues files d'attente pour les consultations",
        "Accès limité aux soins spécialisés",
        "Autre"
    ],
    "Transport": [
        "Manque de connexion entre les différents modes de transport",
        "Conditions de sécurité insuffisantes dans les transports publics",
        "Accessibilité limitée pour les personnes à mobilité réduite",
        "Autre"
    ],
    "Hébergement": [
        "Manque d'accessibilité pour les personnes handicapées",
        "Services clientèle médiocres dans les établissements d'hébergement",
        "Problèmes d'hygiène et de propreté dans les logements",
        "Autre"
    ],
    "Logistique": [
        "Absence de signalisation adéquate pour les touristes",
        "Manque de guides touristiques qualifiés",
        "Difficultés liées au transport des bagages",
        "Autre"
    ],
    "Communication": [
        "Manque de connexions internet fiables dans certaines régions",
        "Difficultés de communication avec les services d'urgence",
        "Problèmes de traduction dans les documents officiels",
        "Autre"
    ]
}

nombre_touristes = 100000

age = np.random.randint(18, 70, size=nombre_touristes)
nationalite = np.random.choice(['Maroc', 'Algérie', 'Tunisie', 'Libye', 'Égypte', 'Mauritanie', 'Sénégal', 'Mali', 'Niger', 'Tchad', 'Soudan', 'Érythrée', 'Djibouti', 'Somalie', 'Gambie', 'Guinée-Bissau', 'Guinée', 'Sierra Leone', 'Libéria', 'Côte d\'Ivoire', 'Burkina Faso', 'Ghana', 'Togo', 'Bénin', 'Nigeria', 'Cameroun', 'Tanzanie', 'Kenya', 'Ouganda', 'Rwanda', 'Burundi', 'Seychelles', 'Maurice', 'Comores', 'Madagascar', 'Zambie', 'Zimbabwe', 'Malawi', 'Botswana', 'Namibie', 'Angola', 'République démocratique du Congo', 'République du Congo', 'Gabon', 'Guinée équatoriale'], p=[0.26, 0.2, 0.12, 0.1, 0.09, 0.02, 0.04, 0.03, 0.02, 0.01, 0.0055, 0.003, 0.019, 0.005, 0.005, 0.0025, 0.002, 0.0021, 0.0022, 0.002, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0019, 0.0025, 0.0023, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025 , 0.0025, 0.0025], size=nombre_touristes)
# Répartition des sexes
sexe = np.random.choice(['Homme', 'Femme'], size=nombre_touristes, p=[0.6, 0.4])
lieu_residence = np.random.choice(['Agadir', 'Casablanca', 'Marrakech', 'Fes', 'Tanger', 'Rabat','Autre'],p=[0.15,0.25,0.2,0.06,0.07,0.23,0.04],size=nombre_touristes)

# Modifiez les probabilités pour déséquilibrer la répartition des problèmes et sous-problèmes
problemes_rencontres = np.random.choice(problemes, size=nombre_touristes, p=[0.35, 0.25, 0.2, 0.1, 0.1])
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
df.to_csv(r"tec\data.csv", index=False)
