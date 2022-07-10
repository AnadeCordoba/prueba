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
    <img src="DSC_0601.jpg" alt="Mi imagen de prueba">
  </body>
</html> '''

if __name__ == '__main__':
    app.run()
    