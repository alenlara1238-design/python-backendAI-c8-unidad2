from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:
    
    #constructor
    def __init__(self):
        self.repository = UserRepository()
    
    def get_all(self, db: Session) -> list[User]:
        return self.repository.get_all(db)
    
    def get_by_id(self, db: Session, user_id: int) -> User:
        return self.repository.get_by_id(db, user_id)
    
    def create(self, db: Session, username: str, email: str) -> User:

        # regla 0: si el usuario existe previamente, entonces no se puede volver a crear.
        user_exist = repository.get_by_email(db, email)

        if user_exist is not None:
            raise ValueError("Ya existe un usuairo con ese email")

        #regla 1: el nombre no puede estar vacio
        if not username.strip():
            raise ValueError("El nombre del usuario es obligatorio")

        # regla 2: el corre no puede estar vacío
        if not email.strip():
            raise ValueError("El correo del usuario es obligatorio")
        
        user = User(username=username, email=email)

        return self.repository.create(db, user)

    
    def update(self, db: Session, user_id: int, username: str, email: str) -> User:
        
        #regla 1: verificar si el usuario existe previamente
        user = self.repository.get_by_id(db, user_id)

        if user is None:
            raise ValueError("El usuario que intenta editar no existe")
        
        #valida los nuevos datos
        if not username.strip():
            raise ValueError("El nombre del usuario es obligatorio")
        
        if not email.strip():
            raise ValueError("El correo del usuario es obligatorio")
        
        return self.repository.update(db, user, username, email)
    
    def delete(self, db: Session, user_id: int) -> None:
        #regla 1: verificar si el usuario existe previamente
        user = self.repository.get_by_id(db, user_id)

        if user is None:
            raise ValueError("El usuario que itenta eliminar no existe")
        
        self.repository.delete(db, user)