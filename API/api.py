from flask import Flask
import commands

app = Flask(__name__)

@app.route('/')
def index():
	return "Hola Mundo!"

@app.route('/api/adelante')
def saludo():
	commands.getoutput('python /home/pi/Robot/Movimientos/Avanzar.py')
	return "El carro avanza hacia adelante"

@app.route('/api/reversa')
def reversa():
	commands.getoutput('python /home/pi/Robot/Movimientos/Retroceder.py')
	return "El carro avanza en reversa"

@app.route('/api/izquierda')
def izquierda():
	commands.getoutput('python /home/pi/Robot/Movimientos/IzquierdaAdelante.py')
	return "El carro gira a la izquierda de frente"

@app.route('/api/derecha')
def Derecha():
	commands.getuotput('python /home/pi/Robot/Movimientos/DerechaAdelante.py')
	return "El carro gira a la derecha de frente"

@app.route('/api/detener')
def detener():
	commands.getoutput('python /home/pi/Robot/Movimientos/Detener.py')
	return "El Carro se ha detenido"


if __name__ == '__main__':
	app.run(debug= True, port=5000, host="0.0.0.0")
