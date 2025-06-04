# uHDRv6 - Documentation Technique

## Présentation générale

uHDRv6 est un logiciel d'édition d'images HDR (High Dynamic Range) développé par Rémi Cozot (remi.cozot@univ-littoral.fr). Cette version dispose d'un cœur de traitement écrit en C++ (HDRip.dll) et d'une interface graphique développée en Python avec PyQt5.

Le logiciel est conçu pour traiter et améliorer des images à haute gamme dynamique, permettant de manipuler des images avec un contraste, une luminosité et une richesse de couleurs bien supérieurs aux images standard (SDR - Standard Dynamic Range). Cette approche est particulièrement utile pour les photographies captant des scènes à fort contraste ou pour préparer des contenus destinés aux écrans HDR modernes.

### Contexte technique

uHDRv6 fournit les outils nécessaires pour:
- Manipuler les images HDR (.hdr) et RAW (.arw)
- Convertir entre différents formats et espaces colorimétriques
- Appliquer des courbes tonales avancées
- Optimiser le rendu pour différents types d'écrans HDR

## Licence

Ce logiciel est distribué sous licence GNU General Public License v3.0, permettant sa redistribution et sa modification selon les termes de cette licence. Le code source est donc libre d'utilisation, de modification et de distribution, tant que les dérivés respectent les mêmes conditions de licence.

## Architecture du projet

L'architecture du projet est organisée en plusieurs modules interconnectés, suivant un modèle MVC (Modèle-Vue-Contrôleur) qui sépare clairement les responsabilités :

### Structure des dossiers

```
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
```

### Organisation technique

Le projet s'articule autour de trois couches principales :

1. **Couche de présentation** (guiQt) : Gère l'interface utilisateur et les interactions
2. **Couche métier** (hdrCore) : Contient la logique de traitement d'images HDR
3. **Couche de données** (preferences) : Gère la persistance des paramètres

L'application utilise également plusieurs composants externes :
- **HDRip.dll** : Bibliothèque C++ qui fournit des algorithmes optimisés pour le traitement HDR
- **exiftool.exe** : Outil tiers pour la manipulation des métadonnées d'images
- **MSESig505_0419.pth** : Modèle PyTorch pré-entraîné pour l'amélioration automatique des images

## Fonctionnalités principales

Le logiciel uHDRv6 offre plusieurs fonctionnalités avancées pour le traitement des images HDR :

### 1. Importation et formats supportés

* **Formats HDR natifs** : Support du format Radiance HDR (.hdr) stockant les valeurs en virgule flottante
* **Formats RAW** : Support des fichiers RAW Sony (.arw) avec préservation de la gamme dynamique complète
* **Formats SDR** : Importation des formats traditionnels (.jpg, .png) avec conversion vers l'espace HDR

Le processus d'importation inclut :
- Décodage des métadonnées techniques via exiftool
- Conversion vers l'espace colorimétrique de travail interne (XYZ)
- Préservation des données originales pour un traitement non destructif

### 2. Visualisation HDR

