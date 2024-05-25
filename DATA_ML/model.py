import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Télécharger les stop words de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Simuler un dataset de feedbacks textuels en anglais
feedbacks = {
    'Feedback': [
        'Very good service', 'Poor organization', 'Excellent reception', 'Security issue', 
        'Quality accommodation', 'Ticket prices too high', 'Delayed transport', 'Theft during the event'
    ],
    'Label': ['positive', 'negative', 'positive', 'negative', 'positive', 'negative', 'negative', 'negative']
}

df_feedback = pd.DataFrame(feedbacks)

# Fonction de nettoyage des textes
def preprocess_text(text):
    # Convertir en minuscules
    text = text.lower()
    # Supprimer les ponctuations et les chiffres
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Tokeniser
    tokens = word_tokenize(text)
    # Supprimer les stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Rejoindre les tokens nettoyés en une seule chaîne
    cleaned_text = ' '.join(tokens)
    return cleaned_text

# Appliquer le prétraitement à chaque feedback
df_feedback['Cleaned_Feedback'] = df_feedback['Feedback'].apply(preprocess_text)
print(df_feedback.head())

# Initialiser le vectorizer TF-IDF
vectorizer = TfidfVectorizer()

# Vectoriser les textes prétraités
X = vectorizer.fit_transform(df_feedback['Cleaned_Feedback'])
y = df_feedback['Label']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser et entraîner le modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédire sur l'ensemble de test
y_pred = model.predict(X_test)

# Afficher le rapport de classification
print(classification_report(y_test, y_pred))
