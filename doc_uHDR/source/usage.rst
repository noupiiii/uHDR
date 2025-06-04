Guide d'utilisation
===================

Interface utilisateur
---------------------

L'interface de uHDRv6 se compose de plusieurs éléments principaux :

Galerie d'images
~~~~~~~~~~~~~~~~

La galerie offre plusieurs modes d'affichage configurables :

- **Mode 1x1** : Affichage d'une seule image en grand format
- **Mode galerie** : Comparaison de plusieurs images côte à côte
- **Mode avant/après** : Comparaison des modifications appliquées

Outils d'édition
~~~~~~~~~~~~~~~~

L'interface propose plusieurs outils d'édition organisés en catégories :

**Ajustements globaux** :

- Exposition (EV, stops)
- Contraste (global et local)
- Saturation et vibrance
- Balance des blancs

**Courbes tonales** :

- Courbes paramétriques
- Courbes B-Spline
- Manipulation par points de contrôle
- Courbes automatiques basées sur IA

**Édition sélective** :

- Édition par zones de luminance
- Masques par luminosité
- Corrections locales

**Gestion des couleurs** :

- Ajustements HSL
- Optimisation colorimétrique
- Mapping de gammes de couleurs

Workflow typique
---------------

1. **Importation des images**
   
   - Glisser-déposer des fichiers dans la galerie
   - Formats supportés : .hdr, .arw, .jpg, .png
   - Chargement automatique des métadonnées

2. **Prévisualisation et sélection**
   
   - Navigation dans la galerie
   - Sélection des images à traiter
   - Prévisualisation sur différents types d'écrans

3. **Édition et retouche**
   
   - Application des ajustements globaux
   - Utilisation des courbes tonales
   - Corrections sélectives si nécessaire

4. **Exportation**
   
   - Choix du format de sortie
   - Configuration des paramètres d'exportation
   - Sauvegarde avec préservation des métadonnées

Formats supportés
----------------

Importation
~~~~~~~~~~~

* **Formats HDR natifs** : Support du format Radiance HDR (.hdr) stockant les valeurs en virgule flottante
* **Formats RAW** : Support des fichiers RAW Sony (.arw) avec préservation de la gamme dynamique complète
* **Formats SDR** : Importation des formats traditionnels (.jpg, .png) avec conversion vers l'espace HDR

Le processus d'importation inclut :

- Décodage des métadonnées techniques via exiftool
- Conversion vers l'espace colorimétrique de travail interne (XYZ)
- Préservation des données originales pour un traitement non destructif

Exportation
~~~~~~~~~~~

* **Formats de sortie** :
  
  - Radiance HDR (.hdr) pour préserver la gamme dynamique complète
  - JPEG/PNG avec tone mapping optimisé pour les écrans SDR
  - Formats spéciaux pour écrans HDR spécifiques

* **Options d'exportation** :
  
  - Résolution personnalisable
  - Préservation des métadonnées
  - Compression paramétrable
  - Profils colorimétriques intégrés

Visualisation HDR
-----------------

Support multi-écrans
~~~~~~~~~~~~~~~~~~~~

* **Détection automatique** : Le logiciel détecte et utilise de manière optimisée les moniteurs HDR
* **Modes d'affichage** : 
  
  - Mode galerie (comparaison d'images)
  - Mode plein écran (visualisation détaillée)
  - Mode avant/après (comparaison des modifications)

* **Prévisualisation adaptative** : Simulation du rendu sur différents types d'écrans HDR
  
  - Profils VESA DisplayHDR (400/1000 nits)
  - Format HLG (Hybrid Log-Gamma)

Traitement par lots
------------------

Pipeline de traitement
~~~~~~~~~~~~~~~~~~~~~~

* **Application d'ajustements multiples** : Appliquez les mêmes modifications à plusieurs images simultanément
* **Profils d'édition** : Sauvegardez et chargez des configurations de traitement
* **Traitement parallèle** : Utilisation des multiples cœurs du processeur pour accélérer le traitement
* **File d'attente** : Gestion des tâches de traitement en arrière-plan

Configuration des profils
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Appliquez les modifications désirées sur une image de référence
2. Sauvegardez le profil via le menu "Profils"
3. Sélectionnez les images à traiter
4. Appliquez le profil sauvegardé à toutes les images sélectionnées

Conseils d'utilisation
----------------------

Performance optimale
~~~~~~~~~~~~~~~~~~~~

- Utilisez le mode de calcul "numba" pour un bon compromis performance/compatibilité
- Activez le mode CUDA si vous disposez d'un GPU NVIDIA compatible
- Fermez les autres applications gourmandes en mémoire lors du traitement d'images 4K

Qualité d'image
~~~~~~~~~~~~~~~

- Travaillez toujours sur les fichiers originaux (RAW ou HDR natif)
- Évitez les ajustements excessifs qui peuvent introduire des artefacts
- Utilisez les courbes automatiques basées sur IA comme point de départ
- Prévisualisez le résultat sur votre écran cible avant l'exportation