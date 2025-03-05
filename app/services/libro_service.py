from app.utils.database import DatabaseConnection
from bson.objectid import ObjectId

class LibroService:
    def __init__(self):
        self.db = DatabaseConnection.get_database()
        self.collection = self.db['libros']

    def crear_libro(self, libro):
        result = self.collection.insert_one(libro.__dict__)
        return str(result.inserted_id)

    def obtener_libro_por_id(self, libro_id):
        libro = self.collection.find_one({"_id": ObjectId(libro_id)})
        return self._convertir_objectid(libro) if libro else None
    
    def listar_todos_libros(self):
        libros = list(self.collection.find())
        return self._convertir_lista_objectid(libros)

    def buscar_por_isbn(self, isbn):
        libros = list(self.collection.find({"isbn": isbn}))
        return self._convertir_lista_objectid(libros)

    def buscar_por_titulo(self, titulo):
        libros = list(self.collection.find({"titulo": {"$regex": titulo, "$options": "i"}}))
        return self._convertir_lista_objectid(libros)

    def buscar_por_autor(self, autor):
        libros = list(self.collection.find({"autor": {"$regex": autor, "$options": "i"}}))
        return self._convertir_lista_objectid(libros)

    def eliminar_libro(self, libro_id):
        resultado = self.collection.delete_one({"_id": ObjectId(libro_id)})
        return resultado.deleted_count > 0

    def _convertir_objectid(self, documento):
        """Convierte ObjectId a string en un documento"""
        if documento and '_id' in documento:
            documento['_id'] = str(documento['_id'])
        return documento
    

    def _convertir_lista_objectid(self, documentos):
        """Convierte lista de documentos con ObjectId a documentos con _id como string"""
        return [self._convertir_objectid(doc) for doc in documentos]