Fonctionnalités détaillées
==========================

Le logiciel uHDRv6 offre plusieurs fonctionnalités avancées pour le traitement des images HDR :

Importation et formats supportés
--------------------------------

Formats HDR natifs
~~~~~~~~~~~~~~~~~

* **Format Radiance HDR (.hdr)** : Support complet du format standard pour les images HDR
  
  - Stockage des valeurs en virgule flottante
  - Préservation de la gamme dynamique complète
  - Compatibilité avec les outils HDR standards

Formats RAW
~~~~~~~~~~~

* **Fichiers RAW Sony (.arw)** : Support optimisé pour les appareils Sony
  
  - Préservation de la gamme dynamique complète du capteur
  - Décodage des données brutes
  - Interprétation correcte de la matrice de couleur

Formats SDR traditionnels
~~~~~~~~~~~~~~~~~~~~~~~~

* **JPEG, PNG** : Importation avec conversion intelligente vers l'espace HDR
  
  - Expansion de la gamme dynamique
  - Préservation des détails
  - Conversion vers l'espace colorimétrique de travail

Processus d'importation
~~~~~~~~~~~~~~~~~~~~~~

Le processus d'importation automatisé inclut :

1. **Décodage des métadonnées** : Extraction via exiftool des informations EXIF, IPTC, XMP
2. **Conversion colorimétrique** : Transformation vers l'espace colorimétrique de travail interne (XYZ)
3. **Préservation des données** : Sauvegarde des données originales pour un traitement non destructif
4. **Génération de prévisualisations** : Création d'aperçus optimisés pour l'affichage

Outils d'édition avancés
------------------------

Ajustements globaux
~~~~~~~~~~~~~~~~~~

**Exposition**
  - Réglage en valeurs EV (Exposure Value)
  - Compensation par stops photographiques
  - Préservation des hautes lumières et des ombres

**Contraste**
  - Contraste global pour l'ensemble de l'image
  - Contraste local pour préserver les détails
  - Algorithmes adaptatifs pour éviter l'écrêtage

**Saturation et Vibrance**
  - Saturation uniforme sur toutes les couleurs
  - Vibrance intelligente préservant les tons chair
  - Protection contre la sursaturation

**Balance des blancs**
  - Correction de la température de couleur
  - Ajustement du tint (magenta/vert)
  - Préservation de la neutralité des zones grises

Courbes tonales avancées
~~~~~~~~~~~~~~~~~~~~~~~

**Courbes paramétriques**
  - Contrôle par zones (ombres, tons moyens, hautes lumières)
  - Ajustement de la luminosité et du contraste par zone
  - Interface intuitive avec prévisualisation temps réel

**Courbes B-Spline**
  - Manipulation précise par points de contrôle
  - Lissage automatique entre les points
  - Support des courbes complexes

**Courbes automatiques basées sur IA**
  - Analyse intelligente du contenu de l'image
  - Optimisation automatique de la courbe tonale
  - Adaptation au type de scène (portrait, paysage, etc.)

Édition sélective
~~~~~~~~~~~~~~~~

**Masques par luminance**
  - Sélection automatique des zones par niveau de luminosité
  - Ajustements ciblés sur les ombres ou les hautes lumières
  - Transitions douces entre les zones

**Corrections locales**
  - Outils de pinceau pour les corrections précises
  - Masques personnalisés
  - Ajustements indépendants par zone

Gestion avancée des couleurs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Ajustements HSL**
  - Contrôle indépendant de la teinte (Hue)
  - Ajustement de la saturation par plage de couleurs
  - Modification de la luminosité par couleur

**Optimisation colorimétrique**
  - Adaptation aux profils d'écran spécifiques
  - Optimisation pour différents espaces colorimétriques
  - Préservation de la cohérence des couleurs

**Mapping de gammes de couleurs**
  - Conversion entre espaces colorimétriques étendus
  - Préservation des couleurs hors gamut
  - Adaptation perceptuelle des couleurs

Intelligence artificielle intégrée
----------------------------------

Modèle de réseau neuronal
~~~~~~~~~~~~~~~~~~~~~~~~

uHDRv6 intègre un modèle PyTorch pré-entraîné (``MSESig505_0419.pth``) qui fournit :

**Amélioration automatique d'image**
  - Analyse du contenu de l'image
  - Suggestions d'amélioration basées sur l'apprentissage
  - Optimisation automatique des paramètres

**Classification de scènes**
  - Reconnaissance du type de scène
  - Adaptation des algorithmes au contenu
  - Optimisation spécifique (portrait, paysage, architecture)

**Détection d'artefacts**
  - Identification automatique des problèmes d'image
  - Suggestions de correction
  - Prévention de la dégradation lors du traitement

Évaluation de qualité
---------------------

Métriques objectives
~~~~~~~~~~~~~~~~~~~

Le module ``quality.py`` fournit plusieurs métriques pour évaluer la qualité des images :

**Métriques de netteté**
  - Analyse de la netteté globale et locale
  - Détection du flou de mouvement
  - Évaluation de la mise au point

**Métriques de bruit**
  - Quantification du bruit dans différentes zones
  - Analyse spectrale du bruit
  - Évaluation du rapport signal/bruit

**Métriques colorimétriques**
  - Évaluation de la précision colorimétrique
  - Analyse de la gamme de couleurs
  - Détection des couleurs hors gamut

Traitement par lots avancé
-------------------------

Pipeline personnalisable
~~~~~~~~~~~~~~~~~~~~~~~

**Configuration des étapes**
  - Définition d'une séquence de traitements
  - Paramétrage indépendant de chaque étape
  - Sauvegarde et réutilisation des pipelines

**Traitement conditionnel**
  - Application de traitements selon des critères
  - Adaptation automatique aux caractéristiques de l'image
  - Gestion des exceptions et des cas particuliers

**Monitoring et reporting**
  - Suivi en temps réel du traitement
  - Génération de rapports détaillés
  - Logging des erreurs et des avertissements

Optimisations pour différents écrans
------------------------------------

Support des standards HDR
~~~~~~~~~~~~~~~~~~~~~~~~~

**VESA DisplayHDR**
  - Profils optimisés pour DisplayHDR 400
  - Support des écrans DisplayHDR 1000
  - Adaptation automatique aux capacités de l'écran

**Format HLG (Hybrid Log-Gamma)**
  - Compatibilité avec le standard de diffusion
  - Optimisation pour les contenus télévisuels
  - Préservation de la compatibilité SDR

**Dolby Vision et HDR10**
  - Préparation des contenus pour ces standards
  - Métadonnées dynamiques
  - Optimisation du tone mapping

Exportation avancée
-------------------

Options de rendu
~~~~~~~~~~~~~~~

**Tone mapping personnalisé**
  - Algorithmes adaptatifs selon le contenu
  - Préservation des détails dans les extrêmes
  - Optimisation perceptuelle

**Gestion des métadonnées**
  - Préservation complète des métadonnées EXIF
  - Ajout d'informations de traitement
  - Compatibilité avec les systèmes de gestion d'actifs

**Formats de sortie spécialisés**
  - Export optimisé pour différentes plateformes
  - Adaptation aux contraintes de diffusion
  - Génération de multiples versions simultanément
