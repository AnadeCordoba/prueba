from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Mi pagina de prueba</title>
  </head>
  <body>
    <h1>La foto de Duna</h1>
        <h2> Es la más bonita</h2>
    <img src="file:////Users/ana/Desktop/pruebarepositorio/DSC_0601.jpg"/>
  </body>
</html> '''

if __name__ == '__main__':
    app.run()
    