Installation et configuration
=============================

Prérequis système
-----------------

- **Python** : Version 3.12 ou supérieure (migration récente depuis Python 3.7)
- **Système d'exploitation** : Windows 10/11 (64 bits)
- **Processeur** : Intel/AMD multi-cœur recommandé
- **Mémoire** : 8 Go minimum, 16 Go recommandé pour les images 4K
- **Stockage** : 500 Mo d'espace disque pour l'installation
- **Affichage** : 
  
  * Écran standard pour les fonctions de base
  * Écran compatible HDR recommandé pour tirer pleinement parti du logiciel

- **GPU** : 
  
  * Facultatif pour le mode standard
  * NVIDIA avec support CUDA recommandé pour les performances optimales

.. note::
   **Migration Python 3.12** : Le projet a récemment migré de Python 3.7 vers Python 3.12.
   Consultez la section :doc:`mises-a-jour` pour plus de détails sur cette migration.

Installation de l'environnement
-------------------------------

1. **Installation de Python 3.12**

   Téléchargez et installez Python 3.12 depuis `python.org <https://www.python.org/downloads/>`_.
   
   .. code-block:: powershell

      # Vérifier la version Python installée
      python --version
      # Doit afficher: Python 3.12.x

2. **Cloner le dépôt ou extraire l'archive**

   .. code-block:: powershell

      git clone <repository-url>
      cd uHDRv6

3. **Créer un environnement virtuel Python** (recommandé)

   .. code-block:: powershell

      # Création de l'environnement avec Python 3.12
      python -m venv venv
      venv\Scripts\Activate.ps1

4. **Mettre à jour pip et installer les dépendances**

   .. code-block:: powershell

      # Mise à jour de pip
      python -m pip install --upgrade pip
      
      # Installation des dépendances
      pip install -r requirements.txt

5. **Vérifier l'installation des composants externes**

   - Assurez-vous que ``HDRip.dll`` est présent dans le répertoire principal
   - Vérifiez que ``exiftool.exe`` est accessible

Configuration avancée
---------------------

Configuration des écrans HDR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``preferences/prefs.json`` contient les configurations pour différents types d'écrans HDR :

.. code-block:: json

   {
     "HDRdisplays": {
       "imagePath": "C:/Users/username/Documents/hdrImages"
     }
   }

Paramètres principaux :

- ``shape`` : Résolution cible [hauteur, largeur]
- ``scaling`` : Facteur d'échelle pour les valeurs HDR
- ``post`` : Suffixe ajouté aux fichiers exportés
- ``tag`` : Identifiant interne du profil

Configuration des performances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Éditez le fichier ``preferences/preferences.py`` pour ajuster les paramètres de performances :

.. code-block:: python

   # Mode de calcul : 'python', 'numba', 'cuda'
   computation = 'numba'

   # Mode verbeux pour le débogage
   verbose = True

Démarrage de l'application
-------------------------

Pour lancer l'application, exécutez le script principal :

.. code-block:: powershell

   python uHDR.py

L'application initialise séquentiellement :

1. Chargement des préférences utilisateur
2. Initialisation de l'interface graphique
3. Détection des écrans disponibles
4. Chargement des modèles d'IA si nécessaire