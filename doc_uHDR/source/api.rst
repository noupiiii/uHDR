Référence API
=============

Cette section documente l'API interne de uHDRv6 pour les développeurs souhaitant comprendre ou étendre le logiciel.

Module hdrCore
--------------

Le module ``hdrCore`` contient la logique principale de traitement des images HDR.

hdrCore.image
~~~~~~~~~~~~~

Classes principales pour la manipulation d'images.

.. py:class:: HDRImage

   Classe principale pour représenter une image HDR.

   .. py:method:: __init__(self, data, metadata=None)

      :param numpy.ndarray data: Données de l'image en format float32
      :param dict metadata: Métadonnées optionnelles de l'image

   .. py:method:: load_from_file(self, filepath)

      Charge une image depuis un fichier.

      :param str filepath: Chemin vers le fichier image
      :return: Instance HDRImage
      :rtype: HDRImage

   .. py:method:: save_to_file(self, filepath, format='hdr')

      Sauvegarde l'image vers un fichier.

      :param str filepath: Chemin de destination
      :param str format: Format de sortie ('hdr', 'exr', 'tiff')

   .. py:method:: apply_tone_mapping(self, curve_params)

      Applique un tone mapping à l'image.

      :param dict curve_params: Paramètres de la courbe tonale
      :return: Image avec tone mapping appliqué
      :rtype: HDRImage

   .. py:method:: get_histogram(self, bins=256)

      Calcule l'histogramme de l'image.

      :param int bins: Nombre de bins pour l'histogramme
      :return: Histogramme RGB
      :rtype: tuple

hdrCore.processing
~~~~~~~~~~~~~~~~~

Fonctions de traitement d'image.

.. py:function:: apply_exposure_adjustment(image, ev_adjustment)

   Applique un ajustement d'exposition.

   :param numpy.ndarray image: Image source
   :param float ev_adjustment: Ajustement en EV (-5.0 à +5.0)
   :return: Image ajustée
   :rtype: numpy.ndarray

.. py:function:: apply_white_balance(image, temperature, tint)

   Applique une correction de balance des blancs.

   :param numpy.ndarray image: Image source
   :param float temperature: Température de couleur (2000-10000K)
   :param float tint: Correction tint (-1.0 à +1.0)
   :return: Image corrigée
   :rtype: numpy.ndarray

.. py:function:: apply_curve_adjustment(image, curve_points)

   Applique une courbe tonale personnalisée.

   :param numpy.ndarray image: Image source
   :param list curve_points: Points de contrôle de la courbe [(x1,y1), (x2,y2), ...]
   :return: Image avec courbe appliquée
   :rtype: numpy.ndarray

hdrCore.aesthetics
~~~~~~~~~~~~~~~~~

Fonctions d'amélioration esthétique automatique.

.. py:function:: auto_enhance(image, enhancement_type='balanced')

   Amélioration automatique basée sur IA.

   :param numpy.ndarray image: Image source
   :param str enhancement_type: Type d'amélioration ('balanced', 'vivid', 'natural')
   :return: Image améliorée
   :rtype: numpy.ndarray

.. py:function:: analyze_scene_type(image)

   Analyse le type de scène pour optimiser les traitements.

   :param numpy.ndarray image: Image à analyser
   :return: Type de scène détecté
   :rtype: str

hdrCore.quality
~~~~~~~~~~~~~~

Métriques de qualité d'image.

.. py:function:: calculate_sharpness(image)

   Calcule la métrique de netteté de l'image.

   :param numpy.ndarray image: Image à analyser
   :return: Score de netteté (0.0 à 1.0)
   :rtype: float

.. py:function:: calculate_noise_level(image)

   Estime le niveau de bruit dans l'image.

   :param numpy.ndarray image: Image à analyser
   :return: Niveau de bruit estimé
   :rtype: float

.. py:function:: calculate_dynamic_range(image)

   Calcule la gamme dynamique effective de l'image.

   :param numpy.ndarray image: Image à analyser
   :return: Gamme dynamique en stops
   :rtype: float

hdrCore.srgb
~~~~~~~~~~~

Conversions d'espaces colorimétriques.

.. py:function:: rgb_to_xyz(rgb_array, illuminant='D65')

   Convertit RGB vers XYZ.

   :param numpy.ndarray rgb_array: Données RGB
   :param str illuminant: Illuminant de référence
   :return: Données XYZ
   :rtype: numpy.ndarray

