from sqlalchemy import select
from sqlalchemy import Session

from app.models.user import User

class UserRepository:

    def get_all(self, db:Session) -> list[User]:
        statement = select(User)
        return list(db.scalars(statement).all())
    
    def get_by_email(self, db: Sesion, user_email: str) -> User:
        return db.get(User, user_email)
    
    def get_by_id(self, db: Session, user_id: int) -> User:
        return db.get(User, user_id)

    
    def create(self, db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def update(self, db: Session, user: User, username: str, email: str) -> User:
        user.username = username
        user.email = email

        db.commit()
        db.refresh(user)

        return user
    
    def delete(self, db: Session, user: User) -> None:
        db.delete(user)
        db.commit()

    