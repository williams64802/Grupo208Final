from src.FinalBase.modelo.Curso import Curso
from src.FinalBase.modelo.declarative_base import engine, Base, session

class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_curso(self, nombreCurso):
        busqueda = session.query(Curso).filter(Curso.nombreCurso == nombreCurso).all()
        if len(busqueda) == 0:
            curso = Curso(nombreCurso=nombreCurso)
            session.add(curso)
            session.commit()
            return True
        else:
            return False