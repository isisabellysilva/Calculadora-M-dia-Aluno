from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/validar_notas", methods=['POST'])
def validar_notas():
    nome = request.form["nome"]
    nota1 = request.form["nota1"]
    nota2 = request.form["nota2"]
    nota3 = request.form["nota3"]
    
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome};{nota1};{nota2};{nota3}\n")

    return redirect("/")

@app.route("/consulta")
def consulta_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            notas.append({
                'nome': item[0],
                'nota1': item[1],
                'nota2': item[2],
                'nota3': item[3]
            })


    return render_template("consulta.html", inf=notas)

@app.route("/excluir_notas", methods=['GET'])
def excluir_notas():
    linha_para_excluir = int(request.args.get('linha')) 
    caminho_arquivo = 'models/notas.txt'
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    del linhas[linha_para_excluir]  

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return redirect("/consulta") 

app.run(host='127.0.0.1', port=80, debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

if __name__ == "__main__":
    app.run(debug=True)
