# sensor_OH_M3

Este proyecto implementa un sistema de medición y visualización de concentración de alcohol usando un sensor MQ3 conectado a un microcontrolador compatible con MicroPython (como ESP32).

El sistema realiza las siguientes funciones:
- Lee continuamente el valor analógico del sensor MQ3 mediante un ADC configurado con resolución de 10 bits y rango de entrada ampliado para 3.3 V.
- Calcula un porcentaje relativo de concentración de alcohol ajustado a partir de un umbral base para filtrar ruido.
- Visualiza el porcentaje de alcohol detectado en una pantalla OLED SSD1306 de 128x32 píxeles, mediante una barra gráfica proporcional y un texto numérico.
- Implementa una alerta visual mediante parpadeo en la pantalla OLED cuando el porcentaje de alcohol supera un umbral definido (15%), alternando entre mostrar la barra y pantalla en negro para captar la atención.
- Optimiza la visualización y control de tiempo usando funciones de temporización con time.ticks_ms() para lograr un parpadeo fluido sin bloquear la lectura del sensor.
-Permite un monitoreo en tiempo real y fácil interpretación de la concentración de alcohol en el ambiente o cercano al sensor.

Este proyecto puede utilizarse como base para sistemas de monitoreo ambiental, alcoholímetros caseros o para enseñanza de integración de sensores analógicos con pantallas OLED en MicroPython.
