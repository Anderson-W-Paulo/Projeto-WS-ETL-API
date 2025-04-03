import pandas as pd
from flask import Flask, jsonify, request
import flask_cors

# Inicializar
app = Flask(__name__)
flask_cors.CORS(app)

# Carregar CSV
arquivo = 'Relatorio_cadop_modificado.csv'
df = pd.read_csv(arquivo, encoding='latin1', sep=';')

@app.route('/buscar', methods=['GET'])
def buscar():
    # Obter o valor de 'Registro_ANS' da query string
    registro_ans = request.args.get('registro_ans')

    if not registro_ans:
        return jsonify({'erro': 'Registro_ANS é necesspario'}), 400

    df['Registro_ANS'] = df['Registro_ANS'].astype(str).str.strip()
    # Filtrar o datafram pelo 'Registro_ANS'
    resultado = df[df['Registro_ANS'] == registro_ans]

    # Se não encontrar nenhum registro
    if resultado.empty:
        return jsonify({'erro': 'Registro_ANS não encontrado'}), 404

    # Selecionar as colunas principais
    resultado_principal = resultado[['CNPJ', 'Modalidade', 'Cidade', 'UF', 'Representante', 'Telefone', 'Endereco_eletronico']]

    # Converter o resultado para dicionário e retornar em formato JSON
    return jsonify(resultado_principal.to_dict(orient='records'))

'''# Rodar o serviço Flask
if __name__ == '__main__':
    app.run(debug=True)
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)