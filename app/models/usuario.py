from marshmallow import Schema, fields, validate

class Usuario:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

class UsuarioSchema(Schema):
    nombre = fields.Str(required=True)
    email = fields.Email(required=True)
    telefono = fields.Str(required=True, validate=validate.Length(min=10, max=15))