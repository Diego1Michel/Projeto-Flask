from flask import Flask, flash, redirect, render_template, request
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

@app.route('/produtos') #rota página contato
def produtos(): #define função contato
    return render_template('produtos.html')

@app.route('/login') #rota página contato
def login(): #define função contato
    return render_template('login.html')

# @app.route('/autenticar' , method=['GET']) #rota página contato
# def autenticar(): #define função contato
#     usuario = request.args.get('usuario')
#     senha = request.args.get('senha')
#     return "usuario:{} e senha:{}" .format(usuario,senha)

# chave secreta para poder realizar o redirect da página
app.config['SECRET_KEY'] = "minha-chave"


@app.route('/autenticar', methods=['POST']) #rota página contato
def autenticar(): #define função contato
    usuario = request.form.get('usuario') #enviar form
    senha = request.form.get('senha') 
    if (usuario=='admin' and senha=='12345'):
        return "usuario:{} e senha:{}" .format(usuario,senha)   
    else:
        flash('Dados Inválidos!')
        return redirect('/login')
    


app.run()