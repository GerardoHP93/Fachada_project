from app.services.libro_service import LibroService
from app.services.usuario_service import UsuarioService
from app.services.prestamo_service import PrestamoService
from app.models.libro import Libro, LibroSchema
from app.models.usuario import Usuario, UsuarioSchema
from app.models.prestamo import Prestamo, PrestamoSchema

class BibliotecaFacade:
    def __init__(self):
        self.libro_service = LibroService()
        self.usuario_service = UsuarioService()
        self.prestamo_service = PrestamoService()
        self.libro_schema = LibroSchema()
        self.usuario_schema = UsuarioSchema()
        self.prestamo_schema = PrestamoSchema()

    def registrar_libro(self, titulo, autor, categoria, isbn):
        libro = Libro(titulo, autor, categoria, isbn)
        libro_dict = self.libro_schema.dump(libro)
        return self.libro_service.crear_libro(libro)

    def registrar_usuario(self, nombre, email, telefono):
        usuario = Usuario(nombre, email, telefono)
        usuario_dict = self.usuario_schema.dump(usuario)
        return self.usuario_service.crear_usuario(usuario)

    def buscar_libros_por_isbn(self, isbn):
        return self.libro_service.buscar_por_isbn(isbn)

    def buscar_libros_por_titulo(self, titulo):
        return self.libro_service.buscar_por_titulo(titulo)

    def buscar_libros_por_autor(self, autor):
        return self.libro_service.buscar_por_autor(autor)

    def buscar_usuarios_por_email(self, email):
        return self.usuario_service.buscar_por_email(email)

    def eliminar_libro(self, libro_id):
        return self.libro_service.eliminar_libro(libro_id)
    
    def listar_todos_usuarios(self):
        return self.usuario_service.listar_todos_usuarios()

    def listar_todos_libros(self):
        return self.libro_service.listar_todos_libros()

    def listar_todos_prestamos(self):
        return self.prestamo_service.listar_todos_prestamos()

    def eliminar_usuario(self, usuario_id):
        return self.usuario_service.eliminar_usuario(usuario_id)

    def prestar_libro(self, libro_id, usuario_id, dias_prestamo=14):
        return self.prestamo_service.realizar_prestamo(libro_id, usuario_id, dias_prestamo)

    def devolver_libro(self, prestamo_id):
        return self.prestamo_service.devolver_libro(prestamo_id)