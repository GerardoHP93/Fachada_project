from app.utils.database import DatabaseConnection
from bson.objectid import ObjectId

class UsuarioService:
    def __init__(self):
        self.db = DatabaseConnection.get_database()
        self.collection = self.db['usuarios']

    def crear_usuario(self, usuario):
        result = self.collection.insert_one(usuario.__dict__)
        return str(result.inserted_id)

    def obtener_usuario_por_id(self, usuario_id):
        usuario = self.collection.find_one({"_id": ObjectId(usuario_id)})
        return self._convertir_objectid(usuario) if usuario else None

    def buscar_usuarios(self, filtro=None):
        filtro = filtro or {}
        usuarios = list(self.collection.find(filtro))
        return self._convertir_lista_objectid(usuarios)

    def buscar_por_email(self, email):
        usuarios = list(self.collection.find({"email": {"$regex": email, "$options": "i"}}))
        return self._convertir_lista_objectid(usuarios)

    def eliminar_usuario(self, usuario_id):
        resultado = self.collection.delete_one({"_id": ObjectId(usuario_id)})
        return resultado.deleted_count > 0

    def listar_todos_usuarios(self):
        usuarios = list(self.collection.find())
        return self._convertir_lista_objectid(usuarios)

    def _convertir_objectid(self, documento):
        """Convierte ObjectId a string en un documento"""
        if documento and '_id' in documento:
            documento['_id'] = str(documento['_id'])
        return documento

    def _convertir_lista_objectid(self, documentos):
        """Convierte lista de documentos con ObjectId a documentos con _id como string"""
        return [self._convertir_objectid(doc) for doc in documentos]