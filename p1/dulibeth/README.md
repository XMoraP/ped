# Guía de Ejecución de Pruebas para Kata de TDD: Marcador de Bolos

Esta guía te ayudará a ejecutar las pruebas para la Kata de TDD, que se centra en el desarrollo de un marcador de bolos, permitiéndote llevar un seguimiento preciso de las puntuaciones en una partida de bolos.

## Pasos para Ejecutar las Pruebas

1. **Requisitos del Sistema**:
   - Asegúrate de tener Python instalado en tu sistema.
   - Además, necesitarás tener Make instalado para simplificar el proceso de ejecución de las pruebas.

2. **Ubicarte en el Directorio del Proyecto**:
   #### Clonación del Repositorio
    Clonar el repositorio que contiene el código del programa Cliente-Servidor. Abre una terminal y ejecuta el siguiente comando:

    ```bash
    git clone http://git.eps.ceu.es/ped/ped8

    cd ped8/p1/dulibeth
    ```

3. **Ejecutar las Pruebas**:
   - Si tienes instalado Make, ejecuta el siguiente comando:
     ```bash
     make ttest
     ```
   - Si no tienes instalado Make, puedes ejecutar las pruebas directamente con Python utilizando el siguiente comando:
     ```bash
     python3 -m unittest -v test/test_bolos.py
     ```

Asegúrate de estar en el directorio correcto antes de ejecutar los comandos de prueba. Esto garantizará que las pruebas se ejecuten correctamente y puedas verificar el funcionamiento del software desarrollado utilizando la metodología TDD.


