Cahier des charges – Application de gestion de plantes d’intérieur (Django)
Contexte et objectifs

Contexte  
Vous développez une application (web et/ou mobile) destinée aux particuliers et aux professionnels pour suivre l’état et l’entretien de leurs plantes.

Objectifs  

Centraliser les données de chaque plante (espèce, date d’achat, emplacement, historique d’arrosage, etc.) 
Rappeler automatiquement les entretiens à effectuer (arrosage, fertilisation, rempotage…) 
Fournir des conseils personnalisés selon l’espèce et les conditions environnementales 



Périmètre

Inclus  

Gestion d’un catalogue d’espèces (base de données) 
Création et modification de fiches « plante » 
Planification et notifications d’actions d’entretien 
Suivi visuel via photos et historique 
Statistiques d’ensemble (nombre de plantes, actions récurrentes, etc.)


Exclus (pour la v1)  

Vente ou e‑commerce de plantes 
Intelligence artificielle de diagnostic (cependant, prévoir extensibilité) 



Acteurs


Utilisateur final : crée et suit ses plantes 
Administrateur : gère le catalogue d’espèces et les paramètres globaux 
Système de notifications : envoie rappels par mail et/ou push 




Exigences fonctionnelles
Authentification 

   - Inscription via e‑mail et mot de passe  
   - Réinite. de mot de passe par e‑mail  


Gestion des plantes

   - Création / édition / suppression de fiche plante  
   - Association de tags (intérieur/extérieur, luminosité, etc.)  
   - Upload et affichage de photos  


Planification d’actions

   - Définir un calendrier récurrent (RRULE) pour chaque type d’entretien  
   - Paramétrer rappel par notification locale ou par e‑mail  


Notifications

   - Format : titre, description, lien vers la fiche plante  
   - Fréquence : configurable (minutes, heures, jours)  


Tableau de bord 

   - Vue synthétique : prochaines actions, plantes en bonne/mauvaise santé  
   - Filtres : par espèce, par statut d’entretien                                                                             

Exigences non‑fonctionnelles


Performance : temps de réponse < 2 s sur opérations courantes 
Scalabilité : prise en charge de plusieurs milliers d’utilisateurs 
Sécurité : chiffrement des mots de passe (bcrypt), HTTPS obligatoire 
Accessibilité : conformité WCAG 2.1 niveau AA 
Compatibilité : responsive web design, iOS ≥ 13, Android ≥ 9 


 7. Architecture technique

Frontend : React (web) 
Backend : Node.js + Express ou Django REST Framework 
Base de données : PostgreSQL (principal) + Redis (cache) 
Notifications : Firebase Cloud Messaging + SMTP (Mailgun) 
Hébergement : AWS (EC2, RDS, S3) ou équivalent 



Modèle de données (extrait simplifié)


Utilisateur** (id, nom, e‑mail, mot_de_passe_hashé, date_inscription) 
Espèce (id, nom_latin, nom_commun, description, besoins_lumière, besoins_eau) 
Plante (id, utilisateur_id, espece id, nom personnalisé, date_achat, emplacement) 
Action (id, plante_id, type_action, date_planifiée, statut, date_réalisée) 



Interfaces utilisateur (maquettes à prévoir)


Écran de connexion/inscription 
Liste des plantes avec aperçu photo et prochaine action 
Fiche détail plante 
Formulaire de planification d’entretien 
Dashboard statistiques 



Contraintes et risques


Dépendances externes : fiabilité du service SMTP / FCM 
Contraintes réglementaires : RGPD (données personnelles) 
Risques techniques : synchronisation des rappels sur plusieurs appareils 



Planning de réalisation (exemple)

| Phase                   | Durée estimée | Livrables                          |
|-------------------------|---------------|------------------------------------|
| 1. Analyse & spéc.      | 2 semaines    | Cahier des spécifications validé   |
| 2. Design UI/UX         | 3 semaines    | Maquettes & prototypes interactifs |
| 3. Développement v1     | 6 semaines    | API + Frontend de base             |
| 4. Tests & corrections  | 2 semaines    | Rapport de tests                   |
| 5. Déploiement pilote   | 1 semaine     | Version bêta en production         |


 realise par : mohamed slama et raed souissi et omar mazouz , rachid elhani
