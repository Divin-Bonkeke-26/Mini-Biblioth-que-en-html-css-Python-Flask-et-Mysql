# Mini Bibliothèque — HTML/CSS + Flask + MySQL

Description
Une petite application web pour gérer une bibliothèque : ajout et consultation de livres, interface frontend en HTML/CSS et backend en Python (Flask) avec une base MySQL.

Stack
- Frontend : HTML, CSS
- Backend : Python 3 + Flask
- Base de données : MySQL

Prérequis
- Python 3.8+
- MySQL
- (Optionnel) virtualenv

Installation
1. Cloner :
   git clone https://github.com/Divin-Bonkeke-26/Mini-Biblioth-que-en-html-css-Python-Flask-et-Mysql.git
2. Se placer dans le dossier du projet :
   cd Mini-Biblioth-que-en-html-css-Python-Flask-et-Mysql
3. Créer et activer un environnement virtuel :
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate   # Windows
4. Installer les dépendances (si `requirements.txt` est présent) :
   pip install -r requirements.txt
5. Configurer la connexion MySQL (fichier de configuration ou variables d'environnement).
6. Lancer l'application :
   flask run
   (ou `python app.py` si l'entrypoint est `app.py`)

Notes
- Ajoute un fichier `.env` pour stocker les variables sensibles (DB_USER, DB_PASS, etc.).
- Vérifie l'orthographe et l'encodage si les fichiers contiennent des accents.

Contribuer
- Ouvre une issue pour discuter d'une fonctionnalité.
- Crée une branche `feature/xxx` et soumets une pull request.
