from app.utils.database import DatabaseConnection
from bson.objectid import ObjectId
from datetime import datetime, timedelta

class PrestamoService:
    def __init__(self):
        self.db = DatabaseConnection.get_database()
        self.prestamos_collection = self.db['prestamos']
        self.libros_collection = self.db['libros']

    def realizar_prestamo(self, libro_id, usuario_id, dias_prestamo=14):
        libro = self.libros_collection.find_one({"_id": ObjectId(libro_id), "disponible": True})
        
        if not libro:
            raise ValueError("El libro no está disponible")

        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=dias_prestamo)

        prestamo = {
            "libro_id": ObjectId(libro_id),
            "usuario_id": ObjectId(usuario_id),
            "fecha_prestamo": fecha_prestamo,
            "fecha_devolucion": fecha_devolucion,
            "dias_prestamo": dias_prestamo
        }

        result = self.prestamos_collection.insert_one(prestamo)
        
        # Actualizar disponibilidad del libro
        self.libros_collection.update_one(
            {"_id": ObjectId(libro_id)},
            {"$set": {"disponible": False}}
        )

        return str(result.inserted_id)

    def devolver_libro(self, prestamo_id):
        prestamo = self.prestamos_collection.find_one({"_id": ObjectId(prestamo_id)})
        
        if not prestamo:
            raise ValueError("Préstamo no encontrado")

        # Actualizar disponibilidad del libro
        self.libros_collection.update_one(
            {"_id": prestamo['libro_id']},
            {"$set": {"disponible": True}}
        )

        # Eliminar préstamo
        self.prestamos_collection.delete_one({"_id": ObjectId(prestamo_id)})

        return True
    
    def listar_todos_prestamos(self):
        prestamos = list(self.prestamos_collection.aggregate([
        {
            "$lookup": {
                "from": "libros",
                "localField": "libro_id",
                "foreignField": "_id",
                "as": "libro"
            }
        },
        {
            "$lookup": {
                "from": "usuarios",
                "localField": "usuario_id",
                "foreignField": "_id",
                "as": "usuario"
            }
        },
        {
            "$unwind": "$libro"
        },
        {
            "$unwind": "$usuario"
        },
        {
            "$project": {
                "_id": {"$toString": "$_id"},
                "libro": {
                    "_id": {"$toString": "$libro._id"},
                    "titulo": "$libro.titulo",
                    "autor": "$libro.autor"
                },
                "usuario": {
                    "_id": {"$toString": "$usuario._id"},
                    "nombre": "$usuario.nombre",
                    "email": "$usuario.email"
                },
                "fecha_prestamo": 1,
                "fecha_devolucion": 1,
                "dias_prestamo": 1
            }
        }
    ]))
    
        return list(prestamos)