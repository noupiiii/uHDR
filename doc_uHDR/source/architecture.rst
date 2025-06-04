Architecture technique
=====================

L'architecture du projet uHDRv6 est organisée en plusieurs modules interconnectés, suivant un modèle MVC (Modèle-Vue-Contrôleur) qui sépare clairement les responsabilités.

Structure des dossiers
----------------------

.. code-block:: text

   uHDRv6/
   ├── guiQt/               # Interface graphique PyQt5
   │   ├── controller.py    # Contrôleurs de l'interface (gestion des événements)
   │   ├── model.py         # Modèles de données (structure des données)
   │   ├── thread.py        # Gestion des traitements asynchrones (performances)
   │   ├── view.py          # Composants d'affichage (interface utilisateur)
   │   └── view.useCase.py  # Cas d'utilisation de l'interface (scénarios)
   ├── hdrCore/             # Cœur de traitement HDR
   │   ├── aesthetics.py    # Fonctions d'amélioration esthétique (retouche automatique)
   │   ├── coreC.py         # Interface Python vers le core C++ (optimisation)
   │   ├── image.py         # Gestion des images (chargement, conversion, manipulation)
   │   ├── metadata.py      # Gestion des métadonnées (EXIF, IPTC, XMP)
   │   ├── net.py           # Modèle de réseau neuronal (intelligence artificielle)
   │   ├── numbafun.py      # Fonctions optimisées avec Numba (accélération)
   │   ├── processing.py    # Fonctions de traitement d'image (algorithmes)
   │   ├── quality.py       # Évaluation de la qualité d'image (métriques)
   │   ├── srgb.py          # Gestion de l'espace colorimétrique sRGB (conversions)
   │   └── utils.py         # Fonctions utilitaires (outils communs)
   ├── preferences/         # Gestion des préférences
   │   ├── preferences.py   # Module de gestion des préférences (configuration)
   │   ├── prefs.json       # Fichier de configuration des préférences (paramètres)
   │   ├── tags.json        # Gestion des tags (métadonnées)
   │   └── tags.old.json    # Sauvegarde des tags (backup)
   ├── HDRip.dll            # Bibliothèque C++ pour le traitement HDR (performances)
   ├── HDRipold.dll         # Ancienne version de la bibliothèque (compatibilité)
   ├── MSESig505_0419.pth   # Modèle de réseau neuronal pré-entraîné (IA)
   ├── exiftool.exe         # Outil de gestion des métadonnées EXIF (intégration)
   ├── requirements.txt     # Dépendances Python (environnement)
   ├── uHDR.py              # Point d'entrée de l'application (bootstrap)
   └── uHDR.pyproj/sln      # Fichiers de projet Visual Studio (développement)

Organisation en couches
----------------------

Le projet s'articule autour de trois couches principales :

Couche de présentation (guiQt)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Responsabilités :**
- Gestion de l'interface utilisateur
- Interactions avec l'utilisateur
- Affichage des résultats

**Composants principaux :**

* ``controller.py`` : Gère les événements utilisateur et orchestre les traitements
* ``model.py`` : Contient les structures de données pour l'interface
* ``view.py`` : Composants d'affichage et widgets personnalisés
* ``thread.py`` : Gestion des traitements asynchrones pour maintenir la réactivité
* ``view.useCase.py`` : Implémentation des cas d'utilisation spécifiques

**Technologies utilisées :**
- PyQt5 pour l'interface graphique
- Threading pour la gestion asynchrone
- Signaux/slots pour la communication entre composants

Couche métier (hdrCore)
~~~~~~~~~~~~~~~~~~~~~~

**Responsabilités :**
- Logique de traitement d'images HDR
- Algorithmes de manipulation d'image
- Intelligence artificielle et optimisations

**Composants principaux :**

* ``image.py`` : Classes et fonctions pour la manipulation d'images
* ``processing.py`` : Algorithmes de traitement d'image
* ``aesthetics.py`` : Fonctions d'amélioration automatique
* ``net.py`` : Intégration des modèles de réseau neuronal
* ``quality.py`` : Métriques et évaluation de qualité
* ``coreC.py`` : Interface vers les fonctions C++ optimisées
* ``numbafun.py`` : Fonctions accélérées avec Numba
* ``metadata.py`` : Gestion des métadonnées d'image
* ``srgb.py`` : Conversions d'espaces colorimétriques
* ``utils.py`` : Fonctions utilitaires partagées

**Technologies utilisées :**
- NumPy pour les calculs numériques
- Numba pour l'accélération JIT
- PyTorch pour l'intelligence artificielle
- ctypes pour l'interface C++

Couche de données (preferences)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Responsabilités :**
- Persistance des paramètres utilisateur
- Configuration de l'application
- Gestion des profils et préférences

