from flask import Flask, render_template, request

try:
    import RPi.GPIO as GPIO
except ImportError:
    from mock_gpio import GPIO

# Pin configuration
LED_PIN = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Flask setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def control_led():
    action = request.form.get('action')
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED turned ON"
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED turned OFF"
    else:
        return "Invalid action", 400

@app.route('/status', methods=['GET'])
def led_status():
    status = GPIO.input(LED_PIN)
    return "ON" if status == GPIO.HIGH else "OFF"

@app.route('/cleanup', methods=['GET'])
def cleanup():
    GPIO.cleanup()
    return "GPIO cleaned up. Safe to shut down."

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        GPIO.cleanup()