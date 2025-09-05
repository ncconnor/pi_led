# pi_led


on dev machine:

pip3 install -r requirements.txt
python3 app.py

http://localhost:5001


on raspberry pi:
export FLASK_APP=app.py
flask run --host=0.0.0.0

Then go to http://<pi-ip>:5001 in your browser and you’ll see your LED switch app.