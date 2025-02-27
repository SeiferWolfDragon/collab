from flask import Flask
#comentario de prueba
app = Flask(__name__)
##Esto es una linea para decirte que eres bien homosexual
@app.route('/')
def hello_world():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)