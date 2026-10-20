from fastapi import FastApi

from app.controllers.product_controller import router as product_router

# Crea la aplicacion FastAPI
app = FastApi(title="Products API")

# Registra las rutas de los productos
app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "Products API funcionando"}

