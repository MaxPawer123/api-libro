from app.database import db

class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.String(50), nullable=False)
    disponibilidad = db.Column(db.String(50), nullable=False)

    def __init__(self, autor, titulo, edicion, disponibilidad):
        self.autor = autor
        self.titulo = titulo
        self.edicion = edicion
        self.disponibilidad = disponibilidad

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Libro.query.all()

    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

    def update(self, autor=None, titulo=None, edicion=None, disponibilidad=None):
        if autor is not None:
            self.autor = autor
        if titulo is not None:
            self.titulo = titulo
        if edicion is not None:
            self.edicion = edicion
        if disponibilidad is not None:
            self.disponibilidad = disponibilidad
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
