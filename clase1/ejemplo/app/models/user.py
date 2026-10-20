from sqlalchemy import String
from sqlachemy.orm import Mapped, mapped_column

from app.database import Base

class User(Base):
    __tablename__="users"

    # Identificador unico del usuario (es generado por la base de datos)
    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mappeed_column(String(50))

    email: Mapped[str] = mapped_column(String(100))

