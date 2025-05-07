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


Etape 3: ajouter les fichier et dossier a git (staging) avec :

git add .





Étape 4: Faire un commit
*************************

Créer un commit :Un commit est comme une "photo" de ton projet à un moment donné.
Chaque fois que tu effectues un commit, tu peux ajouter un message décrivant ce que tu as modifié.
Pour faire un commit, utilise la commande suivante :

git commit -m "Premier commit - Ajout des fichiers de base"

-m permet de spécifier un message pour ce commit.

Le message "Premier commit - Ajout des fichiers de base" est une description
de ce que tu as ajouté ou changé. C’est une bonne pratique d’écrire des messages
clairs et explicites pour te souvenir de chaque étape de ton projet.


Vérifier que ton commit est bien effectué :
*******************************************
Après avoir fait le commit, tu peux utiliser la commande suivante pour vérifier l'historique des commits :

****************************************************************************************


Étape 5 : Connecter ton projet local à GitHub
*********************************************
Maintenant que tu as effectué un commit local, nous allons connecter ton projet à GitHub, ce qui te permettra de pousser ton code sur la plateforme. Voici ce qu'il faut faire étape par étape :

1. Créer un dépôt sur GitHub
****************************
Si ce n’est pas encore fait, va sur GitHub et crée un nouveau dépôt :

Va sur GitHub.

Connecte-toi à ton compte.

Clique sur le bouton "New" pour créer un nouveau dépôt (repository).

Donne un nom à ton dépôt (par exemple, Churn-Project).

Assure-toi que l'option "Public" est sélectionnée.

Ne coche pas l'option pour ajouter un fichier README (tu l'as déjà fait localement).

Clique sur Create repository.

Une fois le dépôt créé, tu devrais voir une page avec des instructions pour connecter ton dépôt local à ce dépôt GitHub.


2. Ajouter l'URL de ton dépôt GitHub comme dépôt distant
********************************************************
Sur la page GitHub de ton dépôt, tu verras une URL, elle ressemblera à ceci :

https://github.com/ton-nom-utilisateur/ton-depot.git

Dans ton terminal PyCharm (dans ton projet local),
tu vas lier ton dépôt local à ce dépôt distant sur GitHub en utilisant la commande suivante :
************************************************************************************************
git remote add origin  https://github.com/naderkheloui/churn-project.git
Cette commande associe ton dépôt local avec le dépôt GitHub, via l'URL que tu viens de copier.






GENERATION TOKEN:
*****************


Méthode recommandée : via un Token GitHub (HTTPS)
Depuis août 2021, GitHub n’autorise plus l’usage du mot de passe classique, il faut utiliser un token d'accès personnel (PAT).

Voici comment faire :
Va sur https://github.com/settings/tokens.

Clique sur "Fine-grained tokens" ou "Personal access tokens".

Clique sur "Generate new token".

Coche les permissions nécessaires :

repo → pour les accès en lecture/écriture sur tes dépôts.

Garde le token précieusement (copie-le immédiatement, tu ne pourras plus le voir après).

Lorsqu’il te demande ton login/mot de passe dans le terminal :

Pour le login : entre ton nom d’utilisateur GitHub.

Pour le mot de passe : colle le token (ctrl+v ou clic droit coller dans le terminal).

🧠 Astuce :
Pour éviter d’avoir à retaper ton token à chaque fois, tu peux :

Configurer un gestionnaire de clés Git (git-credential-manager).

Ou utiliser SSH (méthode avancée, on pourra la voir plus tard).

Tu veux que je t’accompagne pour générer ton token maintenant ?







Vous avez dit :
oui stp


ChatGPT a dit :
Parfait ! Voici les étapes très simples pour générer un token GitHub et l’utiliser pour te connecter :

🔐 Étape 1 : Aller sur la page des tokens GitHub
Connecte-toi à GitHub : https://github.com

Va sur : https://github.com/settings/tokens

Clique sur "Generate new token" → Choisis "Fine-grained token" (le plus sécurisé)
👉 Ou sinon, clique sur "Generate new token (classic)" si l’autre n’est pas disponible.

📝 Étape 2 : Créer le token
Nom du token : par exemple token-git-local

Expiration : choisis 90 days ou No expiration

Repository access : choisis "Only select repositories" → coche ton dépôt ou "All repositories"

Permissions :

Section Repository : coche "Contents - Read and write"

Clique sur "Generate token"

✅ Tu vas obtenir un long code → quelque chose comme :

nginx
Copier
Modifier
ghp_9aP01234EXEMPLEabcdeTOKEN12345678
⚠️ Copie-le tout de suite et garde-le de côté (bloc-notes par exemple). Tu ne pourras plus le revoir après.

