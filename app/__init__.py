from flask import Flask, render_template
app = Flask(__name__) #instanciando classe flask

#endereço do site
@app.route('/') #rota principal
@app.route('/index') #rota alternativa

def index():
    #return "Hello Word "
    nome='qualquer' #variavel
    dados={"profissao":"SRE", "cidade":"Santa Rosa"} #variavel lista
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/Contato') #rota página contato
def contato(): #define função contato
    return render_template('Contato.html')


app.run()