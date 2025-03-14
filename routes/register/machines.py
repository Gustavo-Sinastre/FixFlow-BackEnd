from flask import Blueprint, request, jsonify
from db import create_connection

registermachine = Blueprint('registermachine', __name__)

@registermachine.route('/registermachine', methods=['POST'])
def register_machine():

    # Preciso dos dados do front... como faço?
    data = request.get_json()
    machine_name = data.get('machine_name').upper()
    model = data.get('model').upper()
    manufacturer = data.get('manufacturer').upper()
    code = data.get('code')

    # Verifica se recebi todos os dados
    if not machine_name or not model or not manufacturer or not code:
        return jsonify ({"error": "Preencha todos os campos..."}), 400

    # Preciso criar uma conexão com o meu BD... como faço?
    connection = create_connection()
    if not connection:
        return jsonify ({"error": "Não me conectei com o bando..."}), 500
    
    try:
        cursor = connection.cursor()
        # Verificar se já tenho uma máquina com esse código...
        search_machine_code_query = """SELECT code FROM machines WHERE code = ? """
        cursor.execute(search_machine_code_query, (code,))
        machine_code_result = cursor.fetchone()

        if machine_code_result:
            return jsonify ({"error": "Máquina já cadastrada"}), 400

        # Se não tenho, inserir...
        insert_machine_data_query = """
        INSERT INTO machines (machine_name, model, manufacturer, code)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_machine_data_query, (machine_name, model, manufacturer, code,))

        connection.commit()

        return jsonify({"sucess": "Máquina cadastrada com sucesso"}), 200


    except Exception as e:
        return jsonify ({"error": f"Erro {e}"}), 500
    
    finally:
        if connection:
            connection.close()
