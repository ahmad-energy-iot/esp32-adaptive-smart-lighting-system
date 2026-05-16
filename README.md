# ESP32 Adaptive Smart Lighting System  
## ESP32 Adaptives Smart-Beleuchtungssystem

---

#  Deutsch

## Projektbeschreibung

Dieses Projekt demonstriert ein intelligentes adaptives Beleuchtungssystem mit ESP32, PWM-Technologie und einem LDR-Lichtsensor.

Der ESP32 misst kontinuierlich die Lichtintensität der Umgebung und steuert automatisch die Helligkeit der LEDs.

- Bei Dunkelheit werden die LEDs heller.
- Bei mittlerer Beleuchtung werden die LEDs schwächer.
- Bei starkem Licht werden die LEDs vollständig ausgeschaltet.

Die grüne LED und die rote LED sind parallel mit GPIO14 verbunden und reagieren gleichzeitig auf Änderungen der Umgebungsbeleuchtung.

Das System verwendet PWM (Pulse Width Modulation), um sanfte und dynamische Helligkeitsübergänge zu ermöglichen.

---

# Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | WiFi Mikrocontroller |
| LDR Sensor | Misst Lichtintensität |
| Grüne LED | Adaptive Beleuchtung |
| Rote LED | Parallel verbundene LED |
| Widerstände | Strombegrenzung |
| Breadboard | Elektronische Verbindungen |
| MicroPython | Programmiersprache |

---

# Systemverhalten

- Dunkelheit → LEDs werden heller.
- Mittlere Beleuchtung → LEDs leuchten schwächer.
- Helle Umgebung → LEDs schalten sich aus.
- PWM ermöglicht sanfte Helligkeitsübergänge.
- Der interne blaue ESP32 LED dient als Statusanzeige.

---

# Verdrahtung

| Komponente | ESP32 Pin |
|---|---|
| LDR AO | GPIO34 |
| LEDs | GPIO14 |
| Interne LED | GPIO2 |
| VCC | 3V3 |
| GND | GND |

---

# MicroPython Code

```python
from machine import Pin, ADC, PWM
import time

# PWM LED on GPIO14
green_led = PWM(Pin(14))
green_led.freq(1000)

# Internal ESP32 LED
internal_led = Pin(2, Pin.OUT)

# Light sensor
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

print("Adaptive Smart Lighting System Running...")

while True:

    # Read light value
    light_value = light_sensor.read()

    print("Light Value:", light_value)

    # Strong light
    if light_value < 1800:

        brightness = 0
        internal_led.off()

    # Medium light
    elif light_value < 2300:

        brightness = 400
        internal_led.on()

    # Darkness
    else:

        brightness = 1023
        internal_led.on()

    # Apply brightness
    green_led.duty(brightness)

    time.sleep(0.5)
```

---

# Projektbilder


#  English

## Project Description

This project demonstrates an intelligent adaptive lighting system using ESP32, PWM technology, and an LDR light sensor.

The ESP32 continuously monitors ambient light intensity and automatically controls LED brightness.

- In dark environments, the LEDs become brighter.
- In medium lighting, the LEDs become dimmer.
- In bright environments, the LEDs turn OFF completely.

The green LED and red LED are connected in parallel to GPIO14 and react simultaneously to environmental light changes.

The system uses PWM (Pulse Width Modulation) to create smooth and dynamic brightness transitions.

---

# Components Used

| Component | Description |
|---|---|
| ESP32 DevKit V1 | WiFi-enabled microcontroller |
| LDR Sensor | Measures light intensity |
| Green LED | Adaptive lighting |
| Red LED | Parallel connected LED |
| Resistors | Current limiting |
| Breadboard | Electronic connections |
| MicroPython | Programming language |

---

# System Behavior

- Dark environment → LEDs become brighter.
- Medium light → LEDs operate with dim brightness.
- Bright environment → LEDs turn OFF.
- PWM provides smooth brightness transitions.
- Internal ESP32 blue LED works as a status indicator.

---

# Wiring

| Component | ESP32 Pin |
|---|---|
| LDR AO | GPIO34 |
| LEDs | GPIO14 |
| Internal LED | GPIO2 |
| VCC | 3V3 |
| GND | GND |

---

# MicroPython Code

```python
from machine import Pin, ADC, PWM
import time

# PWM LED on GPIO14
green_led = PWM(Pin(14))
green_led.freq(1000)

# Internal ESP32 LED
internal_led = Pin(2, Pin.OUT)

# Light sensor
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

print("Adaptive Smart Lighting System Running...")

while True:

    # Read light value
    light_value = light_sensor.read()

    print("Light Value:", light_value)

    # Strong light
    if light_value < 1800:

        brightness = 0
        internal_led.off()

    # Medium light
    elif light_value < 2300:

        brightness = 400
        internal_led.on()

    # Darkness
    else:

        brightness = 1023
        internal_led.on()

    # Apply brightness
    green_led.duty(brightness)

    time.sleep(0.5)
```

---



# Developer

## Ahmad Azroun

Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer

---
