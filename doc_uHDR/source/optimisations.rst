Modes de calcul et optimisations
=================================

uHDRv6 propose plusieurs modes de calcul, permettant d'adapter les performances en fonction du matériel disponible et des besoins de l'utilisateur.

Vue d'ensemble des modes
-----------------------

Le logiciel dispose de quatre modes de calcul principaux :

1. **Mode Python pur** : Compatibilité maximale, performances de base
2. **Mode Numba (JIT)** : Accélération par compilation à la volée
3. **Mode CUDA (GPU)** : Déportation des calculs sur GPU NVIDIA
4. **Mode C++ (HDRip.dll)** : Fonctions natives optimisées

Mode Python pur
---------------

Caractéristiques
~~~~~~~~~~~~~~~~

- **Fonctionnement** : Utilise uniquement des calculs en Python avec NumPy
- **Technologies** : NumPy, SciPy, bibliothèques Python standard
- **Performance** : Référence de base (multiplicateur x1)

Avantages
~~~~~~~~~

* **Compatibilité maximale** : Fonctionne sur tous les systèmes avec Python
* **Facilité de débogage** : Code source directement accessible et modifiable
* **Pas de dépendances complexes** : Aucune compilation ou configuration spéciale
* **Portabilité** : Compatible avec toutes les architectures supportées par Python

Inconvénients
~~~~~~~~~~~~

* **Performances limitées** : Plus lent sur les grandes images (>10 MP)
* **Consommation mémoire** : Plus importante due aux copies d'objets Python
* **Scalabilité** : Performance dégradée avec la taille des images

Utilisation recommandée
~~~~~~~~~~~~~~~~~~~~~~

- Développement et débogage
- Tests sur nouveaux algorithmes
- Systèmes à ressources très limitées
- Validation de résultats de référence

Configuration
~~~~~~~~~~~~

.. code-block:: python

   # Dans preferences/preferences.py
   computation = 'python'
   verbose = True  # Pour le débogage

Mode Numba (JIT)
----------------

Caractéristiques
~~~~~~~~~~~~~~~~

- **Fonctionnement** : Compilation Just-In-Time des fonctions Python critiques
- **Technologies** : Numba, LLVM, vectorisation automatique
- **Performance** : x5-10 plus rapide que le Python pur

Technologies sous-jacentes
~~~~~~~~~~~~~~~~~~~~~~~~~

**Numba JIT Compiler**
  - Conversion du bytecode Python en code machine optimisé
  - Analyse statique des types pour l'optimisation
  - Génération de code via LLVM

**Vectorisation automatique**
  - Détection des boucles vectorisables
  - Utilisation automatique des instructions SIMD (SSE, AVX)
  - Parallélisation des opérations indépendantes

**Optimisations LLVM**
  - Optimisations de bas niveau (élimination de code mort, inlining)
  - Optimisations spécifiques au processeur
  - Gestion intelligente des registres

Avantages
~~~~~~~~~

* **Accélération significative** : Gain de performance substantiel sans modification du code
* **Préservation de la lisibilité** : Le code source reste en Python
* **Compatible avec la plupart des environnements** : Pas de dépendances système complexes
* **Compilation adaptative** : Optimisation spécifique au matériel détecté

Optimisations spécifiques
~~~~~~~~~~~~~~~~~~~~~~~~

**Fonctions critiques optimisées :**

.. code-block:: python

   from numba import jit, prange
   
   @jit(nopython=True, parallel=True)
   def tone_mapping_optimized(image, curve_params):
       # Parallélisation automatique des boucles
       for i in prange(image.shape[0]):
           for j in range(image.shape[1]):
               # Calculs vectorisés automatiquement
               image[i, j] = apply_curve(image[i, j], curve_params)
       return image

**Cache de compilation :**

.. code-block:: python

   # Cache persistant pour éviter la recompilation
   @jit(nopython=True, cache=True)
   def color_conversion(rgb_array):
       # Fonction mise en cache après première compilation
       return xyz_array

