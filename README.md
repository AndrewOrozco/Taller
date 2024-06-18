# Proyecto de Reconocimiento Facial

## Descripción

Este proyecto implementa un sistema de reconocimiento facial utilizando la librería `keras_vggface` para la extracción de características faciales y un clasificador KNN para la identificación de individuos. El sistema permite agregar nuevas clases sin necesidad de reentrenar todo el modelo desde cero.

## Requisitos

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

## Instalación

### Paso 1: Crear y Activar un Entorno Conda

```sh
conda create -n face_recognition_env python=3.9.19
conda activate face_recognition_env


### Paso 2: Instalar las librerias Necesarias
```sh
pip install tensorflow==2.12.0
pip install keras==2.12.0
pip install opencv-python==4.10.0
pip install dlib==19.24.0
pip install scikit-learn==1.3.0
pip install matplotlib==3.7.1
pip install numpy==1.23.5
pip install keras-vggface==0.6


