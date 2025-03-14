from flask import Blueprint, request, jsonify
from db import create_connection

registermaintenance = Blueprint('registermaintenance', __name__)

@registermaintenance.route('/registermaintenance', methods=['POST'])
def register_registermaintenance():

    # Preciso dos dados do front... como faço?
    data = request.get_json()
    maintenance_name = data.get('maintenance_name').upper()

    # Verifica se recebi todos os dados
    if not maintenance_name:
        return jsonify ({"error": "Preencha todos os campos..."}), 400

    # Preciso criar uma conexão com o meu BD... como faço?
    connection = create_connection()
    if not connection:
        return jsonify ({"error": "Não me conectei com o bando..."}), 500
    
    try:
        cursor = connection.cursor()
        # Verificar se já tenho uma máquina com esse código...
        search_maintenance_query = """SELECT maintenance_name FROM maintenances WHERE maintenance_name = ? """
        cursor.execute(search_maintenance_query, (maintenance_name,))
        maintenance_result = cursor.fetchone()

        if maintenance_result:
            return jsonify ({"error": "Manutenção já cadastrada"}), 400

        # Se não tenho, inserir...
        insert_maintenance_data_query = """
        INSERT INTO maintenances (maintenance_name)
        VALUES (?)
        """
        cursor.execute(insert_maintenance_data_query, (maintenance_name,))

        connection.commit()

        return jsonify({"sucess": f"Manutenção {maintenance_name} cadastrada com sucesso"}), 200


    except Exception as e:
        return jsonify ({"error": f"Erro {e}"}), 500
    
    finally:
        if connection:
            connection.close()