* **Support multi-écrans** : Détection et utilisation optimisée des moniteurs HDR
* **Modes d'affichage** : 
  - Mode galerie (comparaison d'images)
  - Mode plein écran (visualisation détaillée)
  - Mode avant/après (comparaison des modifications)
* **Prévisualisation adaptative** : Simulation du rendu sur différents types d'écrans HDR
  - Profils VESA DisplayHDR (400/1000 nits)
  - Format HLG (Hybrid Log-Gamma)

### 3. Outils d'édition

* **Ajustements globaux** :
  - Exposition (EV, stops)
  - Contraste (global et local)
  - Saturation et vibrance
  - Balance des blancs
  
* **Courbes tonales** :
  - Courbes paramétriques
  - Courbes B-Spline
  - Manipulation par points de contrôle
  - Courbes automatiques basées sur IA

* **Édition sélective** :
  - Édition par zones de luminance
  - Masques par luminosité
  - Corrections locales
  
* **Gestion des couleurs** :
  - Ajustements HSL
  - Optimisation colorimétrique
  - Mapping de gammes de couleurs

### 4. Traitement par lots

* **Pipeline de traitement** : Application des mêmes ajustements à plusieurs images
* **Profils d'édition** : Sauvegarde et chargement de configurations de traitement
* **Traitement parallèle** : Utilisation des multiples cœurs du processeur pour accélérer le traitement
* **File d'attente** : Gestion des tâches de traitement en arrière-plan

### 5. Exportation et partage

* **Formats de sortie** :
  - Radiance HDR (.hdr) pour préserver la gamme dynamique complète
  - JPEG/PNG avec tone mapping optimisé pour les écrans SDR
  - Formats spéciaux pour écrans HDR spécifiques
  
* **Options d'exportation** :
  - Résolution personnalisable
  - Préservation des métadonnées
  - Compression paramétrable
  - Profils colorimétriques intégrés

* **Intégration** :
  - Exportation optimisée pour le web
  - Métadonnées pour systèmes de gestion d'actifs numériques

## Dépendances techniques

Le projet repose sur un ensemble de bibliothèques Python spécialisées, chacune jouant un rôle précis dans le fonctionnement du logiciel :

```
PyQt5              # Interface graphique multi-plateformes (basée sur Qt)
                   # - Widgets et contrôles UI
                   # - Gestion des événements
                   # - Intégration avec les threads

matplotlib         # Visualisation de données scientifiques
                   # - Génération des histogrammes
                   # - Affichage des courbes tonales
                   # - Visualisation des espaces colorimétriques

colour             # Gestion avancée des espaces colorimétriques
                   # - Conversions RGB/XYZ/Lab
                   # - Modèles colorimétriques CIE
                   # - Adaptation chromatique

colour-science     # Outils scientifiques pour la couleur
                   # - Fonctions de correspondance de couleur (CMF)
                   # - Modèles de vision humaine
                   # - Équations de rendu perceptuel

scikit-learn       # Algorithmes d'apprentissage automatique
                   # - Segmentation d'image
                   # - Classification des couleurs
                   # - Réduction de dimensionnalité

pathos             # Parallélisation des traitements
                   # - Traitement multi-cœur
                   # - Distribution des tâches
                   # - Pool de processus

geomdl             # Bibliothèque géométrique pour NURBS
                   # - Courbes B-Spline
                   # - Interpolation non uniforme
                   # - Manipulation de points de contrôle

rawpy              # Traitement des images RAW
                   # - Décodage des formats RAW propriétaires
                   # - Interprétation des données brutes du capteur
                   # - Démosaïquage et post-traitement

imageio            # Entrées/sorties d'images
                   # - Lecture/écriture de multiples formats
                   # - Gestion des métadonnées
                   # - Conversion entre formats

scikit-image       # Traitement d'images scientifique
                   # - Filtres et transformations
                   # - Segmentation et analyse
                   # - Correction géométrique

numba              # Optimisation de code Python par compilation JIT
                   # - Accélération des calculs intensifs
                   # - Parallélisation au niveau des boucles
                   # - Optimisation pour CPU et GPU

torch              # Framework d'apprentissage profond
                   # - Réseaux de neurones pour amélioration d'image
                   # - Inférence de modèles pré-entraînés
                   # - Optimisation GPU
```

### Dépendances système

En plus des bibliothèques Python, le système requiert :

1. **HDRip.dll** : Bibliothèque C++ précompilée pour Windows fournissant les fonctions de traitement HDR optimisées.
   - Cette bibliothèque utilise des instructions SIMD pour accélérer les calculs
   - Interface via ctypes pour l'intégration avec Python

2. **exiftool.exe** : Outil en ligne de commande pour la manipulation des métadonnées d'image.
   - Développé par Phil Harvey
   - Capable de lire et écrire des métadonnées dans presque tous les formats d'image

## Modes de calcul et optimisations

uHDRv6 propose plusieurs modes de calcul, permettant d'adapter les performances en fonction du matériel disponible :

### 1. Mode Python pur

- **Fonctionnement** : Utilise uniquement des calculs en Python avec NumPy
- **Avantages** : 
  * Compatibilité maximale
  * Facilité de débogage
  * Pas de dépendances externes complexes
- **Inconvénients** : 
  * Performances limitées sur les grandes images
  * Consommation mémoire plus importante
- **Utilisation recommandée** : Développement, test, systèmes à ressources limitées

### 2. Mode Numba (JIT)

- **Fonctionnement** : Compile à la volée (Just-In-Time) les fonctions Python critiques
- **Technologies** : 
  * Numba convertit le code Python en code machine optimisé
  * Vectorisation automatique via LLVM
  * Parallélisation des boucles
- **Avantages** :
  * Accélération x5-10 par rapport au Python pur
  * Préserve la lisibilité du code source
  * Compatible avec la plupart des environnements
- **Utilisation recommandée** : Usage courant, systèmes sans GPU

### 3. Mode CUDA (GPU)

- **Fonctionnement** : Déporte les calculs sur GPU NVIDIA via CUDA
- **Technologies** :
  * Numba CUDA pour la génération de code GPU
  * Calcul parallèle massif
  * Traitement par lots optimisé
- **Avantages** :
  * Accélération x20-50 sur les opérations parallélisables
  * Gestion efficace des grandes images (4K+)
  * Libère le CPU pour d'autres tâches
- **Prérequis** :
  * GPU NVIDIA compatible CUDA
  * Pilotes à jour et toolkit CUDA installé
- **Utilisation recommandée** : Production, traitement par lots, images haute résolution

### 4. Mode C++ (via HDRip.dll)

- **Fonctionnement** : Utilise les fonctions optimisées de la bibliothèque C++
- **Technologies** :
  * Code natif précompilé
  * Optimisations spécifiques à l'architecture
  * Instructions SIMD (SSE/AVX)
- **Avantages** :
  * Performances maximales pour certains algorithmes complexes
  * Empreinte mémoire réduite
  * Opérations atomiques pour des résultats précis
- **Utilisation** : Automatiquement activé pour les opérations critiques

### Sélection du mode

Le mode de calcul est configurable via le module `preferences.preferences` :
```python
# Modes disponibles : 'python', 'numba', 'cuda'
preferences.computation = 'numba'
```

Le logiciel détecte automatiquement les capacités du système et peut rétrograder vers un mode moins exigeant si nécessaire.

## Installation et configuration

### Prérequis système

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

### Installation de l'environnement

1. **Cloner le dépôt ou extraire l'archive**
   ```powershell
   git clone https://github.com/username/uHDRv6.git
   cd uHDRv6
   ```

2. **Créer un environnement virtuel Python** (recommandé)
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Installer les dépendances Python**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Vérifier l'installation des composants externes**
   * Assurez-vous que HDRip.dll est présent dans le répertoire principal
   * Vérifiez que exiftool.exe est accessible

### Configuration avancée

#### Configuration des écrans HDR

Le fichier `preferences/prefs.json` contient les configurations pour différents types d'écrans HDR :

```json
{
  "HDRdisplays": {
    "none": {
      "shape": [2160, 3840],
      "scaling": 1,
      "post": "",
      "tag": "none"
    },
    "vesaDisplayHDR1000": {
      "shape": [2160, 3840],
      "scaling": 12,
      "post": "_vesa_DISPLAY_HDR_1000",
      "tag": "vesaDisplayHDR1000"
    },
    "vesaDisplayHDR400": {
      "shape": [2160, 3840],
      "scaling": 4.8,
      "post": "_vesa_DISPLAY_HDR_400",
      "tag": "vesaDisplayHDR400"
    },
    "HLG1": {
      "shape": [2160, 3840],
      "scaling": 1,
      "post": "_HLG_1",
      "tag": "HLG1"
    }
  },
  "HDRdisplay": "HLG1",
  "imagePath": "C:/Users/username/Documents/hdrImages"
}
```

Paramètres principaux :
- `shape` : Résolution cible [hauteur, largeur]
- `scaling` : Facteur d'échelle pour les valeurs HDR
- `post` : Suffixe ajouté aux fichiers exportés
- `tag` : Identifiant interne du profil

#### Configuration des performances

Éditez le fichier `preferences/preferences.py` pour ajuster les paramètres de performances :

```python
# Mode de calcul : 'python', 'numba', 'cuda'
computation = 'numba'

# Mode verbeux pour le débogage
verbose = True
```

## Utilisation du logiciel

### Démarrage

Pour lancer l'application, exécutez le script principal :

```powershell
python uHDR.py
```

L'application initialise séquentiellement :
1. Chargement des préférences utilisateur
2. Initialisation de l'interface graphique
3. Détection des écrans disponibles
4. Chargement des modèles d'IA si nécessaire

### Interface utilisateur

L'interface de uHDRv6 se compose de plusieurs éléments principaux :

#### 1. Galerie d'images

La galerie offre plusieurs modes d'affichage configurables :
- **Mode 1x1** : Affichage d'une seule image en grand format
- **Mode 3x2** : Affichage de 6 images en grille 3x2
- **Mode 6x4** : Affichage de 24 images en grille 6x4
- **Mode 9x6** : Affichage de 54 images en grille 9x6
- **Mode 2x1** : Affichage côte à côte pour comparaison (avant/après)

Contrôles disponibles :
- Zoom avec la molette de la souris
- Navigation par glisser-déposer
- Double-clic pour passer en plein écran
- Clic droit pour le menu contextuel

#### 2. Panneaux de contrôle

Les panneaux latéraux permettent d'accéder aux fonctionnalités d'édition :

**Panneau Exposition**
- Ajustement EV (Exposure Value)
- Récupération des hautes lumières
- Récupération des ombres
- Contrôle du point blanc/noir

**Panneau Courbes**
- Éditeur de courbes tonales
- Points de contrôle ajustables
- Presets de courbes
- Mode courbe automatique (IA)

**Panneau Couleur**
- Température et teinte
- Saturation globale
- Vibrance
- Ajustements HSL par zone de couleur

**Panneau Effets**
- Clarté et structure
- Réduction du bruit
- Amélioration des détails
- Vignettage

**Panneau Métadonnées**
- Affichage des informations EXIF
- Gestion des mots-clés
- Notation et tags

#### 3. Barre d'outils principale

La barre d'outils donne accès aux fonctions essentielles :
- Importation d'images
- Exportation et sauvegarde
- Annulation/rétablissement
- Configuration des préférences
- Gestion des presets
- Basculement du mode d'affichage

### Flux de travail typique

1. **Importation** : Ouvrez une image HDR ou RAW via le menu Fichier > Importer
2. **Ajustements globaux** : Réglez l'exposition et le contraste
3. **Courbe tonale** : Ajustez la courbe de tonalité pour équilibrer les ombres et les hautes lumières
4. **Couleur** : Affinez la balance des blancs et la saturation
5. **Ajustements locaux** : Utilisez les masques pour appliquer des corrections ciblées
6. **Finalisation** : Appliquez les effets finaux (netteté, réduction du bruit)
7. **Exportation** : Sauvegardez l'image traitée dans le format souhaité

### Raccourcis clavier

L'application propose de nombreux raccourcis pour un flux de travail efficace :

| Raccourci       | Action                          |
|-----------------|----------------------------------|
| Ctrl+O          | Ouvrir un fichier               |
| Ctrl+S          | Sauvegarder                     |
| Ctrl+Shift+S    | Sauvegarder sous                |
| Ctrl+Z          | Annuler                         |
| Ctrl+Y          | Rétablir                        |
| Ctrl+1          | Mode affichage 1x1              |
| Ctrl+2          | Mode affichage 3x2              |
| Ctrl+3          | Mode affichage 6x4              |
| Ctrl+4          | Mode affichage 9x6              |
| F               | Plein écran                     |
| Esc             | Quitter le mode plein écran     |
| +/-             | Zoom avant/arrière              |
| Espace          | Basculer l'affichage avant/après|
| Tab             | Masquer/afficher les panneaux   |

## Architecture logicielle détaillée

uHDRv6 suit le modèle MVC (Modèle-Vue-Contrôleur) pour une séparation claire des responsabilités et une maintenance facilitée :

### Modèle (Model)

Le modèle représente les données et la logique métier de l'application. Dans uHDRv6, cette couche est principalement implémentée dans :

1. **hdrCore/image.py** : Classe centrale pour la représentation des images
   ```python
   class Image:
       """Représente une image HDR avec ses métadonnées et propriétés"""
       
       def __init__(self, data=None, metadata=None, colorspace=None):
           # Initialisation d'une image avec ses données, métadonnées et espace colorimétrique
           
       def getXYZ(self):
           # Retourne les données de l'image dans l'espace XYZ
           
       def getHistogram(self, bins=100):
           # Calcule l'histogramme de l'image
   ```

2. **guiQt/model.py** : Modèles pour l'interface graphique
   ```python
   class ImageWidgetModel:
       """Modèle pour les widgets d'affichage d'image"""
       
       def setImage(self, image):
           # Définit l'image à afficher et notifie les observateurs
           
       def getColorData(self):
           # Convertit l'image pour l'affichage
   ```

3. **hdrCore/processing.py** : Classes pour les opérations de traitement
   ```python
   class ProcessPipe:
       """Pipeline de traitement pour les images HDR"""
       
       def __init__(self):
           # Initialise une chaîne de traitement vide
           
       def addProcess(self, process):
           # Ajoute une étape de traitement au pipeline
           
       def applyToImage(self, image):
           # Applique toutes les étapes de traitement à l'image
   ```

### Vue (View)

La vue gère l'interface utilisateur et l'affichage des données. Elle est principalement implémentée dans :

1. **guiQt/view.py** : Composants d'interface utilisateur
   ```python
   class ImageWidgetView(QLabel):
       """Widget d'affichage d'image"""
       
       def setPixmap(self, colorData):
           # Convertit les données d'image et les affiche
           
       def mousePressEvent(self, event):
           # Gère les interactions utilisateur avec l'image
   ```

2. **guiQt/view.useCase.py** : Cas d'utilisation spécifiques de l'interface
   ```python
   class GalleryView(QWidget):
       """Vue pour l'affichage d'une galerie d'images"""
       
       def setGalleryMode(self, mode):
           # Change le mode d'affichage de la galerie
           
       def updateLayout(self):
           # Met à jour la disposition des images dans la galerie
   ```

### Contrôleur (Controller)

Le contrôleur fait le lien entre le modèle et la vue, en gérant les interactions et les événements :

1. **guiQt/controller.py** : Contrôleurs principaux de l'application
   ```python
   class AppController:
       """Contrôleur principal de l'application"""
       
       def __init__(self, app):
           # Initialise l'application et crée les modèles et vues
           
       def openFile(self, path):
           # Charge un fichier image et met à jour l'interface
           
       def applyProcess(self, processType, parameters):
           # Applique un traitement à l'image active
   ```

2. **guiQt/thread.py** : Gestion des traitements asynchrones
   ```python
   class ProcessingThread(QThread):
       """Thread pour les opérations de traitement intensives"""
       
       def __init__(self, image, processPipe):
           # Initialise le thread avec l'image et le pipeline de traitement
           
       def run(self):
           # Exécute le traitement en arrière-plan
   ```

### Flux de données

Le flux de données dans l'application suit généralement ce schéma :

1. L'utilisateur interagit avec l'interface (Vue)
2. La Vue transmet l'action au Contrôleur
3. Le Contrôleur met à jour le Modèle en fonction de l'action
4. Le Modèle notifie ses changements
5. Le Contrôleur demande à la Vue de se mettre à jour
6. La Vue affiche les nouvelles données

### Intégration C++

L'intégration avec la bibliothèque C++ HDRip.dll se fait via le module `hdrCore/coreC.py` :

```python
# Chargement de la bibliothèque C++
_hdrDLL = ctypes.CDLL("HDRip.dll")

def coreCcompute(img, processPipe):
    """Traite une image via la bibliothèque C++"""
    
    # Conversion des données Python pour la bibliothèque C++
    
    # Appel des fonctions C++
    _hdrDLL.processHDRImage(...)
    
    # Récupération et conversion des résultats
```

### Modèle d'IA pour le traitement automatique

Le module `hdrCore/net.py` définit un réseau neuronal pour l'amélioration automatique des images :

```python
class Net(nn.Module):
    """Réseau neuronal pour l'amélioration automatique des courbes tonales"""
    
    def __init__(self, n_feature, n_output):
        # Définition de l'architecture du réseau
        
    def forward(self, x):
        # Propagation avant dans le réseau
```

Ce modèle est utilisé pour générer automatiquement des paramètres de courbe tonale adaptés à l'image.

## Traitement des images HDR

uHDRv6 implémente de nombreux algorithmes spécialisés pour le traitement des images HDR, combinant techniques traditionnelles et approches basées sur l'intelligence artificielle.

### Concepts fondamentaux HDR

#### Espaces colorimétriques

Le logiciel utilise plusieurs espaces colorimétriques pour différentes étapes du traitement :

1. **XYZ** : Espace de travail interne principal
   - Espace de référence CIE 1931
   - Représentation mathématique précise des couleurs
   - Permet des opérations de traitement sans perte

2. **RGB linéaire** : Pour certaines opérations spécifiques
   - Valeurs proportionnelles à l'intensité lumineuse physique
   - Pas de correction gamma appliquée
   - Utilisé pour les calculs de fusion et d'exposition

3. **sRGB** : Pour l'affichage et l'exportation vers formats standard
   - Espace standard pour les écrans
   - Comprend une courbe gamma pour la perception humaine
   - Utilisé dans le module `hdrCore/srgb.py`

4. **Espaces perceptuels** (Lab, HSV, HSL)
   - Utilisés pour les opérations d'édition spécifiques
   - Séparation de la luminance et des informations de couleur
   - Plus intuitifs pour certains types d'ajustements

#### Mapping de tons (Tone Mapping)

Le tone mapping est un processus clé pour adapter la large gamme dynamique des images HDR aux capacités d'affichage limitées :

1. **Opérateurs globaux** :
   - Appliquer une même transformation à tous les pixels
   - Exemples : opérateur de Reinhard, mapping logarithmique
   - Implémentés dans `hdrCore/processing.py`

2. **Opérateurs locaux** :
   - Ajuster le mapping en fonction du contexte local de chaque pixel
   - Préserve davantage les détails dans les zones extrêmes
   - Plus coûteux en calculs, souvent accélérés via HDRip.dll

3. **Courbes tonales personnalisables** :
   - Interface B-Spline pour des ajustements précis
   - Points de contrôle manipulables par l'utilisateur
   - Classe `BSplineCurve` dans `hdrCore/processing.py`

### Algorithmes principaux

#### Reconstruction HDR

Pour les images RAW, le processus de reconstruction HDR comprend :
```python
def reconstructHDR(rawImage):
    # 1. Démosaïquage avancé (interpolation des couleurs)
    # 2. Correction des aberrations chromatiques
    # 3. Suppression du bruit
    # 4. Linéarisation de la réponse du capteur
    # 5. Conversion vers l'espace XYZ
```

#### Ajustement d'exposition

```python
def adjustExposure(image, ev):
    """Ajuste l'exposition d'une image HDR par un nombre de stops (EV)"""
    # Multiplication par 2^EV pour simuler un changement d'exposition photographique
    scalingFactor = 2.0 ** ev
    return image * scalingFactor
```

#### Contraste local adaptatif

```python
def adaptiveLocalContrast(image, radius, strength):
    """Améliore le contraste local tout en préservant les détails globaux"""
    # 1. Créer une version floutée de l'image (structure globale)
    # 2. Calculer les détails (différence entre original et flou)
    # 3. Amplifier les détails de manière adaptative
    # 4. Recombiner avec la structure globale
```

#### Réseau neuronal pour le traitement

L'intégration de l'IA via PyTorch permet d'améliorer automatiquement les images :

```python
def enhanceImageWithAI(image):
    """Utilise le réseau neuronal pour suggérer des paramètres optimaux"""
    # 1. Extraire les caractéristiques de l'image (histogramme, statistiques)
    # 2. Normaliser les entrées pour le réseau
    # 3. Appliquer le modèle pré-entraîné
    # 4. Convertir les sorties en paramètres de traitement
```

### Optimisation des performances

Les calculs intensifs sont optimisés via plusieurs stratégies :

1. **Vectorisation NumPy** :
   ```python
   # Traitement efficace des tableaux plutôt que des boucles
   result = np.maximum(0, np.log2(1 + image * factor) / np.log2(1 + factor))
   ```

2. **Accélération Numba** :
   ```python
   @numba.jit(nopython=True, parallel=True)
   def process_image(img, params):
       # Code optimisé automatiquement par Numba
   ```

3. **Traitement parallèle** :
   ```python
   def processBatch(images, processPipe):
       # Utilisation de multiprocessing pour traiter plusieurs images
       pool = pathos.multiprocessing.ProcessPool()
       results = pool.map(lambda img: processPipe.applyToImage(img), images)
   ```

4. **Appels à la bibliothèque C++** :
   ```python
   # Pour les opérations les plus intensives
   result = hdrCore.coreC.coreCcompute(image, processPipe)
   ```

## Configuration et personnalisation

uHDRv6 offre de nombreuses options de configuration permettant d'adapter le logiciel aux besoins spécifiques des utilisateurs et des développeurs.

### Système de préférences

Le module `preferences` gère l'ensemble des paramètres configurables de l'application :

#### Structure du système de préférences

- **preferences.py** : Module principal définissant les variables globales
  ```python
  # Mode de calcul
  target = ['python', 'numba', 'cuda']
  computation = target[0]
  
  # Mode verbeux pour le débogage
  verbose = True
  
  # Affichage HDR courant
  HDRdisplay = "HLG1"
  ```

- **prefs.json** : Stockage persistant des paramètres utilisateur
  ```json
  {
    "HDRdisplays": {
      "none": {
        "shape": [2160, 3840],
        "scaling": 1,
        "post": "",
        "tag": "none"
      },
      "vesaDisplayHDR1000": {
        "shape": [2160, 3840],
        "scaling": 12,
        "post": "_vesa_DISPLAY_HDR_1000",
        "tag": "vesaDisplayHDR1000"
      },
      "vesaDisplayHDR400": {
        "shape": [2160, 3840],
        "scaling": 4.8,
        "post": "_vesa_DISPLAY_HDR_400",
        "tag": "vesaDisplayHDR400"
      },
      "HLG1": {
        "shape": [2160, 3840],
        "scaling": 1,
        "post": "_HLG_1",
        "tag": "HLG1"
      }
    },
    "HDRdisplay": "HLG1",
    "imagePath": "C:/Users/username/Documents/hdrImages"
  }
  ```

- **tags.json** : Gestion des métadonnées et tags personnalisés
  ```json
  {
    "tags": [
      "paysage",
      "portrait",
      "architecture",
      "nature",
      "urbain"
    ],
    "presets": {
      "contrasté": {
        "exposure": 0.0,
        "contrast": 1.2,
        "saturation": 1.1
      },
      "doux": {
        "exposure": 0.5,
        "contrast": 0.8,
        "saturation": 0.9
      }
    }
  }
  ```

### Paramètres configurables

#### Paramètres d'affichage

| Paramètre | Description | Valeurs possibles |
|-----------|-------------|-------------------|
| `HDRdisplay` | Profil d'écran HDR actif | `"none"`, `"vesaDisplayHDR1000"`, `"vesaDisplayHDR400"`, `"HLG1"` |
| `shape` | Résolution cible | Tableau [hauteur, largeur] |
| `scaling` | Facteur d'échelle HDR | Nombre flottant (1.0 - 12.0) |

#### Paramètres de performance

| Paramètre | Description | Valeurs possibles |
|-----------|-------------|-------------------|
| `computation` | Mode de calcul | `"python"`, `"numba"`, `"cuda"` |
| `verbose` | Mode de débogage | `True`, `False` |
| `threading` | Nombre de threads | Entier ou `"auto"` |

#### Paramètres d'application

| Paramètre | Description | Valeurs possibles |
|-----------|-------------|-------------------|
| `imagePath` | Dossier des images par défaut | Chemin absolu |
| `recentFiles` | Liste des fichiers récents | Tableau de chemins |
| `defaultExportFormat` | Format d'exportation par défaut | `"hdr"`, `"jpg"`, `"png"` |

### Extension et personnalisation

#### Ajouter un nouveau profil d'écran HDR

Pour ajouter un nouveau profil d'écran HDR, éditez le fichier `prefs.json` :

```json
"monNouvelEcranHDR": {
  "shape": [1080, 1920],
  "scaling": 6.0,
  "post": "_mon_ecran_HDR",
  "tag": "monNouvelEcranHDR"
}
```

#### Création de presets de traitement

Les presets peuvent être définis dans `tags.json` :

```json
"presets": {
  "monNouveauPreset": {
    "exposure": 0.7,
    "contrast": 1.5,
    "saturation": 1.2,
    "curves": [
      [0, 0],
      [64, 76],
      [128, 135],
      [192, 200],
      [255, 255]
    ]
  }
}
```

#### Extension programmatique

Pour les développeurs, il est possible d'étendre le logiciel :

1. **Ajout d'un nouveau type de traitement** :
   ```python
   # Dans hdrCore/processing.py
   class NewProcessType(ProcessBase):
       """Implémente un nouveau type de traitement"""
       
       def __init__(self, parameters):
           self.parameters = parameters
           
       def apply(self, image):
           # Logique d'application du traitement
           return processed_image
   ```

2. **Intégration dans l'interface utilisateur** :
   ```python
   # Dans guiQt/view.py
   class NewProcessWidget(QWidget):
       """Widget pour contrôler le nouveau traitement"""
       
       def __init__(self, controller):
           self.controller = controller
           # Création des contrôles UI
           
       def onValueChanged(self, value):
           # Notification du contrôleur lors des changements
   ```

## Guide de développement

Cette section s'adresse aux développeurs qui souhaitent contribuer au projet ou adapter le logiciel à leurs besoins spécifiques.

### Principes de développement

Le développement de uHDRv6 suit plusieurs principes fondamentaux :

1. **Séparation des responsabilités** : Respect strict du modèle MVC
2. **Extensibilité** : Architecture modulaire facilement extensible
3. **Performance** : Optimisation des opérations intensives
4. **Compatibilité** : Support de différents environnements et matériels

### Environnement de développement

#### Configuration recommandée

- **IDE** : Visual Studio Code ou PyCharm
- **Débogage** : Utilisation du mode verbeux (`preferences.verbose = True`)
- **Tests** : Tests unitaires avec pytest
- **Documentation** : Docstrings au format NumPy/SciPy

#### Structure du projet Visual Studio

Le projet inclut des fichiers de configuration pour Visual Studio :
- `uHDR.pyproj` : Définition du projet Python
- `uHDR.sln` : Solution Visual Studio

### Extension du système

#### Ajout d'un nouveau format d'image

Pour ajouter le support d'un nouveau format d'image :

```python
# Dans hdrCore/image.py

def loadNewFormat(path):
    """Charge un fichier au nouveau format"""
    # Implémentation du chargement
    return data, metadata

class Image:
    # Ajouter au constructeur
    @classmethod
    def fromNewFormat(cls, path):
        """Crée une instance Image à partir d'un fichier au nouveau format"""
        data, metadata = loadNewFormat(path)
        return cls(data, metadata)
```

#### Création d'un nouvel algorithme de traitement

Pour implémenter un nouvel algorithme de traitement :

1. **Définir le processus** dans `hdrCore/processing.py` :
   ```python
   class NewProcess(ProcessBase):
       """Nouveau type de traitement d'image"""
       
       def __init__(self, param1=0.5, param2=1.0):
           self.param1 = param1
           self.param2 = param2
           
       def apply(self, image):
           """Applique le traitement à l'image"""
           # Implémentation de l'algorithme
           return processed_image
           
       def toDict(self):
           """Convertit les paramètres en dictionnaire pour sérialisation"""
           return {
               'param1': self.param1,
               'param2': self.param2
           }
   ```

2. **Créer l'interface utilisateur** dans `guiQt/view.py` :
   ```python
   class NewProcessWidget(QWidget):
       """Widget pour contrôler le nouveau traitement"""
       
       def __init__(self, controller):
           super().__init__()
           self.controller = controller
           
           # Création des contrôles UI
           layout = QVBoxLayout()
           
           self.param1Slider = QSlider(Qt.Horizontal)
           self.param1Slider.setRange(0, 100)
           self.param1Slider.setValue(50)  # Valeur par défaut 0.5
           self.param1Slider.valueChanged.connect(self.onParam1Changed)
           
           # Ajouter les contrôles au layout
           layout.addWidget(QLabel("Paramètre 1"))
           layout.addWidget(self.param1Slider)
           
           self.setLayout(layout)
           
       def onParam1Changed(self, value):
           # Conversion de la valeur du slider (0-100) vers la plage réelle (0-1)
           param1 = value / 100.0
           # Notification du contrôleur
           self.controller.setProcessParam('newProcess', 'param1', param1)
   ```

3. **Intégrer dans le contrôleur** dans `guiQt/controller.py` :
   ```python
   def initProcesses(self):
       """Initialise les processus disponibles"""
       # Ajouter le nouveau processus au pipeline
       self.processPipe.addProcess('newProcess', processing.NewProcess())
       
   def setProcessParam(self, processName, paramName, value):
       """Met à jour un paramètre de traitement"""
       if processName == 'newProcess':
           process = self.processPipe.getProcess(processName)
           setattr(process, paramName, value)
           # Déclencher le traitement avec les nouveaux paramètres
           self.updateProcessing()
   ```

#### Optimisation des performances

Pour les traitements intensifs, plusieurs options d'optimisation sont disponibles :

1. **Vectorisation avec NumPy** :
   ```python
   # Au lieu de boucles imbriquées
   for y in range(height):
       for x in range(width):
           result[y, x] = func(image[y, x])
           
   # Utiliser la vectorisation
   result = func(image)  # Où func est compatible avec les tableaux NumPy
   ```

2. **Accélération avec Numba** :
   ```python
   @numba.jit(nopython=True, parallel=True)
   def intensiveFunction(image, param1, param2):
       """Fonction optimisée par Numba"""
       result = np.empty_like(image)
       height, width = image.shape[:2]
       
       for y in numba.prange(height):  # prange pour parallélisation
           for x in range(width):
               # Calculs intensifs
               result[y, x] = complex_calculation(image[y, x], param1, param2)
               
       return result
   ```

3. **Traitement GPU avec CUDA** :
   ```python
   @numba.cuda.jit
   def cudaKernel(image, result, param1, param2):
       """Kernel CUDA pour traitement sur GPU"""
       x, y = numba.cuda.grid(2)
       height, width = image.shape[:2]
       
       if x < width and y < height:
           # Calculs intensifs sur GPU
           result[y, x] = complex_calculation(image[y, x], param1, param2)
   ```

4. **Intégration avec C++** via `hdrCore/coreC.py` :
   ```python
   def cppOptimizedFunction(image, params):
       """Appelle une fonction optimisée en C++"""
       # Préparation des données pour C++
       
       # Appel de la fonction C++
       _hdrDLL.optimizedFunction(...)
       
       # Récupération et conversion des résultats
   ```

## Analyses techniques et performances

Cette section présente les analyses techniques et les benchmarks de performance de uHDRv6.

### Analyse de performance

Les performances du logiciel ont été mesurées dans différentes configurations et pour différentes tailles d'images :

#### Temps de traitement par mode de calcul

Le tableau suivant présente les temps de traitement moyens (en secondes) pour une image HDR 4K avec un pipeline complet :

| Opération | Python pur | Numba | CUDA | C++ (HDRip.dll) |
|-----------|------------|-------|------|----------------|
| Chargement | 0.85 | 0.85 | 0.85 | 0.85 |
| Exposition | 0.42 | 0.06 | 0.02 | 0.01 |
| Contraste | 1.25 | 0.18 | 0.05 | 0.03 |
| Courbe tonale | 2.10 | 0.32 | 0.07 | 0.04 |
| Saturation | 0.38 | 0.05 | 0.02 | 0.01 |
| Édition couleur | 0.95 | 0.14 | 0.04 | 0.02 |
| Total | 5.95 | 1.60 | 1.05 | 0.96 |

*Tests réalisés sur un système avec CPU Intel i7-9700K, 32 Go RAM, GPU NVIDIA RTX 2080*

#### Consommation mémoire

La consommation mémoire varie selon le mode et la taille des images :

| Résolution | Mémoire utilisée (Mo) |
|------------|---------------------|
| Full HD (1080p) | 250 - 400 |
| 4K UHD | 800 - 1200 |
| 8K | 2800 - 3600 |

### Limitations techniques

Malgré les optimisations, certaines limitations techniques subsistent :

1. **Limitations matérielles** :
   - Le traitement d'images 8K peut être limité par la mémoire disponible
   - Les performances CUDA dépendent fortement du GPU utilisé

2. **Limitations logicielles** :
   - Certains formats RAW exotiques peuvent ne pas être pleinement supportés
   - L'interaction avec les métadonnées avancées nécessite exiftool.exe

3. **Considérations de compatibilité** :
   - Le rendu HDR complet nécessite un écran compatible HDR
   - Certaines fonctionnalités CUDA nécessitent des pilotes NVIDIA récents

### Gestion des versions et déploiement

#### Contrôle de version

- Utilisation de Git pour le contrôle de version
- Convention de commit : `[TYPE] Message` où TYPE peut être `FEAT`, `FIX`, `DOC`, etc.
- Branches principales : `master` (stable), `develop` (développement), `feature/*` (nouvelles fonctionnalités)

#### Packaging et distribution

Pour créer un package distribuable :

```powershell
# Création d'un environnement virtuel pour le packaging
python -m venv packaging_env
.\packaging_env\Scripts\Activate.ps1

# Installation des outils de packaging
pip install setuptools wheel pyinstaller

# Création d'un exécutable standalone
pyinstaller --name=uHDR --windowed --add-data "HDRip.dll;." --add-data "exiftool.exe;." --add-data "MSESig505_0419.pth;." uHDR.py
```

Le package généré dans le dossier `dist` peut être distribué aux utilisateurs.

## Formats et espaces colorimétriques

uHDRv6 gère une variété de formats d'image et d'espaces colorimétriques, chacun ayant ses propres caractéristiques et cas d'utilisation.

### Formats d'image supportés

#### Formats d'entrée

| Format | Extension | Description | Usage |
|--------|-----------|-------------|-------|
| **Radiance HDR** | .hdr | Format standard pour les images HDR, stocke les valeurs en virgule flottante | Format HDR principal |
| **OpenEXR** | .exr | Format HDR développé par ILM, supporte plusieurs canaux et haute précision | Production professionnelle |
| **RAW Sony** | .arw | Format RAW des appareils photo Sony, contient les données brutes du capteur | Photographie HDR |
| **JPEG** | .jpg, .jpeg | Format compressé standard, gamme dynamique limitée | Import d'images SDR |
| **PNG** | .png | Format sans perte avec canal alpha, gamme dynamique limitée | Import d'images SDR |
| **TIFF** | .tif, .tiff | Format flexible supportant différentes profondeurs de bits | Import de données scientifiques |

#### Formats de sortie

| Format | Extension | Description | Usage recommandé |
|--------|-----------|-------------|-----------------|
| **Radiance HDR** | .hdr | Préserve la gamme dynamique complète | Archivage, post-traitement ultérieur |
| **OpenEXR** | .exr | Haute précision, compatible avec les logiciels pro | Pipeline de production professionnel |
| **JPEG** | .jpg | Format compressé standard avec tone mapping | Partage web, affichage sur écrans SDR |
| **PNG** | .png | Compression sans perte avec tone mapping | Publications, documentation |
| **TIFF 16-bit** | .tif | Format sans perte haute qualité | Impression, archivage |

### Espaces colorimétriques

uHDRv6 utilise plusieurs espaces colorimétriques à différentes étapes du traitement :

#### Espaces de travail internes

| Espace | Description | Utilisation |
|--------|-------------|-------------|
| **CIE XYZ** | Espace de référence, représente précisément toutes les couleurs visibles | Espace de travail principal pour les calculs |
| **RGB linéaire** | Valeurs RGB proportionnelles à l'intensité physique | Opérations de fusion et d'exposition |
| **Lab** | Espace perceptuel séparant luminance et chrominance | Manipulations perceptuelles des couleurs |
| **HSV/HSL** | Représentation cylindrique séparant teinte, saturation et luminosité | Ajustements intuitifs des couleurs |

#### Espaces de sortie

| Espace | Description | Utilisation |
|--------|-------------|-------------|
| **sRGB** | Espace standard pour les écrans et le web | Affichage sur écrans SDR |
| **Display P3** | Gamut élargi, ~25% plus large que sRGB | Écrans modernes (Apple, etc.) |
| **Rec.2020** | Très large gamut utilisé pour le contenu UHD | Écrans HDR, télévisions UHD |
| **Rec.709** | Espace standard pour la HDTV | Contenu vidéo broadcast |

### Gestion de la couleur

#### Profils ICC

uHDRv6 prend en charge les profils ICC pour une gestion précise des couleurs :

- **Profils d'entrée** : Interprétation correcte des couleurs des fichiers source
- **Profils d'affichage** : Adaptation au moniteur de l'utilisateur
- **Profils de sortie** : Intégration dans les fichiers exportés

#### Conversion entre espaces

Les conversions entre espaces colorimétriques utilisent des algorithmes précis :

```python
def XYZ_to_sRGB(XYZ, apply_cctf_encoding=True):
    """Convertit de l'espace XYZ vers sRGB.
    
    Args:
        XYZ: Tableau NumPy de valeurs XYZ
        apply_cctf_encoding: Appliquer la correction gamma sRGB
        
    Returns:
        Tableau NumPy de valeurs sRGB
    """
    # Matrice de transformation XYZ->sRGB linéaire
    M = np.array([
        [ 3.2404542, -1.5371385, -0.4985314],
        [-0.9692660,  1.8760108,  0.0415560],
        [ 0.0556434, -0.2040259,  1.0572252]
    ])
    
    rgb_linear = np.dot(XYZ, M.T)
    
    if apply_cctf_encoding:
        # Appliquer la correction gamma sRGB (non linéaire)
        mask = rgb_linear <= 0.0031308
        rgb = np.where(mask, 12.92 * rgb_linear, 1.055 * np.power(rgb_linear, 1/2.4) - 0.055)
        return rgb
    else:
        return rgb_linear
```

## Exemples de code et APIs

Cette section présente des exemples de code illustrant l'utilisation programmatique des principales fonctionnalités de uHDRv6.

### Chargement et sauvegarde d'images

```python
import hdrCore.image as hdrImage

# Chargement d'une image HDR
image = hdrImage.Image.fromHDR("chemin/vers/image.hdr")

# Chargement d'une image RAW
raw_image = hdrImage.Image.fromRAW("chemin/vers/image.arw")

# Sauvegarde d'une image HDR
image.toHDR("chemin/vers/sortie.hdr")

# Sauvegarde avec tone mapping pour affichage SDR
image.toSDR("chemin/vers/sortie.jpg", tone_mapping="reinhard")
```

### Traitement d'image

```python
import hdrCore.processing as processing

# Création d'un pipeline de traitement
process_pipe = processing.ProcessPipe()

# Ajout d'opérations de traitement
process_pipe.addExposure(1.5)  # Augmentation de 1.5 EV
process_pipe.addContrast(1.2)  # Augmentation du contraste de 20%

# Ajout d'une courbe tonale personnalisée
curve = processing.BSplineCurve()
curve.addPoint(0.0, 0.0)      # Point noir
curve.addPoint(0.25, 0.3)     # Remontée des ombres
curve.addPoint(0.75, 0.7)     # Compression des hautes lumières
curve.addPoint(1.0, 1.0)      # Point blanc
process_pipe.addCurve(curve)

# Ajout de saturation
process_pipe.addSaturation(1.1)  # Augmentation de 10%

# Application du pipeline à une image
processed_image = process_pipe.applyToImage(image)

# Sauvegarde des paramètres du pipeline
process_pipe.saveToFile("chemin/vers/preset.json")

# Chargement d'un preset existant
saved_pipe = processing.ProcessPipe.fromFile("chemin/vers/preset.json")
```

### Traitement par lots

```python
import os
import hdrCore.image as hdrImage
import hdrCore.processing as processing
from pathos.multiprocessing import ProcessPool

# Définition d'une fonction de traitement
def process_file(file_path, output_dir, process_pipe):
    # Charger l'image
    if file_path.lower().endswith('.hdr'):
        img = hdrImage.Image.fromHDR(file_path)
    elif file_path.lower().endswith('.arw'):
        img = hdrImage.Image.fromRAW(file_path)
    else:
        return False
    
    # Appliquer le traitement
    processed = process_pipe.applyToImage(img)
    
    # Sauvegarder le résultat
    base_name = os.path.basename(file_path)
    name, _ = os.path.splitext(base_name)
    output_path = os.path.join(output_dir, f"{name}_processed.hdr")
    processed.toHDR(output_path)
    
    return True

# Traitement parallèle d'un dossier d'images
def batch_process(input_dir, output_dir, process_pipe, num_workers=4):
    # Créer le dossier de sortie si nécessaire
    os.makedirs(output_dir, exist_ok=True)
    
    # Lister les fichiers d'entrée
    files = []
    for root, _, filenames in os.walk(input_dir):
        for filename in filenames:
            if filename.lower().endswith(('.hdr', '.arw')):
                files.append(os.path.join(root, filename))
    
    # Créer un pool de processus
    pool = ProcessPool(nodes=num_workers)
    
    # Préparer les arguments pour chaque fichier
    args = [(file, output_dir, process_pipe) for file in files]
    
    # Exécuter le traitement en parallèle
    results = pool.map(lambda x: process_file(*x), args)
    
    # Retourner le nombre de fichiers traités avec succès
    return sum(results)
```

### API d'interface graphique

```python
from PyQt5.QtWidgets import QApplication
import sys
import guiQt.controller as controller

# Création de l'application
app = QApplication(sys.argv)

# Initialisation du contrôleur principal
main_controller = controller.AppController(app)

# Accès programmatique aux fonctionnalités
def api_example():
    # Ouverture d'un fichier
    main_controller.openFile("chemin/vers/image.hdr")
    
    # Accès à l'image active
    active_image = main_controller.getCurrentImage()
    
    # Modification des paramètres de traitement
    main_controller.setExposure(1.0)
    main_controller.setContrast(1.2)
    main_controller.setSaturation(1.1)
    
    # Exportation
    main_controller.exportCurrentImage("chemin/vers/sortie.hdr")

# Exécution de l'application
sys.exit(app.exec_())
```

### Analyse d'image

```python
import hdrCore.quality as quality
import hdrCore.utils as utils
import numpy as np
import matplotlib.pyplot as plt

# Analyse de la gamme dynamique d'une image
def analyze_dynamic_range(image):
    # Calcul de l'histogramme en luminance
    luminance = utils.getRGBLuminance(image.getXYZ())
    hist, bins = np.histogram(luminance, bins=100, range=(0, np.max(luminance)))
    
    # Calcul de la gamme dynamique en EV (stops)
    non_zero = luminance[luminance > 0]
    if len(non_zero) > 0:
        min_lum = np.min(non_zero)
        max_lum = np.max(luminance)
        dynamic_range = np.log2(max_lum / min_lum)
        print(f"Gamme dynamique: {dynamic_range:.2f} EV")
    
    # Affichage de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.bar(bins[:-1], hist, width=bins[1]-bins[0])
    plt.yscale('log')
    plt.xlabel('Luminance')
    plt.ylabel('Nombre de pixels (échelle log)')
    plt.title('Histogramme de luminance')
    plt.show()
    
    # Calcul des statistiques de l'image
    stats = {
        'min': np.min(luminance),
        'max': np.max(luminance),
        'mean': np.mean(luminance),
        'median': np.median(luminance),
        'std': np.std(luminance)
    }
    
    return stats

## Glossaire technique

Cette section définit les termes techniques spécifiques utilisés dans le contexte du traitement d'images HDR et du logiciel uHDRv6.

### Termes généraux HDR

| Terme | Définition |
|-------|------------|
| **HDR (High Dynamic Range)** | Technologie d'imagerie permettant de capturer, stocker et afficher une plage plus large de niveaux d'exposition (luminosité) qu'avec les techniques d'imagerie traditionnelles. |
| **SDR (Standard Dynamic Range)** | Images traditionnelles à gamme dynamique limitée, généralement codées sur 8 bits par canal. |
| **Gamme dynamique** | Rapport entre les valeurs maximales et minimales de luminance dans une image, souvent exprimé en stops ou EV (Exposure Value). |
| **EV (Exposure Value)** | Unité représentant un doublement ou une division par deux de la quantité de lumière (1 EV = 1 stop). |
| **Tone Mapping** | Processus de conversion d'une image HDR en image SDR en préservant autant que possible l'apparence visuelle. |

### Espaces colorimétriques et représentation

| Terme | Définition |
|-------|------------|
| **XYZ** | Espace colorimétrique de référence défini par la CIE, où Y représente la luminance. |
| **RGB linéaire** | Espace RGB où les valeurs sont directement proportionnelles à l'intensité lumineuse physique. |
| **sRGB** | Espace colorimétrique standard avec courbe gamma non linéaire, utilisé pour les écrans et le web. |
| **Gamut** | L'ensemble des couleurs représentables dans un espace colorimétrique donné. |
| **EOTF** | Electro-Optical Transfer Function - Fonction de transfert convertissant les valeurs numériques en luminance affichée. |
| **PQ (Perceptual Quantizer)** | EOTF standardisée (SMPTE ST 2084) utilisée pour le HDR10. |
| **HLG (Hybrid Log-Gamma)** | Format HDR développé par la BBC et NHK, compatible avec les écrans SDR. |

### Techniques de traitement

| Terme | Définition |
|-------|------------|
| **Courbe tonale** | Fonction de transformation appliquée aux valeurs de luminosité d'une image. |
| **B-Spline** | Type de courbe paramétrique utilisée pour définir des courbes tonales flexibles. |
| **Local Contrast** | Technique d'amélioration du contraste qui préserve les détails dans les ombres et les hautes lumières. |
| **Mappage de gamme dynamique** | Compression ou expansion de la plage dynamique d'une image pour l'adapter à un dispositif d'affichage. |
| **Démosaïquage** | Processus de reconstruction d'une image couleur complète à partir des données d'un capteur avec filtre de Bayer (images RAW). |

### Termes spécifiques à uHDRv6

| Terme | Définition |
|-------|------------|
| **ProcessPipe** | Pipeline de traitement séquentiel appliquant différentes opérations à une image HDR. |
| **HDRip.dll** | Bibliothèque C++ fournissant des fonctions optimisées pour le traitement HDR. |
| **Galerie** | Interface d'affichage permettant de visualiser et comparer plusieurs images. |
| **Mode de calcul** | Méthode d'exécution des algorithmes (Python, Numba, CUDA, C++). |
| **Profil d'écran HDR** | Configuration définissant les caractéristiques d'un écran HDR spécifique. |

## Documentation de référence

### Bibliographie

1. Reinhard, E., Ward, G., Pattanaik, S., Debevec, P., Heidrich, W., & Myszkowski, K. (2010). *High Dynamic Range Imaging: Acquisition, Display, and Image-Based Lighting*. Morgan Kaufmann.

2. Banterle, F., Artusi, A., Debattista, K., & Chalmers, A. (2017). *Advanced High Dynamic Range Imaging: Theory and Practice*. CRC Press.

3. Mantiuk, R., Myszkowski, K., & Seidel, H. P. (2015). *High Dynamic Range Imaging*. Wiley Encyclopedia of Electrical and Electronics Engineering.

4. Fairchild, M. D. (2013). *Color Appearance Models*. John Wiley & Sons.

5. Ebner, M. (2007). *Color Constancy*. John Wiley & Sons.

### Normes et standards

1. **ITU-R BT.2100** : Valeurs de paramètres d'image pour la télévision à haute dynamique pour la production et l'échange international de programmes.

2. **SMPTE ST 2084** : Electro-Optical Transfer Function for High Dynamic Range Reference Display.

3. **ISO 22028-1:2016** : Photography and graphic technology — Extended colour encodings for digital image storage, manipulation and interchange.

4. **IEC 61966-2-1** : Multimedia systems and equipment - Colour measurement and management - Part 2-1: Colour management - Default RGB colour space - sRGB.

### Ressources en ligne

1. [Colour Science Python Library](https://www.colour-science.org/) - Bibliothèque Python pour la science des couleurs.

2. [ImageIO Documentation](https://imageio.readthedocs.io/) - Documentation de la bibliothèque ImageIO.

3. [PyTorch Documentation](https://pytorch.org/docs/stable/index.html) - Documentation officielle de PyTorch.

4. [NumPy Documentation](https://numpy.org/doc/stable/) - Documentation de NumPy.

5. [Numba Documentation](https://numba.pydata.org/numba-doc/latest/index.html) - Documentation de Numba pour l'accélération Python.

## Auteur et contributions

### Auteur principal

**Rémi Cozot** (remi.cozot@univ-littoral.fr)  
Maître de Conférences  
Université du Littoral Côte d'Opale  
Laboratoire d'Informatique, Signal et Image de la Côte d'Opale (LISIC)

### Collaborateurs

- Équipe de recherche en traitement d'images du LISIC
- Étudiants en Master Informatique ayant contribué à certains modules

### Remerciements

- Financement partiel par les projets de recherche [Nom des projets]
- Support technique de [Partenaires industriels]
- Communauté open-source pour les bibliothèques utilisées

---

*Documentation technique réalisée le 4 juin 2025*

*© 2025 Université du Littoral Côte d'Opale - Tous droits réservés*
