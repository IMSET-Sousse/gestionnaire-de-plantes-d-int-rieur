 Cahier des charges – Application de gestion de 
plantes d’intérieur (Django) 
1. 
�
�
 Contexte et objectifs 
L'application a pour but d’aider les utilisateurs à gérer leurs plantes d’intérieur. Elle permet : 
● De suivre l’arrosage, l’exposition à la lumière, et les besoins en engrais. 
● D’avoir des rappels personnalisés selon les besoins de chaque plante. 
● De consulter des fiches informatives sur chaque type de plante. 
2. 
�
�
 Cible utilisateur 
● Les amateurs de plantes d’intérieur. 
● Les personnes souhaitant prendre soin de leurs plantes sans expertise botanique. 
3. 
⚙
 Fonctionnalités attendues 
a. Gestion des utilisateurs 
● Inscription / Connexion / Déconnexion. 
● Profil utilisateur (nom, email, préférences). 
b. Gestion des plantes 
● Ajouter une plante (nom, espèce, date d’acquisition, photo). 
● Associer des besoins (arrosage, engrais, lumière). 
● Éditer / Supprimer une plante. 
c. Suivi & rappels 
● Historique des arrosages. 
● Rappels automatiques (notifications email ou affichées dans le tableau de bord). 
● Calendrier d’entretien. 
d. Base de données de plantes 
● Fiches préremplies avec données botaniques (nom scientifique, famille, fréquence 
d’arrosage, etc.). 
● Recherche par nom ou caractéristiques. 
e. Dashboard 
● Vue d’ensemble des plantes. 
● Alertes (plantes à arroser aujourd’hui, plantes malades...). 
f. Autres options (bonus) 
● Upload de photo pour détecter l’état de la plante (IA). 
● Communauté (échange de conseils, commentaires...). 
4. 
�
�
 Architecture technique 
a. Backend 
● Framework : Django 4.x 
● Modules : 
○ Django Rest Framework (si API prévue) 
○ Django-cron (rappels automatiques) 
○ Django Allauth (gestion utilisateur) 
b. Frontend 
● HTML/CSS avec Django Templates 
● Option : Intégration React ou Vue.js (API REST) 
c. Base de données 
● PostgreSQL ou SQLite (développement) 
d. Hébergement 
● Heroku / Railway / Render / Serveur privé 
● Stockage média : Cloudinary / Amazon S3 / local 
5. 
�
�
 Sécurité 
● Authentification sécurisée (hashage des mots de passe). 
● Permissions selon utilisateur. 
● Protection CSRF, XSS. 
6. 
�
�
 Tests & Qualité 
● Tests unitaires (modèles, vues) 
● Tests fonctionnels (formulaires, flux utilisateurs) 
● Validation via Django Admin 
7. 
�
�
 Planning estimatif 
Étape 
Spécifications / 
Maquettes 
Durée 
estimée 
1 semaine 
Développement backend 2 à 3 
semaines 
Intégration frontend 
1 à 2 
semaines 
Tests & déploiement 
1 semaine 
8. 
�
�
 Livrables 
● Code source complet 
● Documentation technique 
● Manuel utilisateur 
● Base de données pré-remplie (plantes communes) 

Documentation technique
realise par : mohamed slama et raed souissi et omar mazouz , rachid elhani