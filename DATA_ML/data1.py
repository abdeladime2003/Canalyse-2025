import pandas as pd
import numpy as np

problems = ['Health', 'Transport', 'Housing', 'Logistics', 'Communication','Security']
sub_problems = {
    "Health": [
        "Lack of essential medications",
        "Long queues for consultations",
        "Limited access to specialized care",
        "Other"
    ],
    "Transport": [
        "Lack of connection between different modes of transport",
        "Insufficient security conditions in public transport",
        "Limited accessibility for people with reduced mobility",
        "Other"
    ],
    "Housing": [
        "Lack of accessibility for people with disabilities",
        "Poor customer service in accommodation establishments",
        "Hygiene and cleanliness issues in housing",
        "Other"
    ],
    "Logistics": [
        "Lack of adequate signage for tourists",
        "Shortage of qualified tourist guides",
        "Difficulties related to luggage transport",
        "Other"
    ],
    "Communication": [
        "Lack of reliable internet connections in certain regions",
        "Communication difficulties with emergency services",
        "Translation problems in official documents",
        "Other"
    ],
    "Security" :["Cybersecurity Concerns","Physical Security Risks","Health and Safety Concerns","Other"]
}

number_tourists = 100000

age = np.random.randint(18, 70, size=number_tourists)
nationality = np.random.choice(['Morocco', 'Algeria', 'Tunisia', 'Libya', 'Egypt', 'Mauritania', 'Senegal', 'Mali', 'Niger', 'Chad', 'Sudan', 'Eritrea', 'Djibouti', 'Somalia', 'Gambia', 'Guinea-Bissau', 'Guinea', 'Sierra Leone', 'Liberia', 'Cote d''Ivoire', 'Burkina Faso', 'Ghana', 'Togo', 'Benin', 'Nigeria', 'Cameroon', 'Tanzania', 'Kenya', 'Uganda', 'Rwanda', 'Burundi', 'Seychelles', 'Mauritius', 'Comoros', 'Madagascar', 'Zambia', 'Zimbabwe', 'Malawi', 'Botswana', 'Namibia', 'Angola', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Gabon', 'Equatorial Guinea'], p=[0.26, 0.2, 0.12, 0.1, 0.09, 0.02, 0.04, 0.03, 0.02, 0.01, 0.0055, 0.003, 0.019, 0.005, 0.005, 0.0025, 0.002, 0.0021, 0.0022, 0.002, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0019, 0.0025, 0.0023, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025 , 0.0025, 0.0025, 0.0025], size=number_tourists)

# Sex distribution
sex = np.random.choice(['Male', 'Female'], size=number_tourists, p=[0.6, 0.4])
residence_location = np.random.choice(['Agadir', 'Casablanca', 'Marrakech', 'Fes', 'Tangier', 'Rabat','Other'],p=[0.15,0.25,0.2,0.06,0.07,0.23,0.04],size=number_tourists)

# Modify probabilities to skew the distribution of problems and sub-problems
encountered_problems = np.random.choice(problems, size=number_tourists, p=[0.30, 0.25, 0.2, 0.08, 0.09,0.08])
encountered_sub_problems = []
for problem in encountered_problems:
    encountered_sub_problems.append(np.random.choice(sub_problems[problem]))

data = {
    'Age': age,
    'Nationality': nationality,
    'Sex': sex,
    'Residence Location': residence_location,
    'General Problem': encountered_problems,
    'Specific Sub-Problem': encountered_sub_problems
}

df = pd.DataFrame(data)
df.to_csv(r"DATA_ML\data.csv", index=False)