💡 Étape 3 : L'utiliser pour te connecter depuis Git
Retourne dans ton terminal PyCharm

Tape la commande suivante (si ce n’est pas déjà fait) :

bash
Copier
Modifier
git push -u origin main
Il te demandera :

Username → entre ton nom GitHub (ex: tonpseudo)

Password → colle le token (clic droit ou Ctrl + V)




3. Pousser (push) ton commit local vers GitHub
**********************************************
Maintenant que ton dépôt local est lié à GitHub, tu peux envoyer (pousser) ton commit local vers GitHub avec la commande suivante :

git push -u origin master






*********************************************************************************
*********************************************************************************

 Étape 1 : Cloner ton dépôt (comme un autre utilisateur)
📌 Objectif :
Simuler un nouveau collaborateur qui récupère ton projet depuis GitHub.

✅ Étapes à suivre :
Crée un nouveau dossier sur ton ordinateur (ex. : Churn_clone)

Ouvre PyCharm et dans le menu, choisis :

Get from VCS (VCS = Version Control System) ou Clone repository


Étape suivante : Créer une branche (bonne pratique)
Pourquoi ?
Quand on travaille à plusieurs ou sur une nouvelle fonctionnalité, on ne modifie pas directement la branche master (ou main).
On crée une branche séparée pour y faire ses changements


Étape 2 : Créer une branche et passer dessus
********************************************
Dans ton terminal PyCharm (dans le dossier du projet cloné), tape :

git checkout -b ma-nouvelle-branche

Tu peux remplacer ma-nouvelle-branche par un nom plus parlant, comme ajout-predict-route ou fix-tests.

Cette commande fait deux choses :

1) Elle crée une nouvelle branche.

2) Elle te positionne dessus automatiquement.





**********************************************************************************
**********************************************************************************

Étape 3 : Modifier le code
**************************

Tu peux maintenant :

faire une petite modification dans ton projet (par exemple modifier un commentaire, ou améliorer un fichier)

puis sauvegarder ton fichier comme d’habitude dans PyCharm

Ensuite, dans le terminal :

git status

Cette commande te montre les fichiers modifiés.





Étape 4 : Ajouter les fichiers au staging (préparer le commit)
**************************************************************

Tape la commande suivante pour ajouter toutes les modifications au staging area :

git add . pour ajouter tout
git add chemin depuis dossier vers fichier modifié: git add API/app.py



Étape 5 : Faire un commit
*************************


Un commit est un instantané de ton projet à un moment donné. C’est comme dire : "Voici une étape importante ou une modification que je veux enregistrer".

Fais ton premier commit avec un message clair :

git commit -m "Ajout initial du projet Churn"





Étape 6 : Lier ton dépôt local à GitHub
***************************************

A. Qu'est-ce que ça signifie ?
------------------------------
Quand tu clones un projet depuis GitHub, PyCharm configure déjà pour toi le lien entre ton dépôt local et le dépôt distant sur GitHub. Cela permet de pousser (push) tes changements de ton projet local vers GitHub et inversement.

Par défaut, quand tu clones un projet, Git associe l’URL GitHub à un alias origin. Tu n’as donc pas besoin de refaire cette étape si tu as cloné ton projet depuis GitHub. Cependant, si tu n'as pas cloné le projet mais que tu veux le lier manuellement à un dépôt GitHub, tu devras utiliser la commande git remote add origin.

B. Vérifier si tu as déjà un dépôt distant lié
----------------------------------------------
Pour savoir si ton dépôt local est déjà lié à un dépôt distant sur GitHub, tu peux utiliser cette commande dans le terminal de PyCharm :


git remote -v


