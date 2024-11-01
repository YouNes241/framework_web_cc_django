# Devoir FW1-CC1-20

## Description
Ce dépôt contient les réponses aux questions du devoir de Framework Web 1 de la L3 Informatique de l'Université d'Orléans. Le contrôle porte sur le framework Django.


## Membres du groupe

***Nicolas Paul***  
***Lucas Paulo***  
***Ali Mohamad***  
***Younes Ouaammou***

## Lancement de l'environement Docker
Avant de commencer le projet en Django , on doit lancer l'environement de développement avec Docker. On execute la commande suivante : 
```bash
USERNAME=$(id -un) USERID=$(id -u) docker-compose up -d
```
## Réponses aux questions

### Question 1
On commence par créer un projet Django `cc` , et une application `collec_management` :
```bash
django-admin startproject cc
python manage.py startapp collec_management
```

### Question 2 
Commande pour lancer le serveur :
```bash
python manage.py runserver 0.0.0.0:8000&
```

### Question 3
```bash
python manage.py makemigrations
python manage.py sqlmigrate
python manage.py migrate
```

### Question 4
Une fois le fichier json créé , on peut charger son contenu dans la base de données : 
```bash
python manage.py loaddata examples 
```
Pour vérifier que les données sont bien chargées : 

```bash
python manage.py shell 

from collec_management.models import Collec
# Affiche toutes les collections de la base de données
for collec in Collec.objects.all():
    print(collec.title, collec.description, collec.date)
```

### Question 5 
- Création d'une template `collecinfos.html`
- Ajout de l'URL dans le fichier `collec_management/urls.py` 
- Ajout de la vue collec_infos dans le fichier `views.py`

### Question 6

- Création d'une template `all.html`
- Ajout de l'URL dans le fichier `collec_management/urls.py` 
- Ajout de la vue collec_list dans le fichier `views.py`