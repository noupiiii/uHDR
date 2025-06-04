Dépendances techniques
=====================

Le projet uHDRv6 repose sur un ensemble de bibliothèques Python spécialisées, chacune jouant un rôle précis dans le fonctionnement du logiciel.

Dépendances Python principales
------------------------------

Interface graphique
~~~~~~~~~~~~~~~~~~~

PyQt5
^^^^^

.. code-block:: text

   PyQt5              # Interface graphique multi-plateformes (basée sur Qt)

**Rôle dans le projet :**
- Widgets et contrôles d'interface utilisateur
- Gestion des événements utilisateur
- Intégration avec les threads pour les traitements asynchrones
- Système de signaux/slots pour la communication inter-composants

**Fonctionnalités utilisées :**
- QMainWindow pour la fenêtre principale
- QGraphicsView pour l'affichage des images
- QThread pour les traitements en arrière-plan
- QPainter pour le rendu personnalisé

Traitement d'images et calcul numérique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NumPy
^^^^^

Bibliothèque fondamentale pour le calcul numérique en Python.

**Rôle dans le projet :**
- Manipulation des matrices d'images
- Opérations vectorielles haute performance
- Base pour toutes les opérations numériques

matplotlib
^^^^^^^^^^

.. code-block:: text

   matplotlib         # Visualisation de données scientifiques

**Rôle dans le projet :**
- Génération des histogrammes d'image
- Affichage des courbes tonales et leur manipulation
- Visualisation des espaces colorimétriques
- Graphiques de diagnostic et d'analyse

scikit-image
^^^^^^^^^^^^

.. code-block:: text

   scikit-image       # Traitement d'images scientifique

**Rôle dans le projet :**
- Filtres et transformations d'image avancés
- Segmentation et analyse d'image
- Correction géométrique et déformation
- Algorithmes de traitement d'image éprouvés

imageio
^^^^^^^

.. code-block:: text

   imageio            # Entrées/sorties d'images

**Rôle dans le projet :**
- Lecture et écriture de multiples formats d'image
- Gestion des métadonnées d'image
- Conversion entre différents formats
- Support des formats HDR spécialisés

rawpy
^^^^^

.. code-block:: text

   rawpy              # Traitement des images RAW

**Rôle dans le projet :**
- Décodage des formats RAW propriétaires (notamment Sony .arw)
- Interprétation des données brutes du capteur
- Démosaïquage et post-traitement des images RAW
- Préservation de la gamme dynamique complète

Gestion des couleurs
~~~~~~~~~~~~~~~~~~~

colour
^^^^^^

.. code-block:: text

   colour             # Gestion avancée des espaces colorimétriques

**Rôle dans le projet :**
- Conversions précises entre espaces colorimétriques (RGB/XYZ/Lab)
- Implémentation des modèles colorimétriques CIE
- Adaptation chromatique pour différents illuminants
- Calculs colorimétriques scientifiques

colour-science
^^^^^^^^^^^^^^

.. code-block:: text

   colour-science     # Outils scientifiques pour la couleur

**Rôle dans le projet :**
- Fonctions de correspondance de couleur (CMF - Color Matching Functions)
- Modèles de vision humaine pour l'optimisation perceptuelle
- Équations de rendu et tone mapping scientifiquement validées
- Standards colorimétriques industriels

Optimisation et performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

numba
^^^^^

.. code-block:: text

   numba              # Optimisation de code Python par compilation JIT

**Rôle dans le projet :**
- Accélération significative des calculs intensifs (x5-10 plus rapide)
- Compilation Just-In-Time des fonctions critiques
- Parallélisation automatique au niveau des boucles
- Support de l'accélération GPU CUDA
- Vectorisation SIMD automatique

**Fonctions optimisées :**
- Convolutions et filtres d'image
- Conversions d'espaces colorimétriques
- Calculs de courbes et interpolations
- Opérations matricielles complexes

pathos
^^^^^^

.. code-block:: text

   pathos             # Parallélisation des traitements

**Rôle dans le projet :**
- Traitement parallèle multi-cœur pour les opérations par lots
- Distribution efficace des tâches de calcul
- Pool de processus pour l'isolation des traitements
- Gestion automatique de la charge de travail

Intelligence artificielle
~~~~~~~~~~~~~~~~~~~~~~~~~

torch (PyTorch)
^^^^^^^^^^^^^^^

.. code-block:: text

   torch              # Framework d'apprentissage profond

**Rôle dans le projet :**
- Chargement et utilisation de réseaux de neurones pré-entraînés
- Inférence pour l'amélioration automatique d'images
- Optimisation GPU pour l'accélération des modèles IA
- Interface avec le modèle MSESig505_0419.pth

**Fonctionnalités utilisées :**
- torch.load() pour charger les modèles sauvegardés
- torch.nn pour l'architecture des réseaux
- torch.cuda pour l'accélération GPU
- torch.jit pour l'optimisation des modèles

scikit-learn
^^^^^^^^^^^^

.. code-block:: text

   scikit-learn       # Algorithmes d'apprentissage automatique

