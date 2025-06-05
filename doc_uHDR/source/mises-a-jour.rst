================================= 
Mises à jour et Migration Python
=================================

Cette section documente les mises à jour et migrations importantes du projet uHDRv6, 
notamment la migration de Python 3.7 vers Python 3.12.

Migration Python 3.7 → 3.12
============================

Vue d'ensemble
--------------

Le projet uHDRv6 a été migré de Python 3.7 vers Python 3.12 pour bénéficier des dernières 
améliorations de performance, de sécurité et des nouvelles fonctionnalités du langage.

.. note::
   Cette migration représente un saut majeur de version avec de nombreux changements 
   potentiellement incompatibles qui nécessitent une attention particulière.

Motivations de la migration
---------------------------

**Avantages de Python 3.12 :**

- **Performance améliorée** : Jusqu'à 11% plus rapide que Python 3.11
- **Meilleure gestion d'erreurs** : Messages d'erreur plus précis et informatifs
- **Type hints améliorés** : Support étendu pour les annotations de type
- **Sécurité renforcée** : Corrections de vulnérabilités et améliorations SSL/TLS
- **Support à long terme** : Python 3.7 n'est plus maintenu depuis juin 2023

Checklist de migration
======================

Environnement et dépendances
----------------------------

**Environnement Python**

- [x] Installation de Python 3.12
- [x] Création d'un nouvel environnement virtuel
- [x] Mise à jour de pip vers la dernière version

**Dépendances principales**

- [x] **Matplotlib** : Mise à jour vers version compatible Python 3.12
- [x] **Sphinx** : Mise à jour vers version compatible Python 3.12
- [x] **sphinx_rtd_theme** : Ajout d'un thème pour la génération de la documentation  
  → *Commit* `a3c3a90` : ajout des bibliothèques de documentation
- [x] **scikit-learn** : Correction du nom de package et mise à jour pour compatibilité  
  → *Commit* `d387e0b` : renommage `sklearn` → `scikit-learn`

Code source et compatibilité
----------------------------

**Syntaxe et fonctionnalités dépréciées**

- [x] Passage de la valeur du slider d'un ``float`` à un string  
  → *Commit* `f320c3a` : ajout d'une vérification sur le type de valeur du slider

**Interface graphique (guiQt)**

- [x] **view.py** : Test de l'interface principale  
  → *Commit* `3c19765a` : vérification de l'existence de l’index dans `imagesControllers`
- [x] **controller.py** : Vérification de la logique de contrôle  
  → *Commits* `13cb308`, `acc2a8b` : sécurité sur `displayModel.get()` et `self.processPipes`
- [x] **model.py** : Test du modèle de données  
  → *Commit* `5443bf7` : contrôle de la validité de `selectedProcessPipe`
- [x] **thread.py** : Validation du multithreading  
  *(Aucun changement spécifique identifié)*
- [x] Gestion des événements Qt  
  → *Commit* `3e7a1a1` : correction du comportement de fermeture de la fenêtre d'export

Tests et validation
-------------------

**Tests de fonctionnalité**

- [ ] Import et chargement d'images HDR (.hdr)
- [ ] Modification des paramètres des images HDR
- [ ] Interface utilisateur et interactions
- [ ] Tests de charge sur gros volumes d'images

Documentation et déploiement
----------------------------

**Mise à jour documentation**

- [x] Prérequis système dans installation.rst
- [x] Instructions d'installation Python 3.12
- [x] Mise à jour des dépendances dans requirements.txt
- [x] Guide de migration pour les utilisateurs  
  → *Commit* `7d2e7d1` : documentation complète (guide de migration, usage, optimisations)
- [x] Documentation utilisateur finale  
  → *Commits* `850f1c8`, `4d7fc3a` : ajouts initiaux de documentation

Notes de version
================

Version actuelle: v6.0 (Python 3.12)
-------------------------------------

.. note::
   Les notes de version détaillées seront ajoutées ici au fur et à mesure 
   des releases de la version Python 3.12.

Ressources utiles
=================

Liens de référence
------------------

- `Python 3.12 Release Notes <https://docs.python.org/3.12/whatsnew/3.12.html>`_
