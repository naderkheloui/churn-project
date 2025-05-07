ÉTAPE 1 : Initialiser Git dans ton projet local

Dans ton terminal PyCharm (vérifie bien que tu es dans le dossier racine de ton projet Churn), tape :
git init

Cette commande va créer un dépôt Git local (un dossier .git caché) dans le projet.





ÉTAPE 2 : Ajouter ton fichier .gitignore
******************************************
Le fichier .gitignore permet de spécifier les fichiers et dossiers que Git doit ignorer, comme par exemple des fichiers temporaires, des fichiers de configuration ou des fichiers générés qui ne doivent pas être suivis par Git.

Crée un fichier .gitignore à la racine de ton projet (si tu ne l'as pas déjà).

Ajoute des règles de base dans ce fichier (tu peux le remplir avec les éléments suivants) :


/////
# Fichiers de configuration IDE
.idea/

# Environnement virtuel
.venv/

# Fichiers générés par Python
__pycache__/
*.pyc

# Fichiers de logs
*.log

# D'autres fichiers spécifiques à ton projet
/////

Pour vérifier que ton fichier .gitignore fonctionne bien, tape la commande suivante dans le terminal :
git status


Etape 3:

ajouter les fichier et dossier a git avec : git add .