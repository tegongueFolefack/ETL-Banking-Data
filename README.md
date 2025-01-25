# Banks ETL Project

## Description
Ce projet réalise un processus ETL (Extract, Transform, Load) pour récupérer des données des plus grandes banques, les transformer selon des taux de change, et les charger dans une base de données SQLite. Il utilise les bibliothèques Python comme `pandas`, `sqlite3` et `BeautifulSoup`.

## Fonctionnalités
1. Extraction des données depuis une page Wikipédia sur les plus grandes banques.
2. Transformation des données avec conversion des valeurs en différentes devises (GBP, EUR, INR).
3. Chargement des données dans un fichier CSV et une base de données SQLite.
4. Exécution de requêtes pour des bureaux situés dans différents pays (Londres, Berlin, New Delhi).

---

## Prérequis
- Python 3.8 ou supérieur
- Les bibliothèques Python suivantes :
  - `pandas`
  - `sqlite3` (intégré à Python)
  - `beautifulsoup4`
  - `requests`

Pour installer les dépendances, exécute :
```bash
pip install pandas beautifulsoup4 requests
```

---

## Installation et Configuration
1. Clone ce dépôt Git :
   ```bash
   git clone <URL_DU_DEPOT>
   cd banks-etl-project
   ```

2. Télécharge le fichier `exchange_rate.csv` :
   ```bash
   wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
   ```
   Place-le dans le même dossier que `banks_project.py`.

---

## Exécution du projet
1. Assure-toi que tous les fichiers nécessaires sont dans le même dossier :
   - `banks_project.py`
   - `exchange_rate.csv`

2. Exécute le script :
   ```bash
   python3 banks_project.py
   ```

3. Résultats :
   - Un fichier CSV `Largest_banks_data.csv` sera généré dans le dossier actuel.
   - Une base de données SQLite `Banks.db` sera créée.
   - Les résultats des requêtes seront affichés dans la console.

---

## Étapes ETL détaillées
### 1. Extraction
Le script récupère les 10 plus grandes banques depuis cette page :  
[Archive Wikipedia](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)

### 2. Transformation
Les données sont enrichies avec des conversions de marché en devises :
- GBP (Livre Sterling)
- EUR (Euro)
- INR (Roupie Indienne)

### 3. Chargement
Les données transformées sont :
- Enregistrées dans un fichier CSV (`Largest_banks_data.csv`).
- Chargées dans une base de données SQLite (`Banks.db`).

### 4. Requêtes
Des requêtes SQL récupèrent les données pour des bureaux situés dans différents pays :
- Londres (GBP)
- Berlin (EUR)
- New Delhi (INR)

---

## Structure du projet
```
banks-etl-project/
├── banks_project.py        # Script principal
├── exchange_rate.csv       # Taux de change
├── Largest_banks_data.csv  # Fichier CSV généré après exécution
├── Banks.db                # Base de données SQLite générée
├── code_log.txt            # Journal des opérations
└── README.md               # Documentation
```

---

## Journalisation
Toutes les étapes du processus ETL sont journalisées dans un fichier `code_log.txt`.

---

## Contribution
1. Fork ce projet.
2. Crée une branche avec un nouveau correctif ou une nouvelle fonctionnalité :
   ```bash
   git checkout -b ma-fonctionnalite
   ```
3. Commit tes modifications :
   ```bash
   git commit -m "Ajout de ma fonctionnalité"
   ```
4. Pousse tes modifications :
   ```bash
   git push origin ma-fonctionnalite
   ```
5. Crée une pull request sur ce dépôt.

---

## Licence
Ce projet est sous licence MIT. Tu peux l'utiliser librement.

---