Utilisation recommandée
~~~~~~~~~~~~~~~~~~~~~~

- Usage courant pour la plupart des utilisateurs
- Systèmes sans GPU NVIDIA
- Développement avec besoin de performances
- Production sur serveurs sans GPU

Configuration
~~~~~~~~~~~~

.. code-block:: python

   # Dans preferences/preferences.py
   computation = 'numba'
   
   # Configuration avancée Numba
   import numba
   numba.config.CACHE_DIR = './numba_cache'
   numba.config.THREADING_LAYER = 'omp'  # OpenMP pour parallélisme

Mode CUDA (GPU)
---------------

Caractéristiques
~~~~~~~~~~~~~~~~

- **Fonctionnement** : Déportation des calculs sur GPU NVIDIA via CUDA
- **Technologies** : Numba CUDA, CuPy, accélération GPU massive
- **Performance** : x20-50 plus rapide pour les opérations parallélisables

Architecture CUDA
~~~~~~~~~~~~~~~~~

**Modèle de programmation :**
  - Milliers de threads exécutés simultanément
  - Hiérarchie blocks/threads pour l'organisation
  - Mémoire partagée rapide entre threads d'un block

**Optimisations spécifiques GPU :**
  - Coalescing des accès mémoire pour maximiser la bande passante
  - Utilisation de la mémoire texture pour les images
  - Streams CUDA pour les opérations asynchrones

Avantages
~~~~~~~~~

* **Accélération massive** : Gain x20-50 sur les opérations parallélisables
* **Libération du CPU** : Le processeur reste disponible pour d'autres tâches
* **Scalabilité** : Performance maintenue même sur les très grandes images
* **Traitement par lots** : Optimisation pour le traitement simultané de multiples images

Prérequis techniques
~~~~~~~~~~~~~~~~~~~

**Matériel requis :**
- GPU NVIDIA avec architecture Compute Capability 3.5+
- Mémoire GPU suffisante (4 Go minimum, 8 Go recommandé)
- Pilotes NVIDIA récents (version 450+)

**Logiciels requis :**
- CUDA Toolkit 11.0+ installé
- Numba avec support CUDA
- PyTorch compilé avec support CUDA

Fonctions optimisées GPU
~~~~~~~~~~~~~~~~~~~~~~~

**Convolutions et filtres :**

.. code-block:: python

   from numba import cuda
   import numpy as np
   
   @cuda.jit
   def gaussian_blur_cuda(image, output, kernel):
       # Calcul des indices thread
       x, y = cuda.grid(2)
       if x < image.shape[0] and y < image.shape[1]:
           # Convolution GPU parallélisée
           result = 0.0
           for i in range(kernel.shape[0]):
               for j in range(kernel.shape[1]):
                   if (x+i < image.shape[0] and y+j < image.shape[1]):
                       result += image[x+i, y+j] * kernel[i, j]
           output[x, y] = result

**Conversions colorimétriques :**

.. code-block:: python

   @cuda.jit
   def rgb_to_xyz_cuda(rgb_array, xyz_array, conversion_matrix):
       idx = cuda.grid(1)
       if idx < rgb_array.shape[0]:
           # Multiplication matricielle sur GPU
           for i in range(3):
               xyz_array[idx, i] = (conversion_matrix[i, 0] * rgb_array[idx, 0] +
                                   conversion_matrix[i, 1] * rgb_array[idx, 1] +
                                   conversion_matrix[i, 2] * rgb_array[idx, 2])

Gestion de la mémoire GPU
~~~~~~~~~~~~~~~~~~~~~~~~~

**Stratégies d'optimisation :**