**Composants principaux :**

* ``preferences.py`` : API de gestion des préférences
* ``prefs.json`` : Stockage des configurations
* ``tags.json`` : Gestion des étiquettes et métadonnées
* ``tags.old.json`` : Système de sauvegarde

**Technologies utilisées :**
- JSON pour le stockage des configurations
- Python pickle pour les objets complexes

Composants externes
------------------

HDRip.dll
~~~~~~~~~

**Description :**
Bibliothèque C++ précompilée pour Windows fournissant les fonctions de traitement HDR optimisées.

**Caractéristiques :**
- Utilise des instructions SIMD (SSE/AVX) pour l'accélération
- Interface via ctypes pour l'intégration Python
- Algorithmes optimisés pour les opérations critiques
- Gestion mémoire efficace pour les grandes images

**Fonctions principales :**
- Conversions d'espaces colorimétriques haute performance
- Algorithmes de tone mapping optimisés
- Opérations matricielles vectorisées

exiftool.exe
~~~~~~~~~~~

**Description :**
Outil en ligne de commande développé par Phil Harvey pour la manipulation des métadonnées d'image.

**Capacités :**
- Lecture et écriture de métadonnées dans presque tous les formats
- Support des standards EXIF, IPTC, XMP
- Extraction d'informations techniques détaillées
- Préservation de l'intégrité des données

MSESig505_0419.pth
~~~~~~~~~~~~~~~~~

**Description :**
Modèle PyTorch pré-entraîné pour l'amélioration automatique des images HDR.

**Caractéristiques :**
- Réseau neuronal entraîné sur des milliers d'images HDR
- Optimisation spécifique pour les contenus haute gamme dynamique
- Inférence rapide pour l'amélioration temps réel
- Adaptation au contenu de l'image

Patterns architecturaux
----------------------

Modèle MVC (Modèle-Vue-Contrôleur)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Séparation des préoccupations :**
- **Modèle** : Logique métier et données (hdrCore + preferences)
- **Vue** : Interface utilisateur (guiQt/view.py)
- **Contrôleur** : Gestion des interactions (guiQt/controller.py)

**Avantages :**
- Maintainabilité améliorée
- Testabilité des composants
- Réutilisabilité du code
- Évolutivité de l'architecture

Pattern Observer
~~~~~~~~~~~~~~~~

**Implémentation :**
Utilisation du système signaux/slots de PyQt5 pour la communication entre composants.

**Avantages :**
- Faible couplage entre les modules
- Communication asynchrone
- Réactivité de l'interface

Pattern Strategy
~~~~~~~~~~~~~~~~

**Implémentation :**
Différents modes de calcul (Python, Numba, CUDA) implémentés comme des stratégies interchangeables.

**Avantages :**
- Adaptation aux capacités du système
- Optimisation des performances
- Facilité d'ajout de nouveaux modes

Flux de données
--------------

Pipeline de traitement d'image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Chargement** : Lecture du fichier via imageio ou rawpy
2. **Décodage** : Extraction des métadonnées avec exiftool
3. **Conversion** : Transformation vers l'espace colorimétrique de travail
4. **Traitement** : Application des algorithmes de manipulation
5. **Prévisualisation** : Génération d'aperçus pour l'interface
6. **Exportation** : Sauvegarde dans le format de sortie choisi

Communication inter-modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Interface Python-C++ :**
- Utilisation de ctypes pour l'appel des fonctions HDRip.dll
- Gestion automatique des types de données
- Optimisation des transferts mémoire

**Communication avec exiftool :**
- Lancement de processus externe via subprocess
- Parsing des résultats JSON
- Gestion des erreurs et timeouts

**Chargement des modèles IA :**
- Initialisation paresseuse des modèles PyTorch
- Cache des résultats d'inférence
- Gestion GPU/CPU automatique

Extensibilité
------------

Points d'extension
~~~~~~~~~~~~~~~~~

**Nouveaux formats d'image :**
- Extension du module ``image.py``
- Ajout de décodeurs spécialisés
- Intégration dans le pipeline existant

**Nouveaux algorithmes de traitement :**
- Ajout de fonctions dans ``processing.py``
- Intégration avec le système de préférences
- Exposition dans l'interface utilisateur

**Nouveaux modèles d'IA :**
- Extension du module ``net.py``
- Support de différents frameworks
- Configuration dynamique des modèles

Plugin architecture
~~~~~~~~~~~~~~~~~~~

L'architecture permet l'ajout de plugins pour :
- Nouveaux formats d'importation/exportation
- Algorithmes de traitement personnalisés
- Intégrations avec des services externes
- Interfaces utilisateur spécialisées
