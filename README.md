# Proyecto de Implementación del Patrón Fachada en Flask

- **Nombre:** Gerardo Isidro Herrera Pacheco
- **Matrícula:** ISC 68612
- **Semestre:** 8vo
- Materia: Temas selectos de Programación
- **Maestro:** Jose C Aguilar Canepa
- **Institución:** Universidad Autónoma de Campeche, Facultad de Ingeniería

# Sistema de Biblioteca API

API para la gestión de una biblioteca utilizando el patrón de diseño Fachada. Permite registrar y buscar libros, usuarios y gestionar préstamos de libros.

## Acceso a la API

1. **Desde el servidor en producción:**
   - Puedes acceder a la documentación Swagger en: [https://fachada-project.onrender.com/api/docs/](https://fachada-project.onrender.com/api/docs/) 
   - Nota: El enlace principal no tiene una interfaz gráfica, no está implementado, solo la interfaz de la API, por lo que no redirige a ninguna página visible.

2. **Ejecutar en local:**
   - Clona el repositorio o descarga el archivo ZIP y descomprímelo.
   - Abre el proyecto en tu editor favorito.
   - Crea un entorno virtual y activa la dependencia de los paquetes:
     ```bash
     python -m venv venv
     source venv/bin/activate  # En Linux/macOS
     venv\Scripts\activate  # En Windows
     pip install -r requirements.txt
     ```
   - Modifica el archivo `run.py`:
     - Descomenta:
       ```python
       # from app import create_app
       # app = create_app()
       # if __name__ == 'main':
       #     app.run(debug=True)
       ```
     - Comenta la configuración de producción para habilitar el entorno local.
   - Ejecuta el servidor con:
     ```bash
     python run.py
     ```
   - Accede a la documentación en: [https://localhost/api/docs/](https://localhost/api/docs/)

## Estructura del Proyecto

```
biblioteca_sistema/
│-- requirements.txt
│-- run.py
│-- venv/ (entorno virtual)
│-- app/
│   │-- __init__.py
│   │-- models/
│   │   │-- __init__.py
│   │   │-- libro.py
│   │   │-- prestamo.py
│   │   │-- usuario.py
│   │-- services/
│   │   │-- __init__.py
│   │   │-- libro_service.py
│   │   │-- prestamo_service.py
│   │   │-- usuario_service.py
│   │-- facades/
│   │   │-- __init__.py
│   │   │-- biblioteca_facade.py
│   │-- static/
│   │   │-- swagger.json
│   │-- routes/
│   │   │-- __init__.py
│   │   │-- libro_routes.py
│   │   │-- prestamo_routes.py
│   │   │-- usuario_routes.py
│   │-- utils/
│   │   │-- __init__.py
│   │   │-- database.py
```

### Uso del Patrón Fachada

El patrón Fachada se implementa a través de la clase `BibliotecaFacade`, que actúa como un punto de acceso unificado a los distintos servicios (`LibroService`, `UsuarioService` y `PrestamoService`).
- Unifica operaciones de libros, usuarios y préstamos
- Oculta la complejidad de los servicios individuales
- Proporciona una interfaz simple para realizar operaciones

- **Ejemplo de implementación en `biblioteca_facade.py`:**
  ```python
  class BibliotecaFacade:
      def __init__(self):
          self.libro_service = LibroService()
          self.usuario_service = UsuarioService()
          self.prestamo_service = PrestamoService()

      def registrar_libro(self, titulo, autor, categoria, isbn):
          libro = Libro(titulo, autor, categoria, isbn)
          return self.libro_service.crear_libro(libro)
  ```
  
Este diseño simplifica la interacción con los servicios y desacopla la lógica de la aplicación.

## Endpoints Disponibles

### **Libros**
- `POST /libros` → Crear un nuevo libro.
- `GET /libros` → Listar todos los libros.
- `GET /libros/buscar/isbn?isbn={isbn}` → Buscar libros por ISBN.
- `GET /libros/buscar/titulo?titulo={titulo}` → Buscar libros por título.
- `GET /libros/buscar/autor?autor={autor}` → Buscar libros por autor.
- `DELETE /libros/{libro_id}` → Eliminar un libro.

### **Usuarios**
- `POST /usuarios` → Registrar un nuevo usuario.
- `GET /usuarios` → Listar todos los usuarios.
- `GET /usuarios/buscar/email?email={email}` → Buscar usuarios por email.
- `DELETE /usuarios/{usuario_id}` → Eliminar un usuario.

### **Préstamos**
- `POST /prestamos` → Realizar un préstamo de libro.
- `GET /prestamos` → Listar todos los préstamos.
- `POST /prestamos/{prestamo_id}/devolver` → Devolver un libro prestado.

## Diagrama de Clases

![Diagrama clases Fachada_biblioteca](https://github.com/user-attachments/assets/2da6474b-25dc-41c7-b35d-8571c089838a)

## Componentes del Sistema

### Modelos de Datos

#### 1. Usuario
- **Atributos**:
  - `nombre`: Nombre del usuario
  - `email`: Correo electrónico del usuario
  - `telefono`: Número de teléfono del usuario

#### 2. Libro
- **Atributos**:
  - `titulo`: Título del libro
  - `autor`: Autor del libro
  - `categoria`: Categoría del libro
  - `isbn`: Código ISBN único
  - `disponible`: Estado de disponibilidad del libro

#### 3. Prestamo
- **Atributos**:
  - `libro_id`: Identificador del libro prestado
  - `usuario_id`: Identificador del usuario que realiza el préstamo
  - `fecha_prestamo`: Fecha de inicio del préstamo
  - `fecha_devolucion`: Fecha programada de devolución
  - `dias_prestamo`: Duración del préstamo en días

### Esquemas de Validación

#### 1. UsuarioSchema
- Métodos de validación:
  - `validate_nombre()`: Valida el formato del nombre
  - `validate_email()`: Verifica la estructura del correo electrónico
  - `validate_telefono()`: Comprueba el formato del número de teléfono

#### 2. LibroSchema
- Métodos de validación:
  - `validate_titulo()`: Valida el título del libro
  - `validate_autor()`: Verifica el nombre del autor
  - `validate_categoria()`: Comprueba la categoría
  - `validate_isbn()`: Valida el código ISBN

#### 3. PrestamoSchema
- Métodos de validación:
  - `validate_libro_id()`: Verifica el identificador del libro
  - `validate_usuario_id()`: Comprueba el identificador del usuario
  - `validate_fecha_prestamo()`: Valida la fecha de préstamo
  - `validate_fecha_devolucion()`: Verifica la fecha de devolución

### Servicios

#### 1. UsuarioService
- **Responsabilidades**:
  - Crear nuevos usuarios
  - Obtener usuarios por ID
  - Buscar usuarios por email
  - Eliminar usuarios
  - Listar todos los usuarios

#### 2. LibroService
- **Responsabilidades**:
  - Crear nuevos libros
  - Obtener libros por ID
  - Listar todos los libros
  - Buscar libros por ISBN, título o autor
  - Eliminar libros

#### 3. PrestamoService
- **Responsabilidades**:
  - Realizar préstamos de libros
  - Gestionar devoluciones
  - Listar todos los préstamos

### Fachada (BibliotecaFacade)

- **Objetivo**: Proporcionar una interfaz simplificada para las operaciones del sistema
- **Funcionalidades**:
  - Registrar libros
  - Registrar usuarios
  - Realizar préstamos
  - Gestionar devoluciones

### Conexión a Base de Datos

#### DatabaseConnection
- Implementa el patrón Singleton para gestionar la conexión a MongoDB
- Métodos:
  - `get_instance()`: Obtiene la instancia única de la conexión
  - `get_database()`: Recupera la base de datos

## Relaciones Principales

- Un Usuario puede realizar múltiples Préstamos
- Un Libro puede estar asociado a múltiples Préstamos
- Cada modelo tiene un esquema de validación correspondiente
- Los servicios gestionan las operaciones de cada modelo
- La fachada coordina los servicios para simplificar la interacción

## Tecnologías
- Lenguaje de Programación: Python Con Flask
- Base de Datos: MongoDB