.. py:function:: xyz_to_lab(xyz_array, illuminant='D65')

   Convertit XYZ vers Lab.

   :param numpy.ndarray xyz_array: Données XYZ
   :param str illuminant: Illuminant de référence
   :return: Données Lab
   :rtype: numpy.ndarray

.. py:function:: apply_gamma_correction(image, gamma=2.2)

   Applique une correction gamma.

   :param numpy.ndarray image: Image source
   :param float gamma: Valeur gamma
   :return: Image corrigée
   :rtype: numpy.ndarray

Module guiQt
------------

Le module ``guiQt`` gère l'interface utilisateur.

guiQt.model
~~~~~~~~~~

Modèles de données pour l'interface.

.. py:class:: ImageModel

   Modèle de données pour la gestion des images dans l'interface.

   .. py:method:: add_image(self, image_path)

      Ajoute une image au modèle.

      :param str image_path: Chemin vers l'image

   .. py:method:: get_image_at_index(self, index)

      Récupère une image par son index.

      :param int index: Index de l'image
      :return: Données de l'image
      :rtype: HDRImage

   .. py:method:: remove_image(self, index)

      Supprime une image du modèle.

      :param int index: Index de l'image à supprimer

guiQt.controller
~~~~~~~~~~~~~~~

Contrôleurs pour la gestion des événements.

.. py:class:: MainController

   Contrôleur principal de l'application.

   .. py:method:: handle_image_selection(self, index)

      Gère la sélection d'une image.

      :param int index: Index de l'image sélectionnée

   .. py:method:: handle_processing_request(self, processing_params)

      Gère une demande de traitement d'image.

      :param dict processing_params: Paramètres de traitement

   .. py:method:: handle_export_request(self, export_params)

      Gère une demande d'exportation.

      :param dict export_params: Paramètres d'exportation

guiQt.view
~~~~~~~~~

Composants d'interface utilisateur.

.. py:class:: ImageViewer

   Widget d'affichage d'images.

   .. py:method:: set_image(self, hdr_image)

      Définit l'image à afficher.

      :param HDRImage hdr_image: Image à afficher

   .. py:method:: set_zoom_level(self, zoom)

      Définit le niveau de zoom.

      :param float zoom: Niveau de zoom (0.1 à 10.0)

.. py:class:: HistogramWidget

   Widget d'affichage d'histogramme.

   .. py:method:: update_histogram(self, histogram_data)

      Met à jour l'histogramme affiché.

      :param tuple histogram_data: Données RGB de l'histogramme

Module preferences
------------------

Gestion des préférences et configuration.

preferences.preferences
~~~~~~~~~~~~~~~~~~~~~~~

Configuration globale de l'application.

.. py:data:: computation

   Mode de calcul utilisé.

   :type: str
   :value: 'numba'
   :options: 'python', 'numba', 'cuda'

.. py:data:: verbose

   Mode verbeux pour le débogage.

   :type: bool
   :value: False

.. py:function:: load_preferences()

   Charge les préférences depuis le fichier de configuration.

   :return: Dictionnaire des préférences
   :rtype: dict

.. py:function:: save_preferences(prefs_dict)

   Sauvegarde les préférences.

   :param dict prefs_dict: Préférences à sauvegarder

.. py:function:: get_hdr_display_profiles()

   Récupère les profils d'écrans HDR configurés.

   :return: Liste des profils disponibles
   :rtype: list

Intégration avec composants externes
------------------------------------

Interface HDRip.dll
~~~~~~~~~~~~~~~~~~~

Fonctions C++ optimisées accessibles via ctypes.

.. py:function:: call_hdrip_function(function_name, *args)

   Interface générique pour appeler les fonctions HDRip.

   :param str function_name: Nom de la fonction C++
   :param args: Arguments à passer à la fonction
   :return: Résultat de la fonction C++

Fonctions disponibles dans HDRip.dll :

- ``tone_mapping_optimized`` : Tone mapping haute performance
- ``color_space_conversion`` : Conversions colorimétriques optimisées
- ``image_filtering`` : Filtres d'image vectorisés
- ``histogram_calculation`` : Calcul d'histogramme accéléré

Interface exiftool
~~~~~~~~~~~~~~~~~

.. py:function:: extract_metadata(image_path)

   Extrait les métadonnées d'une image via exiftool.

   :param str image_path: Chemin vers l'image
   :return: Dictionnaire des métadonnées
   :rtype: dict

.. py:function:: write_metadata(image_path, metadata_dict)

   Écrit des métadonnées dans une image.

   :param str image_path: Chemin vers l'image
   :param dict metadata_dict: Métadonnées à écrire

