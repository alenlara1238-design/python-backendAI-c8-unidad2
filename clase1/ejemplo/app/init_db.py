from app.database import Base, engine
from app.models.product import Product
from app.models.user import User

Base.metadata.create_all(bind=engine)

print("Tablas verificadas correctamente")