from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def pagina_inicial():
  return render_template('pagina-inicial.html')


@app.route('/sobre')
def sobre_nos():
  return render_template('sobre-nos.html')

@app.route('/contato')
def contato():
  return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)