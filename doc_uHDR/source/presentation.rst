Présentation générale
====================

uHDRv6 est un logiciel d'édition d'images HDR (High Dynamic Range) développé par Rémi Cozot (remi.cozot@univ-littoral.fr). Cette version dispose d'un cœur de traitement écrit en C++ (HDRip.dll) et d'une interface graphique développée en Python avec PyQt5.

Qu'est-ce que le HDR ?
---------------------

Le HDR (High Dynamic Range) permet de manipuler des images avec un contraste, une luminosité et une richesse de couleurs bien supérieurs aux images standard (SDR - Standard Dynamic Range). Cette approche est particulièrement utile pour les photographies captant des scènes à fort contraste ou pour préparer des contenus destinés aux écrans HDR modernes.

Contexte technique
------------------

uHDRv6 fournit les outils nécessaires pour:

- Manipuler les images HDR (.hdr) et RAW (.arw)
- Convertir entre différents formats et espaces colorimétriques
- Appliquer des courbes tonales avancées
- Optimiser le rendu pour différents types d'écrans HDR

Architecture générale
--------------------

Le projet s'articule autour de trois couches principales :

1. **Couche de présentation** (guiQt) : Gère l'interface utilisateur et les interactions
2. **Couche métier** (hdrCore) : Contient la logique de traitement d'images HDR
3. **Couche de données** (preferences) : Gère la persistance des paramètres

L'application utilise également plusieurs composants externes :

- **HDRip.dll** : Bibliothèque C++ qui fournit des algorithmes optimisés pour le traitement HDR
- **exiftool.exe** : Outil tiers pour la manipulation des métadonnées d'images
- **MSESig505_0419.pth** : Modèle PyTorch pré-entraîné pour l'amélioration automatique des images

Auteur et Contact
----------------

Ce logiciel a été développé par **Rémi Cozot** de l'Université du Littoral Côte d'Opale.

Contact : remi.cozot@univ-littoral.fr
