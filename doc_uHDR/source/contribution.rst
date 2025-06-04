Guide de contribution
====================

Ce document décrit comment contribuer au projet uHDRv6. Nous accueillons toutes les contributions, des corrections de bugs aux nouvelles fonctionnalités.

Types de contributions
---------------------

Rapports de bugs
~~~~~~~~~~~~~~~

**Comment signaler un bug :**

1. Vérifiez d'abord que le bug n'a pas déjà été signalé dans les issues
2. Créez un nouveau ticket avec un titre descriptif
3. Incluez les informations suivantes :
   - Version de uHDRv6
   - Système d'exploitation et version
   - Configuration matérielle (CPU, GPU, RAM)
   - Étapes pour reproduire le bug
   - Comportement attendu vs comportement observé
   - Logs d'erreur si disponibles

**Template de rapport de bug :**

.. code-block:: markdown

   ## Description du bug
   [Description claire et concise du problème]

   ## Étapes pour reproduire
   1. Aller à '...'
   2. Cliquer sur '....'
   3. Faire défiler jusqu'à '....'
   4. Voir l'erreur

   ## Comportement attendu
   [Description de ce qui devrait se passer]

   ## Captures d'écran
   [Si applicable, ajoutez des captures d'écran]

   ## Environnement
   - OS: [ex. Windows 11]
   - Version uHDRv6: [ex. 6.2]
   - Python: [ex. 3.10.5]
   - GPU: [ex. NVIDIA RTX 3080]

   ## Informations supplémentaires
   [Tout autre contexte utile]

Demandes de fonctionnalités
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Processus pour une nouvelle fonctionnalité :**

1. Ouvrez une issue avec le label "enhancement"
2. Décrivez clairement la fonctionnalité souhaitée
3. Expliquez pourquoi cette fonctionnalité serait utile
4. Proposez une implémentation si possible
5. Attendez la discussion et l'approbation avant de commencer le développement

Corrections de documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La documentation peut toujours être améliorée :

- Corrections de fautes de frappe
- Clarifications d'explications
- Ajout d'exemples
- Traductions
- Amélioration de la structure

Contributions de code
~~~~~~~~~~~~~~~~~~~

**Types de contributions de code acceptées :**

- Corrections de bugs
- Nouvelles fonctionnalités approuvées
- Optimisations de performance
- Amélioration du code existant
- Tests supplémentaires

Configuration de l'environnement de développement
------------------------------------------------

Prérequis
~~~~~~~~~

- Git installé et configuré
- Python 3.8+ avec pip
- Compte GitHub
- IDE recommandé : VS Code, PyCharm, ou Spyder

Installation
~~~~~~~~~~~

1. **Fork du repository**

   .. code-block:: bash

      # Sur GitHub, cliquez sur "Fork"
      # Puis clonez votre fork
      git clone https://github.com/votre-username/uHDRv6.git
      cd uHDRv6

2. **Configuration du remote upstream**

   .. code-block:: bash

      git remote add upstream https://github.com/original-repo/uHDRv6.git
      git remote -v

3. **Création de l'environnement virtuel**

   .. code-block:: bash

      python -m venv venv
      # Windows
      venv\Scripts\activate
      # Linux/Mac
      source venv/bin/activate

4. **Installation des dépendances**

   .. code-block:: bash

      pip install -r requirements.txt
      pip install -r requirements-dev.txt  # Dépendances de développement

5. **Installation en mode développement**

   .. code-block:: bash

      pip install -e .

Configuration des outils de développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Pre-commit hooks** (recommandé) :

.. code-block:: bash

   pip install pre-commit
   pre-commit install

**Configuration VS Code** (`.vscode/settings.json`) :

.. code-block:: json

   {
       "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
       "python.formatting.provider": "black",
       "python.linting.enabled": true,
       "python.linting.pylintEnabled": false,
       "python.linting.flake8Enabled": true,
       "python.testing.pytestEnabled": true,
       "python.testing.unittestEnabled": false
   }

Workflow de développement
------------------------

Création d'une branche
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Mise à jour de main
   git checkout main
   git pull upstream main
   
   # Création d'une nouvelle branche
   git checkout -b feature/nom-de-la-fonctionnalite
   # ou
   git checkout -b bugfix/description-du-bug

Développement
~~~~~~~~~~~~

1. **Implémentez vos modifications**
   - Suivez les conventions de code (voir section Standards)
   - Écrivez des tests pour votre code
   - Documentez les nouvelles fonctionnalités

2. **Tests réguliers**

   .. code-block:: bash

      # Lancer tous les tests
      pytest
      
      # Tests avec couverture
      pytest --cov=hdrCore --cov=guiQt
      
      # Tests spécifiques
      pytest tests/test_image.py::test_load_hdr_image

3. **Vérification du code**

   .. code-block:: bash

      # Formatage automatique
      black .
      
      # Vérification du style
      flake8
      
      # Vérification des types
      mypy hdrCore/ guiQt/

Commits
~~~~~~

**Convention de messages de commit :**

.. code-block:: text

   type(scope): description courte

   Description plus détaillée si nécessaire.

   Fixes #123

**Types de commits :**

- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: documentation
- `style`: formatage, pas de changement de code
- `refactor`: refactoring de code
- `test`: ajout/modification de tests
- `chore`: maintenance, dépendances

**Exemples :**

.. code-block:: bash

   git commit -m "feat(image): add support for TIFF format"
   git commit -m "fix(gui): resolve memory leak in image viewer"
   git commit -m "docs(api): update HDRImage class documentation"

Soumission d'une Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Push de votre branche**

   .. code-block:: bash

      git push origin feature/nom-de-la-fonctionnalite

2. **Création de la Pull Request**
   - Allez sur GitHub et cliquez "New Pull Request"
   - Choisissez votre branche vers `main`
   - Remplissez le template de PR

3. **Template de Pull Request :**

.. code-block:: markdown

   ## Description
   [Description des changements]

   ## Type de changement
   - [ ] Bug fix (changement non-breaking qui corrige un problème)
   - [ ] Nouvelle fonctionnalité (changement non-breaking qui ajoute une fonctionnalité)
   - [ ] Breaking change (correction ou fonctionnalité qui casserait la compatibilité)
   - [ ] Documentation

   ## Tests
   - [ ] J'ai ajouté des tests qui prouvent que ma correction/fonctionnalité fonctionne
   - [ ] Les tests nouveaux et existants passent localement

   ## Checklist
   - [ ] Mon code suit les guidelines du projet
   - [ ] J'ai fait une self-review de mon code
   - [ ] J'ai commenté le code dans les zones difficiles à comprendre
   - [ ] J'ai fait les changements correspondants dans la documentation
   - [ ] Mes changements ne génèrent pas de nouveaux warnings
   - [ ] J'ai ajouté des tests qui prouvent l'efficacité de ma correction/fonctionnalité

Standards de code
----------------

Style Python
~~~~~~~~~~~~

**Formatage :**
- Utilisez `black` pour le formatage automatique
- Largeur de ligne : 88 caractères (défaut de black)
- Utilisez `isort` pour organiser les imports

**Conventions de nommage :**
- Classes : `PascalCase` (ex: `HDRImage`)
- Fonctions et variables : `snake_case` (ex: `load_image`)
- Constantes : `UPPER_SNAKE_CASE` (ex: `MAX_IMAGE_SIZE`)
- Fichiers et modules : `snake_case` (ex: `image_processing.py`)

**Docstrings :**
Utilisez le style Google/Sphinx :

.. code-block:: python

   def apply_tone_mapping(image, curve_params):
       """Applique un tone mapping à une image HDR.

       Args:
           image (numpy.ndarray): Image HDR source
           curve_params (dict): Paramètres de la courbe tonale

       Returns:
           numpy.ndarray: Image avec tone mapping appliqué

       Raises:
           ValueError: Si les paramètres sont invalides
           
       Example:
           >>> image = load_hdr_image('test.hdr')
           >>> params = {'gamma': 2.2, 'exposure': 1.0}
           >>> result = apply_tone_mapping(image, params)
       """

**Type hints :**
Utilisez les annotations de type :

.. code-block:: python

   from typing import Optional, List, Dict, Tuple
   import numpy as np

   def process_images(
       image_paths: List[str], 
       output_dir: str,
       params: Optional[Dict[str, float]] = None
   ) -> List[str]:
       """Process multiple images."""

Organisation du code
~~~~~~~~~~~~~~~~~~~

**Structure des modules :**

.. code-block:: text

   module/
   ├── __init__.py          # Exports publics
   ├── core.py              # Fonctionnalités principales
   ├── utils.py             # Fonctions utilitaires
   ├── exceptions.py        # Exceptions personnalisées
   └── tests/
       ├── __init__.py
       ├── test_core.py
       └── test_utils.py

**Imports :**

.. code-block:: python

   # Standard library
   import os
   import sys
   from pathlib import Path

   # Third party
   import numpy as np
   import torch
   from PyQt5.QtWidgets import QWidget

   # Local imports
   from hdrCore.image import HDRImage
   from .utils import validate_image

Tests
----

Framework de tests
~~~~~~~~~~~~~~~~~

Utilisez `pytest` pour tous les tests :

.. code-block:: python

   import pytest
   import numpy as np
   from hdrCore.image import HDRImage

   class TestHDRImage:
       def test_load_valid_hdr_file(self):
           """Test de chargement d'un fichier HDR valide."""
           image = HDRImage()
           image.load_from_file('tests/data/test.hdr')
           assert image.data is not None
           assert image.data.dtype == np.float32

       def test_load_invalid_file_raises_error(self):
           """Test qu'un fichier invalide lève une exception."""
           image = HDRImage()
           with pytest.raises(FileNotFoundError):
               image.load_from_file('nonexistent.hdr')

       @pytest.mark.parametrize("format", ["hdr", "exr", "tiff"])
       def test_save_different_formats(self, format):
           """Test de sauvegarde dans différents formats."""
           # Test parametrisé

Couverture de tests
~~~~~~~~~~~~~~~~~~

Objectifs de couverture :
- Code nouveau : 90%+ de couverture
- Code critique (traitement d'image) : 95%+
- Code d'interface : 70%+ (plus difficile à tester)

.. code-block:: bash

   # Rapport de couverture
   pytest --cov=hdrCore --cov=guiQt --cov-report=html
   # Ouvre htmlcov/index.html pour voir le rapport détaillé

Documentation
------------

Types de documentation
~~~~~~~~~~~~~~~~~~~~~

1. **Docstrings** : Documentation du code (API)
2. **README** : Vue d'ensemble et quick start
3. **Documentation Sphinx** : Documentation complète
4. **Commentaires** : Explications du code complexe

Écriture de documentation
~~~~~~~~~~~~~~~~~~~~~~~~

**Principes :**
- Clarté avant tout
- Exemples concrets
- Mise à jour avec le code
- Différents niveaux de détail pour différents publics

**Structure d'une page de documentation :**

.. code-block:: restructuredtext

   Titre de la page
   ================

   Description courte de ce que fait cette fonctionnalité.

   Usage de base
   ------------

   Exemple simple d'utilisation.

   Options avancées
   ---------------

   Détails pour les utilisateurs avancés.

   Référence API
   ------------

   Documentation technique complète.

Build de la documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd doc_uHDR
   make html
   # La documentation sera dans build/html/

Review et intégration
--------------------

Processus de review
~~~~~~~~~~~~~~~~~~

1. **Review automatique :**
   - Tests CI/CD passent
   - Couverture de code acceptable
   - Style de code conforme

2. **Review manuelle :**
   - Pertinence de la fonctionnalité
   - Qualité de l'implémentation
   - Compatibilité avec le code existant
   - Documentation adéquate

3. **Feedback et itération :**
   - Répondez aux commentaires des reviewers
   - Apportez les modifications demandées
   - Demandez des clarifications si nécessaire

Critères d'acceptation
~~~~~~~~~~~~~~~~~~~~~

Une PR sera acceptée si :

- [ ] Les tests passent
- [ ] La couverture de code est suffisante
- [ ] Le code suit les standards du projet
- [ ] La documentation est à jour
- [ ] Pas de régression fonctionnelle
- [ ] Approbation d'au moins un mainteneur

Ressources pour les contributeurs
---------------------------------

Documentation technique
~~~~~~~~~~~~~~~~~~~~~~

- Architecture du projet : `architecture.rst`
- API Reference : `api.rst`
- Guide d'optimisation : `optimisations.rst`

Outils utiles
~~~~~~~~~~~~~

- **GitHub CLI** : `gh` pour gérer les PRs en ligne de commande
- **pytest-xdist** : Exécution parallèle des tests
- **coverage.py** : Analyse de couverture de code
- **mypy** : Vérification de types statique

Communauté
~~~~~~~~~

- **Issues GitHub** : Pour discussions techniques
- **Email** : remi.cozot@univ-littoral.fr pour questions directes
- **Code de conduite** : Respectueux et constructif

Reconnaissance
~~~~~~~~~~~~~

Les contributeurs seront reconnus dans :
- Fichier CONTRIBUTORS.md
- Notes de version
- Documentation

Merci de contribuer à uHDRv6 ! 🎉
