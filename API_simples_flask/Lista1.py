from flask import Flask, request, jsonify, make_response
from bd import usuarios
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

current_id = len(usuarios) + 1

@app.route('/users', methods=['GET'])
def read_all():
    return make_response(jsonify(mensagem="Lista de usuarios.", dados= usuarios), 200)

@app.route('/users', methods = ['POST'])
def create():
    global current_id
    user = request.json
    user["id"] = current_id
    current_id += 1
    
    usuarios.append(user)
    return make_response(jsonify(mensagem="Usuario cadastrado com sucesso.", usuario= user), 201) 

@app.route("/users/<int:id>", methods = ['GET'])
def read_single(id):
    for user in usuarios:
        if user["id"] == id:
            return make_response(jsonify(user), 200)
    return make_response(jsonify({"erro": "Usuario nao encontrado"}), 404)

@app.route("/users/<int:id>", methods =['PUT'])
def update(id):
    for user in usuarios:
        if user["id"] == id:
            novo = request.json
            user.update(novo)
            return make_response(jsonify(mensagem="Usuario atualizado com sucesso.", usuario= user), 200)
    return make_response(jsonify({"erro": "Usuario nao encontrado"}), 404)

@app.route("/users/<int:id>", methods = ['DELETE'])
def delete(id):
    for user in usuarios:
        if user["id"] == id:
            usuarios.remove(user)
            return make_response(jsonify(mensagem = "Usuario excluido com sucesso"), 200)
    return make_response(jsonify({"erro": "Usuario nao encontrado"}), 404)



if __name__ == '__main__':
    app.run(debug=True, port=5001)