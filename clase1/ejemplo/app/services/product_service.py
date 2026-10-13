

class ProductService:

    def __init__(self):
        self.repository = Product_repository()
    
    def get_all(self, db:Session) -> list[Product]:
        return self.repository.get_all(db)

    def get_by_id(self, db:Session, product_id: int): -> Product | None:
        return self.repository.get_by_id(db, product_id)

    def create(self, db:Session, product: Product) -> Product:
        # regla 1: el nombre no puede estar vacio
        if not product.name.strip():
            raise ValueError("El nombre del producto es obligatorio")
        
        # regla 2: el precio debe ser maor a cero
        if product.price <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero")
        
        # aqui las instrucciones si no se violentó ninguna regla
        return self.repository.create(db, product)

        

    