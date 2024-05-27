### Manual de Usuario

Este manual proporciona instrucciones detalladas sobre cómo utilizar el programa Cliente-Servidor desarrollado en un entorno Linux.

#### Requisitos del Sistema

Este programa fue desarrollado y probado en un entorno Linux. Para ejecutarlo, necesitas tener instalado Python 3 y Make en tu sistema.

### Puerto de escucha

Puerto TCP número 16081.

#### Instalación de Python y Make en Linux

1. **Python 3**: Puedes instalar Python 3 en tu sistema Linux usando el gestor de paquetes de tu distribución. Por ejemplo, en sistemas basados en Debian (como Ubuntu), puedes usar el siguiente comando:

    ```bash
    sudo apt update
    sudo apt install python3
    ```

    Verifica que Python 3 se haya instalado correctamente ejecutando:

    ```bash
    python3 --version
    ```

2. **Make**: Make es una herramienta de construcción que se utiliza para automatizar tareas comunes en el desarrollo de software. Puedes instalar Make en tu sistema Linux usando el gestor de paquetes de tu distribución. Por ejemplo, en sistemas basados en Debian:

    ```bash
    sudo apt update
    sudo apt install make
    ```

    Verifica que Make se haya instalado correctamente ejecutando:

    ```bash
    make --version
    ```

#### Clonación del Repositorio

Una vez que hayas instalado Python 3 y Make, puedes clonar el repositorio que contiene el código del programa Cliente-Servidor. Abre una terminal y ejecuta el siguiente comando:

```bash
git clone URL_DEL_REPOSITORIO

cd proyecto/
```

#### Instrucciones de uso

Una vez dentro del proyecto el Makefile proporciona varios comandos útiles para ejecutar el programa Cliente-Servidor:

- **make test**: Este comando ejecuta todas las pruebas del sistema. Asegúrate de tener el entorno de prueba configurado correctamente antes de ejecutar este comando.

```bash
    make ttest
```

- **make servidor**: Este comando inicia el servidor. El servidor estará escuchando en el puerto especificado y responderá a las solicitudes de los clientes. Por ejemplo:

    ```bash
    make servidor
    ```

- **make cliente**: Este comando ejecuta el cliente. El cliente se conectará al servidor y enviará solicitudes según lo especificado en el código.

    ```bash
    make cliente
    ```
- Al ejecutar el cliente, se pedirá que introduzca la direccion del servidor () y las peticiones (hora o fecha) de la siguiente manera:

```bash
    Introduzca la dirección del servidor: localhost
    Introduzca la petición: hora
```