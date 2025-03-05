from flask import Blueprint, request, jsonify
from app.facades.biblioteca_facade import BibliotecaFacade

prestamo_bp = Blueprint('prestamo', __name__)
biblioteca_facade = BibliotecaFacade()

@prestamo_bp.route('/prestamos', methods=['POST'])
def realizar_prestamo():
    data = request.json
    try:
        dias_prestamo = data.get('dias_prestamo', 14)  # Por defecto 14 días
        prestamo_id = biblioteca_facade.prestar_libro(
            data['libro_id'], 
            data['usuario_id'],
            dias_prestamo
        )
        return jsonify({"id": prestamo_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@prestamo_bp.route('/prestamos/<prestamo_id>/devolver', methods=['POST'])
def devolver_libro(prestamo_id):
    try:
        biblioteca_facade.devolver_libro(prestamo_id)
        return jsonify({"mensaje": "Libro devuelto exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@prestamo_bp.route('/prestamos', methods=['GET'])
def listar_prestamos():
    try:
        prestamos = biblioteca_facade.listar_todos_prestamos()
        return jsonify(prestamos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400