Si tu vois des liens (comme https://github.com/ton-utilisateur/ton-projet.git), cela signifie que ton dépôt est déjà lié à GitHub.

Sinon, tu verras rien ou un message d'erreur.


C. Si tu n’as pas encore lié ton dépôt à GitHub
-----------------------------------------------
Si tu vois qu’il n’est pas lié à un dépôt distant (en vérifiant avec git remote -v), tu peux le faire en ajoutant le dépôt GitHub avec cette commande :

Ajoute un dépôt distant avec l'URL GitHub :

git remote add origin https://github.com/ton-utilisateur/ton-projet.git

👉 Remplace ton-utilisateur par ton nom d'utilisateur GitHub et ton-projet par le nom de ton dépôt.




D. Vérifier la liaison avec GitHub
----------------------------------

Une fois la commande exécutée, tu peux vérifier que le dépôt distant est bien ajouté avec :

git remote -v

Cela devrait te renvoyer quelque chose comme ça :

origin  https://github.com/ton-utilisateur/ton-projet.git (fetch)
origin  https://github.com/ton-utilisateur/ton-projet.git (push)







******************************************************************************
******************************************************************************

Étape 7 : Pousser ta branche locale vers GitHub
***********************************************

Maintenant que ton dépôt local est lié à GitHub, il est temps de pousser ta branche branche-nadir vers GitHub.

Pousser la branche vers GitHub :

Comme tu as créé une branche branche-nadir sur ton dépôt local, tu veux l'envoyer sur GitHub pour qu'elle soit accessible à d'autres personnes (ou pour la sauvegarder sur le cloud).

Utilise cette commande pour pousser ta branche branche-nadir :

git push -u origin branche-nadir


origin est le nom du dépôt distant (GitHub dans ce cas).

branche-nadir est la branche que tu veux pousser.

La première fois que tu pousses une branche, tu dois utiliser -u pour dire à Git de lier cette branche locale à la branche distante sur GitHub.

Après avoir exécuté cette commande, tu devrais voir un message du type :

To https://github.com/ton-utilisateur/ton-depot.git
 * [new branch]      branche-nadir -> branche-nadir




******************************************************************************
******************************************************************************
Étape 8 : Vérifier sur GitHub
*****************************

Rends-toi sur GitHub et vérifie si ta branche branche-nadir est bien visible dans l'onglet Branches de ton dépôt.

Si tu vois ta branche sur GitHub, cela signifie que tout s'est bien passé !

Tu as maintenant réussi à pousser ta branche sur GitHub et elle est sauvegardée à distance.









******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************


C’est quoi une Pull Request ?
******************************

Une Pull Request (PR), c’est une demande de fusion de code que tu as modifié sur une branche (par exemple branche-nadir) vers une autre branche (souvent main ou master).

C’est un peu comme dire à ton équipe (ou à toi-même si tu es seul) :

“Hé, j’ai fini mes changements ici, est-ce qu’on peut les ajouter dans le projet principal ?”


👀 C’est quoi une Revue de Code ?
**********************************

Avant d’accepter cette demande (la PR), quelqu’un peut :

Lire le code modifié,

Vérifier qu’il fonctionne bien,

Suggérer des améliorations,

Ou détecter des erreurs potentielles.

C’est ce qu’on appelle une revue de code (code review).

Même si tu es seul, cette étape t’aide à bien relire ton propre code avant de le fusionner.



C’est quoi une Fusion ?
***********************
Une fois que tout est validé, on fusionne (merge) la branche dans le projet principal (main/master). Le code de ta branche devient alors officiellement une partie du projet principal.

🔁 En résumé :
***************
   Terme	                 Description
Pull Request	   Demande de fusion de ton code (branche → main)
Revue de Code	   Vérification du code avant la fusion
Fusion (Merge)	   Intégration du code dans le projet principal

Souvent utilisé dans un travail d’équipe, mais très utile même en solo, car ça t’oblige à structurer tes étapes : coder → tester → valider → intégrer.









******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
************************ COLLABORATION EQUIPE  *******************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************
******************************************************************************




Étape 8 : Créer une Pull Request (PR)
*************************************
1) Va sur GitHub dans ton dépôt.

2) Tu devrais voir un bandeau violet ou jaune en haut qui dit :

	“branche-nadir had recent pushes...”
	Et un bouton : Compare & pull request
	➤ Clique dessus.

      Si tu ne vois pas ce bandeau, pas de panique :

	Clique sur le menu "Pull requests"

	Puis clique sur "New pull request"

	Sélectionne :

		base = master

		compare = branche-nadir

3) Tu arrives sur la page de création de PR :

	Mets un titre clair : Ajout des fonctions d'authentification

	Dans la description, explique brièvement ce que tu as changé.

	Clique sur Create pull request


📝 C’est à cette étape qu’en équipe, un collègue lirait ton code et ferait une review (relecture).







Étape 9 : Fusionner la Pull Request (PR)
****************************************
Maintenant que ta Pull Request est créée, on va fusionner (merge) ton travail dans la branche principale master.

👉 Étapes pour fusionner :
	1. Toujours sur GitHub, dans ta Pull Request, tu devrais voir un bouton “Merge pull request”.

	2. Clique dessus.

	3. Puis clique sur “Confirm merge”.


🎉 Bravo ! Ton code est maintenant intégré dans la branche principale (master).
Ta branche branche-nadir existe toujours, mais le travail est désormais fusionné.




Étape 9 : Récupérer les dernières modifications de master (si on est un autre utilisateur)
*******************************************************************************************

Quand quelqu’un fusionne une PR dans master, les autres doivent mettre à jour leur copie locale pour rester à jour.

👉 Commandes à exécuter :
	git checkout master          # Revenir sur la branche master
	git pull origin master       # Récupérer les derniers changements de GitHub

Cela t’assure de travailler sur la dernière version du projet.
