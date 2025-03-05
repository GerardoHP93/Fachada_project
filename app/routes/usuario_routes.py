from flask import Blueprint, request, jsonify
from app.facades.biblioteca_facade import BibliotecaFacade

usuario_bp = Blueprint('usuario', __name__)
biblioteca_facade = BibliotecaFacade()

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    try:
        usuario_id = biblioteca_facade.registrar_usuario(
            data['nombre'], 
            data['email'], 
            data['telefono']
        )
        return jsonify({"id": usuario_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route('/usuarios/buscar/email', methods=['GET'])
def buscar_por_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email es requerido"}), 400
    
    try:
        usuarios = biblioteca_facade.buscar_usuarios_por_email(email)
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route('/usuarios/<usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    try:
        resultado = biblioteca_facade.eliminar_usuario(usuario_id)
        if resultado:
            return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = biblioteca_facade.listar_todos_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400