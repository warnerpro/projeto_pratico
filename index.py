from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Obtém os dados enviados pelo cliente
    data = request.get_json()

    # Verifica se os dados de login e senha foram enviados
    if not data:
        return jsonify({'error': 'Corpo da requisição não pode ser vazio'}), 400
    
    # Verifica se os campos 'login' e 'senha' estão presentes
    if 'login' not in data:
        return jsonify({'error': 'Login é necessário'}), 400
    if 'senha' not in data:
        return jsonify({'error': 'Senha é necessária'}), 400
    
    # Verifica se o 'login' e 'senha' não são vazios
    if not data['login']:
        return jsonify({'error': 'Login não pode ser vazio'}), 400
    if not data['senha']:
        return jsonify({'error': 'Senha não pode ser vazia'}), 400

    # Extrai os dados de login e senha
    login = data['login']
    senha = data['senha']

    # Retorna os mesmos dados de login e senha como resposta
    return jsonify({'login': login, 'senha': senha})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
