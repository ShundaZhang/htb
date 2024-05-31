from application.app import app
from application.util.database import Database

if __name__ == "__main__":
    Database().migrate()
    app.run(host="0.0.0.0", port=3000, threaded=True, debug=False)