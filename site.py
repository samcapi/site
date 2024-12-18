from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aleatoria'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

# Criação do banco de dados
with app.app_context():
    db.create_all()

produtos = {
    "1": {
        "nome": "Relógio Invicta Venom",
        "preco": "940.50",
        "imagem": "imagens/relogio1.png",
        "descricao": "Relógio de luxo com design robusto e resistência à água.",
        "especificacoes": "Resistência à água até 200 metros, movimento de quartzo."
    },
    "2": {
        "nome": "Relógio Festina Masculino Aço Prateado",
        "preco": "553,00",
        "imagem": "imagens/relogio2.png",
        "descricao": "Elegância e sofisticação em cada detalhe.",
        "especificacoes": "Feito em aço inoxidável, com pulseira de couro."
    },
    "3": {
        "nome": "Relógio Masculino Orient",
        "preco": "758.00",
        "imagem": "imagens/relogio3.png",
        "descricao": "Relógio clássico e atemporal, ideal para qualquer ocasião.",
        "especificacoes": "Movimento automático, vidro mineral."
    },
    "4": {
        "nome": "Z Relógio Eletrônico Analógico Digital",
        "preco": "157,80",
        "imagem": "imagens/relogio4.png",
        "descricao": "Versátil e prático, perfeito para atividades ao ar livre.",
        "especificacoes": "Função cronômetro, resistência à água."
    },
    "5": {
        "nome": "Relógio Santis Nautilus Aço Inoxidável Polido Preto",
        "preco": "167,00",
        "imagem": "imagens/relogio5.png",
        "descricao": "Estilo moderno com um toque clássico.",
        "especificacoes": "Mostrador analógico, pulseira de aço inoxidável."
    },
    "6": {
        "nome": "Curren-relógio De Pulso Masculino De Quartzo",
        "preco": "215,20",
        "imagem": "imagens/relogio6.png",
        "descricao": "Design elegante com funcionalidade de alto nível.",
        "especificacoes": "Movimento de quartzo, resistente a riscos."
    },
    "7": {
        "nome": "Fone De Ouvido F9-5 Tws Bluetoth Sem Fio Cor Da Luz Azul",
        "preco": "19,80",
        "imagem": "imagens/fone1.png",
        "descricao": "Fones de ouvido sem fio com boa qualidade de som.",
        "especificacoes": "Bluetooth 5.0, autonomia de até 5 horas."
    },
    "8": {
        "nome": "Fone De Ouvido Sem Fio Wireless M10 Damix Bluetooth Preto",
        "preco": "49,90",
        "imagem": "imagens/fone2.png",
        "descricao": "Design ergonômico e leve, ideal para longas horas de uso.",
        "especificacoes": "Cancelamento de ruído ativo, microfone embutido."
    },
    "9": {
        "nome": "Fone De Ouvido Bluetooth Sem Fio Com Microfone Gamer 510 Bt",
        "preco": "46,74",
        "imagem": "imagens/fone3.png",
        "descricao": "Fones ideais para gamers com áudio imersivo.",
        "especificacoes": "Bateria de longa duração, ajuste de volume."
    },
    "10": {
        "nome": "Fones de ouvido para dormir, máscara ocular Bluetooth, sem fio, Bluetooth 5.2",
        "preco": "40,00",
        "imagem": "imagens/fone4.png",
        "descricao": "Perfeitos para quem precisa de conforto ao dormir.",
        "especificacoes": "Confortável, com som de qualidade."
    },
    "11": {
        "nome": "Óculos de Sol Sunzest Cruiser - Preto Fosco",
        "preco": "99,00",
        "imagem": "imagens/oculos1.png",
        "descricao": "Óculos elegantes com proteção UV.",
        "especificacoes": "Lentes polarizadas, material leve."
    },
    "12": {
        "nome": "Óculos de Sol Sunzest Grind - Preto Polarizado",
        "preco": "59,40",
        "imagem": "imagens/oculos2.png",
        "descricao": "Estilo e proteção em um só produto.",
        "especificacoes": "Resistência a impactos, lentes de alta definição."
    },
    "13": {
        "nome": "Óculos de sol Sunzest Miami - Preto Brilhante",
        "preco": "99,00",
        "imagem": "imagens/oculos3.png",
        "descricao": "Óculos que oferecem estilo e conforto.",
        "especificacoes": "Design unissex, lentes UV400."
    },
    "14": {
        "nome": "Óculos de Sol Oxer com Proteção Solar Casual Redondo Adulto",
        "preco": "49,99",
        "imagem": "imagens/oculos4.png",
        "descricao": "Óculos casuais para uso diário.",
        "especificacoes": "Material resistente, lentes polarizadas."
    },
    "15": {
        "nome": "Apple Watch SE GPS (2da gen) - Caixa meia-noite de alumínio 44 mm ",
        "preco": "2.098",
        "imagem": "imagens/relogio7.png",
        "descricao": "Óculos casuais para uso diário.",
        "especificacoes": "Material resistente, lentes polarizadas."

    },
    "16": {
            "nome": "Relógio Casio Masculino Digital World Time AE-1200WHD ",
            "preco": "299,00",
            "imagem": "imagens/relogio8.png",
            "descricao": "Óculos casuais para uso diário.",
            "especificacoes": "Material resistente, lentes polarizadas."

        }
}


# Rotas
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Agora você pode fazer login.')
        return redirect(url_for('homepage.html'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Login realizado com sucesso!')
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/relogios')
def relogios():
    return render_template('relogios.html')

@app.route('/fones')
def fones():
    return render_template('fones.html')

@app.route('/oculos')
def oculos():
    return render_template('oculos.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/pagamento')
def pagamento():
    produto_id = request.args.get('produto_id')  # Obtém o ID do produto
    produto = produtos.get(produto_id)  # Busca o produto no dicionário

    if not produto:  # Caso o produto não seja encontrado
        flash("Produto não encontrado.")
        return redirect(url_for('home'))

    # Extrai as informações do produto
    nome = produto["nome"]
    preco = produto["preco"]
    imagem = url_for('static', filename=produto["imagem"])
    descricao = produto["descricao"]  # Adicionado
    especificacoes = produto["especificacoes"]  # Adicionado

    # Renderiza a página de pagamento com todas as informações
    return render_template(
        'pagamento.html',
        nome=nome,
        preco=preco,
        imagem=imagem,
        descricao=descricao,
        especificacoes=especificacoes
    )


    return render_template('pagamento.html', nome=nome, preco=preco, imagem=imagem)

@app.route('/confirmar-pagamento', methods=['POST'])
def confirmar_pagamento():
    produto_nome = request.form['produto_nome']
    preco = request.form['preco']
    metodo = request.form['metodo']
    imagem = request.form['imagem']

    # Aqui você pode adicionar alguma lógica de registro ou processamento do pagamento
    flash(f"Pagamento confirmado! Você comprou {produto_nome} por R$ {preco} usando {metodo}.")

    # Redirecionar para a página de confirmação
    return redirect(url_for('confirmacao'))

@app.route('/confirmacao')
def confirmacao():
    return render_template('confirmacao.html')


# Outras rotas e tratamento de erro
@app.errorhandler(404)
def not_found_error(error):
    print(f"Erro 404: {request.url}")  # Log para identificar a URL que está falhando
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
