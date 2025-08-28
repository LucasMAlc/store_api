from store.controllers.product import router as product
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(product, prefix="/products")
