from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product

class ProductRepository:

    def get_all(self, db: Session) -> list[Product]:
        statement = select(Product)
        return list(db.scalars(statement).all())
    
    def get_by_id(self, db:Session, product_id: int) -> Product | None:
        return db.get(Product, product_id)
    
    def create(self, db:Session, product:Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product