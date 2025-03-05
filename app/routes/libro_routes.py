from flask import Blueprint, request, jsonify
from app.facades.biblioteca_facade import BibliotecaFacade

libro_bp = Blueprint('libro', __name__)
biblioteca_facade = BibliotecaFacade()

@libro_bp.route('/libros', methods=['POST'])
def crear_libro():
    data = request.json
    try:
        libro_id = biblioteca_facade.registrar_libro(
            data['titulo'], 
            data['autor'], 
            data['categoria'], 
            data['isbn']
        )
        return jsonify({"id": libro_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@libro_bp.route('/libros/buscar/isbn', methods=['GET'])
def buscar_por_isbn():
    isbn = request.args.get('isbn')
    if not isbn:
        return jsonify({"error": "ISBN es requerido"}), 400
    
    try:
        libros = biblioteca_facade.buscar_libros_por_isbn(isbn)
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@libro_bp.route('/libros/buscar/titulo', methods=['GET'])
def buscar_por_titulo():
    titulo = request.args.get('titulo')
    if not titulo:
        return jsonify({"error": "Título es requerido"}), 400
    
    try:
        libros = biblioteca_facade.buscar_libros_por_titulo(titulo)
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@libro_bp.route('/libros/buscar/autor', methods=['GET'])
def buscar_por_autor():
    autor = request.args.get('autor')
    if not autor:
        return jsonify({"error": "Autor es requerido"}), 400
    
    try:
        libros = biblioteca_facade.buscar_libros_por_autor(autor)
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@libro_bp.route('/libros/<libro_id>', methods=['DELETE'])
def eliminar_libro(libro_id):
    try:
        resultado = biblioteca_facade.eliminar_libro(libro_id)
        if resultado:
            return jsonify({"mensaje": "Libro eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@libro_bp.route('/libros', methods=['GET'])
def listar_libros():
    try:
        libros = biblioteca_facade.listar_todos_libros()
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400