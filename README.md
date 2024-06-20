# Proyecto de Reconocimiento Facial

## NOTA

Es importante isntalar Microsft Visual Studio para el funcionamiento correcto de la libreria de `dlib` en caso de no tenerlo isntalado seguir los siguientes pasos:

### Paso 1: Instalar Microsoft Visual Studio

1. Descargar e instalar Microsoft Visual Studio Edition desde la siguiente URL

```markdown
https://visualstudio.microsoft.com/es/
```

Seleccionar Visual *Community*

2. Durante la isntación, asegurar de seleccionar la carga de trabajo *Desarrollo para escritorio con C++*

## Descripción

Este proyecto implementa un sistema de reconocimiento facial utilizando la librería `keras_vggface` para la extracción de características faciales y un clasificador KNN para la identificación de individuos. El sistema permite agregar nuevas clases sin necesidad de reentrenar todo el modelo desde cero.

## Requisitos

### Instalación de Conda (En ves de instalar Python)

Para instlar Conda se necesita dirigirce a la pagina

```markdown
    https://www.anaconda.com/download/
```

Seguir los pasos que el programa

### Versión de Python

- Python 3.9.19

### Librerías y Frameworks

Para asegurar la compatibilidad y el correcto funcionamiento del código, se recomienda usar un entorno de `conda`. A continuación se listan las librerías necesarias:

- TensorFlow 2.12.0
- Keras 2.12.0
- OpenCV 4.10.0
- Dlib 19.24.0
- Scikit-learn 1.3.0
- Matplotlib 3.7.1
- Numpy 1.23.5
- Keras VGGFace 0.6
- seaborn
- cmake

## Instalación

### Paso 1: Crear y Activar un Entorno Conda

```sh
conda create -n face_recognition_env python=3.9.19
conda activate face_recognition_env
```

### Paso 2: Instalar las librerias Necesarias
```sh
pip install tensorflow==2.12.0
pip install seaborn
pip install keras==2.12.0
pip install opencv-python==4.10.0
pip install cmake
pip install dlib==19.24.0
pip install scikit-learn==1.3.0
pip install matplotlib==3.7.1
pip install numpy==1.23.5
pip install keras-vggface==0.6
```
## Configuración
### Paso 1: Configurar la libreria `keras_vggface`

cuando se encuentre el archivo `model.py` debe poner insertar este llamdo de libreria poder llamar a la libreria correctamente

```python
from keras.utils.layer_utils import get_source_inputs
```
#### Error de kermas_aplications
Si al isntalar las librerias y les aprece un error:

```markdown
ModuleNotFoundError: No module named `keras_applicaions`
```
Ejecutar el siguiente comando:
```python
pip install keras_applications
```
y con ello defe funcionar correctamente

Asegurar de que tu archivo `model.py` tenga la siguiente configuración para importar correctamente las librerias:
```python
from keras.layers import Flatten, Dense, Input, GlobalAveragePooling2D, GlobalMaxPooling2D, Activation, Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D, Reshape, Permute, multiply
from keras_applications.imagenet_utils import _obtain_input_shape
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras import backend as K
from keras_vggface import utils
from keras.utils.layer_utils import get_source_inputs
import warnings
from keras.models import Model
from keras import layers
```
## Ejecución de SVM o KNN
### Paso 1: Prepar el Dataset
1. crear una estructura de capepetas, (en caso de tener el Dataset ver ejemplo de estructuración) donde cada carpeta represente un clase (una persona).
   Ejemplo:
   ```markdown
      dataset/
      ├── andrew/
      │   ├── andrew1.jpg
      │   ├── andrew2.jpg
      │   └── ...
      └── unknown/
          ├── unknown1.jpg
          ├── unknown2.jpg
          └── ...
      ```
### Paso 3: Entrenar el Modelo
Ejecutar la celda de KNN que se encargue de entrenar el modelo KNN.

### Paso 4: Predicción en tiempo real
Ejecutar la celda encargada de iniciar la cámara web y realizar la predicción en tiempo real.

## Erroros posibles al instalar librerias

## En caso de error de instalacioón de la libreria dlib

### Paso 1: Verificar instalacción Desarrollo C++

En caso de tener el error de `error: subprocess-exited-with-error` asegurar de que se halla instalado correctamente la carga de trabajo, en caso de que el error preciste realizar el siguiente paso

### Paso 2: Isntalar Pycharm

#### ¿Que es Pycharm? 

Es un editor de codigo parecido a Visual Studio Code, Pycharm facilita las isntalaciones de librerias ya que contiene su propio buscador, el requerira crer una carpeta virtual (Pues seguir con ese editor o si es prefieres seguir con Visual Studio Code con tu carpeta de Conda actual puedes ahcer lo siguiente)

#### si continuaste con Visual Studio Code

al seguir con Visual y teneindo instlado la libreria `Dlib` con pycharm, puedes buscar la carpeta que se crea automaticamente o buscar la libreria `Dlib` y copiar las 2 carpetas y un archivo `.py`. Acontinuación busca la carpta de tu entorno virtual en la supcarpeta de `lib` y pegar todo sobre esa libreria.

para ver si esta importado correctamente en una celda aparte o otro archivo de `.py` probar el siguiente codigo:

```python
    import dlib
```
