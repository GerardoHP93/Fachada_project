# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app)  # Habilita CORS para toda la API

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Asegura que Render lo ejecute en el puerto correcto