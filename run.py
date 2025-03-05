# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

import os 
from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app)  # Habilita CORS en toda la API

port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto automáticamente
app.run(host="0.0.0.0", port=port)
