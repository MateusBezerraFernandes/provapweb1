from flask import Flask, render_template

app = Flask(__name__)

funcionarios = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/adicionar_funcionarios', methods=['POST'])
def adicionar_funcionarios():
    nome = request.form.get('nome')  # Obtém o valor do campo 'nome' do formulário
    cargo = request.form.get('cargo')  # Obtém o valor do campo 'cargo' do formulário

    funcionario = {
        'nome': nome,
        'cargo': cargo
    }
    funcionarios.append(funcionario)

    return render_template('adicionar_funcionarios.html')

@app.route('/editar_funcionarios')
def editar_funcionarios():
    return render_template('editar_funcionarios.html')

@app.route('/listfun')
def listfun():
    return render_template('listfun.html')

if __name__ == '__main__':
    app.run(debug=True)