Interface réseau neuronal
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: load_neural_model(model_path)

   Charge un modèle PyTorch pré-entraîné.

   :param str model_path: Chemin vers le modèle .pth
   :return: Modèle chargé
   :rtype: torch.nn.Module

.. py:function:: run_inference(model, input_image)

   Exécute une inférence sur une image.

   :param torch.nn.Module model: Modèle neuronal
   :param numpy.ndarray input_image: Image d'entrée
   :return: Résultat de l'inférence
   :rtype: numpy.ndarray

Exceptions et gestion d'erreurs
-------------------------------

Exceptions personnalisées
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:exception:: HDRProcessingError

   Exception levée lors d'erreurs de traitement HDR.

.. py:exception:: InvalidImageFormatError

   Exception levée pour les formats d'image non supportés.

.. py:exception:: MetadataError

   Exception levée lors d'erreurs de métadonnées.

.. py:exception:: ComputationModeError

   Exception levée lors d'erreurs de mode de calcul.

Gestion des erreurs
~~~~~~~~~~~~~~~~~~

.. py:function:: handle_processing_error(error, fallback_mode=True)

   Gestionnaire d'erreurs génériques pour le traitement.

   :param Exception error: Erreur à traiter
   :param bool fallback_mode: Active le mode de fallback
   :return: Code d'erreur ou None si récupération réussie
   :rtype: int or None

Configuration de logging
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: setup_logging(level='INFO', log_file=None)

   Configure le système de logging.

   :param str level: Niveau de log ('DEBUG', 'INFO', 'WARNING', 'ERROR')
   :param str log_file: Fichier de log optionnel

Constants et enums
------------------

Formats d'image supportés
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:data:: SUPPORTED_INPUT_FORMATS

   Formats d'entrée supportés.

   :type: list
   :value: ['.hdr', '.exr', '.arw', '.jpg', '.png', '.tiff']

.. py:data:: SUPPORTED_OUTPUT_FORMATS

   Formats de sortie supportés.

   :type: list
   :value: ['.hdr', '.exr', '.jpg', '.png', '.tiff']

Modes de traitement
~~~~~~~~~~~~~~~~~~

.. py:data:: COMPUTATION_MODES

   Modes de calcul disponibles.

   :type: list
   :value: ['python', 'numba', 'cuda', 'cpp']

Paramètres par défaut
~~~~~~~~~~~~~~~~~~~~

.. py:data:: DEFAULT_TONE_MAPPING_PARAMS

   Paramètres par défaut pour le tone mapping.

   :type: dict

.. py:data:: DEFAULT_COLOR_CORRECTION_PARAMS

   Paramètres par défaut pour la correction colorimétrique.

   :type: dict

Utilisation de l'API
--------------------

Exemple d'utilisation basique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hdrCore.image import HDRImage
   from hdrCore.processing import apply_exposure_adjustment
   from preferences.preferences import load_preferences
   
   # Chargement des préférences
   prefs = load_preferences()
   
   # Chargement d'une image HDR
   hdr_img = HDRImage()
   hdr_img.load_from_file('image.hdr')
   
   # Application d'un ajustement d'exposition
   adjusted_data = apply_exposure_adjustment(hdr_img.data, ev_adjustment=1.5)
   
   # Création d'une nouvelle image avec les données ajustées
   result_img = HDRImage(adjusted_data, hdr_img.metadata)
   
   # Sauvegarde
   result_img.save_to_file('output.hdr')

Exemple d'utilisation avancée
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hdrCore.image import HDRImage
   from hdrCore.aesthetics import auto_enhance, analyze_scene_type
   from hdrCore.quality import calculate_sharpness
   from guiQt.model import ImageModel
   
   # Pipeline de traitement automatisé
   def auto_process_image(image_path):
       # Chargement
       img = HDRImage()
       img.load_from_file(image_path)
       
       # Analyse de la scène
       scene_type = analyze_scene_type(img.data)
       print(f"Type de scène détecté: {scene_type}")
       
       # Amélioration automatique
       enhanced_data = auto_enhance(img.data, enhancement_type='balanced')
       
       # Vérification de la qualité
       sharpness = calculate_sharpness(enhanced_data)
       print(f"Netteté: {sharpness:.3f}")
       
       # Création de l'image résultat
       result = HDRImage(enhanced_data, img.metadata)
       return result
   
   # Utilisation avec l'interface
   def integrate_with_gui():
       model = ImageModel()
       model.add_image('input.hdr')
       
       # Traitement
       processed_img = auto_process_image('input.hdr')
       
       # Ajout au modèle pour affichage
       model.add_processed_image(processed_img)