.. code-block:: python

   import cupy as cp
   
   # Allocation mémoire optimisée
   def process_large_image_gpu(image_path):
       # Utilisation de memory pools pour éviter la fragmentation
       mempool = cp.get_default_memory_pool()
       
       # Chargement par chunks pour les très grandes images
       with cp.cuda.Device(0):
           # Traitement par blocs
           for chunk in image_chunks:
               gpu_chunk = cp.asarray(chunk)
               processed_chunk = apply_processing_gpu(gpu_chunk)
               result_chunks.append(cp.asnumpy(processed_chunk))
       
       # Libération explicite de la mémoire
       mempool.free_all_blocks()

Utilisation recommandée
~~~~~~~~~~~~~~~~~~~~~~

- Production avec besoins de performance élevés
- Traitement par lots de nombreuses images
- Images haute résolution (4K, 8K+)
- Développement d'algorithmes intensifs

Configuration
~~~~~~~~~~~~

.. code-block:: python

   # Vérification de disponibilité CUDA
   try:
       from numba import cuda
       if cuda.is_available():
           # Configuration CUDA
           computation = 'cuda'
           cuda_device = cuda.get_current_device()
           print(f"GPU détecté: {cuda_device.name}")
           print(f"Mémoire disponible: {cuda_device.memory_size // 1024**2} MB")
       else:
           print("CUDA non disponible, fallback vers Numba")
           computation = 'numba'
   except ImportError:
       computation = 'numba'

Mode C++ (HDRip.dll)
-------------------

Caractéristiques
~~~~~~~~~~~~~~~~

- **Fonctionnement** : Utilise les fonctions optimisées de la bibliothèque C++
- **Technologies** : Code natif précompilé, instructions SIMD, optimisations compilateur
- **Performance** : Performance maximale pour les algorithmes spécialisés

Architecture de la DLL
~~~~~~~~~~~~~~~~~~~~~~

**Optimisations compilateur :**
  - Optimisations agressives (O3, LTO)
  - Vectorisation automatique avec intrinsèques SIMD
  - Optimisations spécifiques à l'architecture (AVX2, AVX-512)

**Instructions SIMD :**
  - SSE2/SSE4 pour compatibilité étendue
  - AVX/AVX2 pour performance sur processeurs récents
  - Détection automatique des capacités du processeur

Avantages
~~~~~~~~~

* **Performances maximales** : Code natif optimisé au maximum
* **Opérations atomiques** : Calculs précis sans erreurs d'arrondi
* **Stabilité** : Code mature et testé
* **Efficacité mémoire** : Gestion optimisée des allocations

Interface Python-C++
~~~~~~~~~~~~~~~~~~~~

**Intégration via ctypes :**

.. code-block:: python

   import ctypes
   from ctypes import c_float, c_int, POINTER
   
   # Chargement de la DLL
   hdrip = ctypes.CDLL('./HDRip.dll')
   
   # Définition des prototypes de fonctions
   hdrip.tone_mapping.argtypes = [
       POINTER(c_float),  # image_data
       c_int,             # width
       c_int,             # height
       POINTER(c_float)   # curve_params
   ]
   hdrip.tone_mapping.restype = c_int
   
   # Appel des fonctions C++
   def apply_tone_mapping_cpp(image, curve_params):
       # Conversion des données Python vers C
       image_ptr = image.ctypes.data_as(POINTER(c_float))
       params_ptr = curve_params.ctypes.data_as(POINTER(c_float))
       
       # Appel de la fonction native
       result = hdrip.tone_mapping(
           image_ptr, 
           image.shape[1], 
           image.shape[0], 
           params_ptr
       )
       return result

Fonctions disponibles
~~~~~~~~~~~~~~~~~~~~

**Traitement HDR spécialisé :**
- Tone mapping avec algorithmes propriétaires
- Conversions d'espaces colorimétriques haute précision
- Filtres adaptatifs optimisés
- Opérations matricielles vectorisées

**Gestion des métadonnées :**
- Extraction rapide d'informations EXIF
- Calculs de statistiques d'image
- Validation et correction de données

Utilisation
~~~~~~~~~~

Le mode C++ est automatiquement activé pour certaines opérations critiques, transparent pour l'utilisateur.