**Rôle dans le projet :**
- Segmentation intelligente d'image par clustering
- Classification automatique des couleurs et zones
- Réduction de dimensionnalité pour l'analyse d'image
- Algorithmes d'optimisation pour les paramètres

Géométrie et courbes
~~~~~~~~~~~~~~~~~~~

geomdl
^^^^^^

.. code-block:: text

   geomdl             # Bibliothèque géométrique pour NURBS

**Rôle dans le projet :**
- Manipulation précise des courbes B-Spline pour les courbes tonales
- Interpolation non uniforme pour des transitions douces
- Manipulation interactive des points de contrôle
- Génération de courbes lisses et précises

Dépendances système
-------------------

HDRip.dll
~~~~~~~~~

**Description :**
Bibliothèque C++ précompilée pour Windows fournissant les algorithmes de traitement HDR optimisés.

**Fonctionnalités :**
- Instructions SIMD (SSE/AVX) pour l'accélération vectorielle
- Optimisations spécifiques au processeur
- Gestion mémoire optimisée pour les grandes images
- Interface ctypes pour l'intégration Python

**Fonctions principales :**
- Conversions d'espaces colorimétriques haute performance
- Algorithmes de tone mapping optimisés
- Opérations de convolution accélérées
- Calculs matriciels vectorisés

exiftool.exe
~~~~~~~~~~~~

**Description :**
Outil de ligne de commande développé par Phil Harvey, référence mondiale pour la manipulation des métadonnées d'image.

**Capacités :**
- Lecture/écriture de métadonnées dans plus de 100 formats d'image
- Support complet des standards EXIF, IPTC, XMP, GPS
- Extraction d'informations techniques détaillées des appareils photo
- Préservation de l'intégrité des fichiers lors des modifications

**Intégration dans uHDRv6 :**
- Lancement via subprocess.Popen()
- Parsing des résultats au format JSON
- Gestion des erreurs et timeouts
- Cache des métadonnées pour les performances

Configuration des environnements
-------------------------------

Environnement de développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Python version :**
- Python 3.8+ recommandé
- Support des annotations de type
- Compatibilité avec les versions récentes des dépendances

**Installation des dépendances :**

.. code-block:: powershell

   pip install -r requirements.txt

**Dépendances de développement supplémentaires :**

.. code-block:: text

   pytest             # Tests unitaires
   black              # Formatage du code
   mypy               # Vérification de types
   sphinx             # Génération de documentation

Environnement de production
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Optimisations recommandées :**

1. **Numba avec cache persistant :**

   .. code-block:: python

      import numba
      numba.config.CACHE_DIR = './numba_cache'

2. **PyTorch optimisé :**

   .. code-block:: python

      torch.set_num_threads(4)  # Ajuster selon le CPU
      torch.backends.cudnn.benchmark = True  # Pour GPU

3. **Configuration mémoire :**

   .. code-block:: python

      import gc
      gc.set_threshold(700, 10, 10)  # Ajustement du garbage collector

Compatibilité et versions
-------------------------

Matrice de compatibilité
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Versions testées et supportées
   :header-rows: 1

   * - Composant
     - Version minimale
     - Version recommandée
     - Notes
   * - Python
     - 3.8
     - 3.10+
     - Support des annotations de type
   * - PyQt5
     - 5.12
     - 5.15+
     - Stabilité de l'interface
   * - NumPy
     - 1.19
     - 1.21+
     - Performances optimisées
   * - PyTorch
     - 1.8
     - 1.12+
     - Support CUDA récent
   * - Numba
     - 0.54
     - 0.56+
     - Optimisations LLVM
   * - Windows
     - 10 (1909)
     - 11
     - Support HDR natif

Gestion des dépendances
----------------------

Fichier requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``requirements.txt`` contient toutes les dépendances avec leurs versions spécifiques :

.. code-block:: text

   PyQt5>=5.15.0
   numpy>=1.21.0
   matplotlib>=3.5.0
   torch>=1.12.0
   numba>=0.56.0
   scikit-image>=0.19.0
   scikit-learn>=1.0.0
   colour-science>=0.3.16
   imageio>=2.16.0
   rawpy>=0.17.0
   pathos>=0.2.8
   geomdl>=5.3.0

Installation conditionnelle
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Certaines dépendances peuvent être installées conditionnellement selon l'environnement :

.. code-block:: python

   # Détection automatique de CUDA pour PyTorch
   try:
       import torch
       if torch.cuda.is_available():
           print("CUDA disponible - optimisations GPU activées")
       else:
           print("CUDA non disponible - mode CPU uniquement")
   except ImportError:
       print("PyTorch non installé")

Résolution des conflits
~~~~~~~~~~~~~~~~~~~~~~

**Problèmes courants et solutions :**

1. **Conflits de versions NumPy :**
   
   .. code-block:: powershell

      pip install --upgrade numpy
      pip install --force-reinstall scikit-image

2. **Problèmes PyQt5 sur Linux :**
   
   .. code-block:: bash

      sudo apt-get install python3-pyqt5-dev

3. **CUDA toolkit manquant :**
   
   .. code-block:: powershell

      # Installer CUDA Toolkit depuis NVIDIA
      # Puis réinstaller PyTorch avec support CUDA
      pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
