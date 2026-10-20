from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.product import Product
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

service = ProductService()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Aqui empezamos a crear las rutas
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.post("/")
def create_product(product: Product, db: Session =Depends(get_db)):
    return service.create(db, product)