Sélection automatique du mode
-----------------------------

Algorithme de sélection
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def select_optimal_computation_mode():
       # Détection des capacités système
       capabilities = detect_system_capabilities()
       
       if capabilities['cuda_available'] and capabilities['gpu_memory'] > 4096:
           return 'cuda'
       elif capabilities['numba_available']:
           return 'numba'
       else:
           return 'python'
   
   def detect_system_capabilities():
       capabilities = {
           'cuda_available': False,
           'gpu_memory': 0,
           'numba_available': False,
           'cpu_cores': os.cpu_count()
       }
       
       # Test CUDA
       try:
           import torch
           if torch.cuda.is_available():
               capabilities['cuda_available'] = True
               capabilities['gpu_memory'] = torch.cuda.get_device_properties(0).total_memory // 1024**2
       except ImportError:
           pass
       
       # Test Numba
       try:
           import numba
           capabilities['numba_available'] = True
       except ImportError:
           pass
       
       return capabilities

Fallback automatique
~~~~~~~~~~~~~~~~~~~

En cas d'échec d'un mode, le système rétrograde automatiquement :

.. code-block:: python

   def safe_computation(func, data, mode='auto'):
       if mode == 'auto':
           mode = select_optimal_computation_mode()
       
       try:
           if mode == 'cuda':
               return func.cuda_version(data)
       except Exception as e:
           logger.warning(f"CUDA failed: {e}, falling back to Numba")
           mode = 'numba'
       
       try:
           if mode == 'numba':
               return func.numba_version(data)
       except Exception as e:
           logger.warning(f"Numba failed: {e}, falling back to Python")
           mode = 'python'
       
       return func.python_version(data)

Benchmarking et profiling
-------------------------

Métriques de performance
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import time
   import psutil
   
   def benchmark_computation_modes(test_image):
       results = {}
       
       for mode in ['python', 'numba', 'cuda']:
           if is_mode_available(mode):
               # Mesure du temps d'exécution
               start_time = time.perf_counter()
               memory_before = psutil.virtual_memory().used
               
               # Exécution du test
               result = process_image(test_image, mode=mode)
               
               end_time = time.perf_counter()
               memory_after = psutil.virtual_memory().used
               
               results[mode] = {
                   'execution_time': end_time - start_time,
                   'memory_usage': memory_after - memory_before,
                   'speedup': results.get('python', {}).get('execution_time', 1) / (end_time - start_time)
               }
       
       return results

Recommandations d'optimisation
------------------------------

Configuration système
~~~~~~~~~~~~~~~~~~~~~

**Pour performances CPU (Numba) :**
- Processeur multi-cœur récent (8+ cœurs recommandé)
- RAM rapide (DDR4-3200 ou supérieure)
- SSD pour réduire les temps de chargement

**Pour performances GPU (CUDA) :**
- GPU NVIDIA RTX série 30xx ou supérieure
- 8 Go+ de VRAM pour les images 4K
- PCIe 3.0 x16 ou supérieur pour les transferts

Configuration logicielle
~~~~~~~~~~~~~~~~~~~~~~~~

**Variables d'environnement optimales :**

.. code-block:: bash

   # Numba
   export NUMBA_NUM_THREADS=8
   export NUMBA_CACHE_DIR=/tmp/numba_cache
   
   # OpenMP (pour parallélisme)
   export OMP_NUM_THREADS=8
   export OMP_DYNAMIC=true
   
   # CUDA
   export CUDA_VISIBLE_DEVICES=0
   export CUDA_CACHE_MAXSIZE=1073741824  # 1GB cache

**Configuration PyTorch :**

.. code-block:: python

   import torch
   
   # Optimisation des threads CPU
   torch.set_num_threads(4)
   
   # Optimisation CUDA
   if torch.cuda.is_available():
       torch.backends.cudnn.benchmark = True
       torch.backends.cudnn.deterministic = False
