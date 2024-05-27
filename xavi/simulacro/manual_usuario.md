# Manual de Instalación y Uso

Este manual describe los pasos necesarios para instalar y utilizar el sistema en un entorno Linux.

# Puerto de escucha elegido

Puerto TCP número 16082.

## Requisitos del Sistema

Asegúrese de que su sistema cumpla con los siguientes requisitos antes de proceder:

- Linux OS (Ubuntu, Fedora, etc.)
- Python
- Make

## Instalación

Siga estos pasos para instalar el proyecto:

1. **Instalación de Python:**

   Si no tiene Python instalado, puede instalarlo usando el gestor de paquetes de su distribución. Por ejemplo, en Ubuntu:

   ```bash
   sudo apt-get update
   sudo apt-get install python3

## Instrucciones de uso

- Para ejecurtar los tests: 

	```bash
	make ttest

- Para ejecutar el servidor: 

	```bash
    make serv

- Para ejecutar el cliente: 

	```bash
    make cli

- Como responder al cliente:
    ```bash
    Introduzca la direcccion: <Direccion_servidor>
    ¿Que quieres?: <HORA> | <FECHA>
