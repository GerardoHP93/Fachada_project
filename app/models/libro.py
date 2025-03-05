from marshmallow import Schema, fields, validate

class Libro:
    def __init__(self, titulo, autor, categoria, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = disponible

class LibroSchema(Schema):
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)
    categoria = fields.Str(required=True)
    isbn = fields.Str(required=True, validate=validate.Length(equal=13))
    disponible = fields.Bool(dump_default=True)