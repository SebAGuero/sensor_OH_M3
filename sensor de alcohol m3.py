from machine import Pin, I2C, ADC
import time
import ssd1306

# Configuración I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Configuración del sensor MQ3
mq3 = ADC(Pin(36))         # GPIO36 = ADC1_CH0
mq3.atten(ADC.ATTN_11DB)   # Rango completo (0 - 3.3 V)
mq3.width(ADC.WIDTH_10BIT) # Resolución 10 bits (0 - 1023)

UMBRAL_ADC_BASE = 100      # Lecturas menores a este valor se ignoran (0%)
UMBRAL_PORCENTAJE = 15    # Porcentaje a partir del cual parpadea el OLED

def dibujar_barra(valor_adc):
    # Calcula porcentaje solo si valor_adc > UMBRAL_ADC_BASE
    if valor_adc <= UMBRAL_ADC_BASE:
        porcentaje = 0
        largo_barra = 0
    else:
        valor_ajustado = valor_adc - UMBRAL_ADC_BASE
        max_valor = 1023 - UMBRAL_ADC_BASE
        porcentaje = int((valor_ajustado / max_valor) * 100)
        largo_barra = int((valor_ajustado / max_valor) * 128)

    oled.fill(0)
    oled.text("ALCOHOL:", 0, 0)
    oled.fill_rect(0, 20, largo_barra, 10, 1)
    oled.rect(0, 20, 128, 10, 1)
    oled.text(f"{porcentaje}%", 90, 0)
    oled.show()

ultimo_toggle = time.ticks_ms()
mostrar_oled = True

while True:
    lectura = mq3.read()

    # Calcular porcentaje con ajuste
    if lectura <= UMBRAL_ADC_BASE:
        porcentaje = 0
    else:
        porcentaje = ((lectura - UMBRAL_ADC_BASE) / (1023 - UMBRAL_ADC_BASE)) * 100

    if porcentaje > UMBRAL_PORCENTAJE:
        ahora = time.ticks_ms()
        tiempo_transcurrido = time.ticks_diff(ahora, ultimo_toggle)

        if mostrar_oled and tiempo_transcurrido >= 100:  # 100 ms prendido
            mostrar_oled = False
            ultimo_toggle = ahora
        elif not mostrar_oled and tiempo_transcurrido >= 200:  # 200 ms apagado
            mostrar_oled = True
            ultimo_toggle = ahora

        if mostrar_oled:
            dibujar_barra(lectura)
        else:
            oled.fill(0)
            oled.show()
    else:
        dibujar_barra(lectura)
        mostrar_oled = True
        ultimo_toggle = time.ticks_ms()

    time.sleep(0.05)
