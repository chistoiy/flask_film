from film import create_app
from film import db

app = create_app()
if __name__ == "__main__":
    #db.create_all()
    app.run()
