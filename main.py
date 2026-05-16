from machine import Pin, ADC, PWM
import time

# Green LED with PWM on GPIO14
green_led = PWM(Pin(14))
green_led.freq(1000)

# Internal LED on GPIO2
internal_led = Pin(2, Pin.OUT)

# Light sensor on GPIO34
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

print("Smart PWM Automatic Lighting System Running...")

while True:
    light_value = light_sensor.read()
    print("Light value:", light_value)

    # Your sensor:
    # lower value = more light
    # higher value = more darkness

    if light_value < 1800:
        brightness = 0
        internal_led.off()
        print("Bright -> Green LED OFF")

    elif light_value >= 1800 and light_value < 2300:
        brightness = 400
        internal_led.on()
        print("Medium Light -> Green LED DIM")

    else:
        brightness = 1023
        internal_led.on()
        print("Dark -> Green LED FULL")

    green_led.duty(brightness)

    time.sleep(0.5)