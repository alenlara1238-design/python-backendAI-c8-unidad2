from sqlalchemy import String
from sqlachemy.orm import Mapped, mapped_column


from app.database import Base

class Product(Base):
    __tablename__ = "products"

    # atributos del modelo producto (caracteristicas):
    #Represeta el idetificador unico
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    price: Mapped[float]

    