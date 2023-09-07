# Test Habi :heart:

En este programa se resolverá la prueba para backend developer de Habi a cargo de **Carlos Felipe Baquero**.

## Tabla de Contenidos

- [Test Habi :heart:](#test-habi-heart)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Instalación](#instalación)
  - [Tecnologías](#tecnologías)
  - [Dudas](#dudas)
  - [Esquema like :+1:](#esquema-like-1)



## Instalación

Para instalar el proyecto, sigue estos pasos:

1. Clona el repositorio: `git clone https://github.com/Tu_usuario/Habi-test.git`
2. Entra en el directorio del proyecto: `cd carpeta del proyecto`
3. Instala las dependencias: `pip install -r requiriment.txt`
4. Crea las variables de entorno en tu sistema: `host_test ,port_test ,user_test ,pass_test ,database_test`
   1. las variables de entorno deben tener los datos de la cadena de conexion
5. Crear entorno virtual  `python -m venv venv_name`
6. Activar el entorno virtual `venv_name\Scripts\activate`

## Tecnologías

1. [Python](https://www.python.org/doc/): Lenguaje de programación en el cual se desarrolló la prueba dados los requerimientos.
2. [Http.server](https://docs.python.org/3/library/http.server.html): Módulo de python que nos permite crear un servidor sencillo web HTTP, se utilizó este módulo por lo practico y sencillo de implementar, es una solucion rapida que permite una concurrencia basica.
3. [Mysql Connnector](https://dev.mysql.com/doc/connector-python/en/): utilizamos este conector dado que es un conector oficial para trabajar con [MySQl](https://www.mysql.com/), algunas de las razones por las cuales utilizamos este conector es por el soporte oficial que tiene y la documentación completa que posee aprovechando así las funcionalidades completas especificas de [MySQl](https://www.mysql.com/).
4. [Json](https://www.json.org/json-en.html): formato ligero para manejo de comunicación con los servicios.

## Dudas
1. Utilizar la libreria **Sockets** o **Http.server**
   1. Al final me decanté por usar http.server para un manejo más sencillo de las conexiones, ya que usar sockets era más para otros requerimientos y control de cargas.
2. Hacer las variables para la conexión  a la base de datos como variables de entorno
   1. Si dado que trabajar con variables de conexión públicas hace el código inseguro.
3. Que conector usar para la base de datos
   1. **MySql Connector** dado que es el oficial y tiene soporte completo con bases de datos **MySql**, lo que nos permite tener una documentación clara en caso de que surja cualquier duda.
4. Como hacer la consulta a la bd dinámica para que no consuma tantos recursos y a su vez sea funcional para el primer requerimiento
   1. relaizar una serie de join para optimizar el consumo de la base de datos y a su vez hacer concatenación de strigns para realizar filtros dinámicos según los requerimientos del proyecto.

## Esquema like :+1:
![Esquema](.\logos\diagrama_megustas.png)
