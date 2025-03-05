from marshmallow import Schema, fields
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, libro_id, usuario_id, fecha_prestamo=None, fecha_devolucion=None):
        self.libro_id = libro_id
        self.usuario_id = usuario_id
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.fecha_devolucion = fecha_devolucion or (self.fecha_prestamo + timedelta(days=14))

class PrestamoSchema(Schema):
    libro_id = fields.Str(required=True)
    usuario_id = fields.Str(required=True)
    fecha_prestamo = fields.DateTime(dump_default=datetime.now)
    fecha_devolucion = fields.DateTime()