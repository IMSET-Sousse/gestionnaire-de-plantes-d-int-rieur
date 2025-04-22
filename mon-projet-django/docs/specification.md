🗂 Cahier des charges — Application “Gestionnaire de Plantes d’Intérieur” (Django)
🔖 1. Contexte
L'application a pour but d’aider les utilisateurs à gérer leurs plantes d'intérieur : arrosage, lumière, humidité, engrais, etc. Elle permet de suivre l'état de santé des plantes, d’obtenir des rappels, et d'accéder à des fiches techniques.

🎯 2. Objectifs
Gérer un catalogue de plantes (personnelles ou générales)

Suivre les besoins spécifiques de chaque plante (arrosage, lumière, humidité, etc.)

Recevoir des rappels (notifications ou e-mails)

Ajouter des photos et des notes

Gérer plusieurs utilisateurs (authentification)

Accès à des fiches informatives par espèce

⚙️ 3. Fonctionnalités principales
3.1 Gestion des utilisateurs
Inscription / Connexion / Déconnexion

Gestion du profil (photo, nom, email, etc.)

3.2 Gestion des plantes
Ajouter une plante avec photo

Définir les besoins : arrosage, lumière, température, engrais

Journaliser des événements (arrosage, rempotage, etc.)

Voir l’historique d’une plante

3.3 Rappels et notifications
Système de rappel automatique basé sur la fréquence d’arrosage ou autres besoins

Notifications par e-mail ou dans l’app

3.4 Fiches plantes
Accès à une base de données de plantes (nom, besoins, entretien)

Recherche par nom / type / besoin

3.5 Tableau de bord
Vue d’ensemble des plantes

Rappels du jour

Alertes (ex : "Plante X n’a pas été arrosée depuis 10 jours")

🧱 4. Architecture technique
4.1 Backend
Framework: Django

Base de données: PostgreSQL (ou SQLite pour dev)

Authentification: Django Auth (JWT ou sessions)

4.2 Frontend
Template Django (ou React/VueJS si séparation frontend)

Responsive (mobile first)

4.3 Extensions utiles
Django REST framework (si API)

Django Crispy Forms

Django Allauth (authentification sociale)

Celery + Redis (pour rappels automatisés)

Pillow (gestion images)

Django Storages (si hébergement sur S3 ou autre)


    
📅 6. Planning prévisionnel (exemple)

Étape	Durée	Détail
Analyse & conception	1 semaine	Définition des modèles, maquettes
Développement backend	2 semaines	Modèles, vues, logique métier
Développement frontend	1 semaine	Templates, UI
Intégration rappels / email	1 semaine	Notifications, Celery
Tests & déploiement	1 semaine	Debug, mise en ligne
🚀 7. Livrables
Code source sur GitHub

Base de données de test

Documentation technique
realise par : mohamed slama et raed souissi et omar mazouz , rachid elhani