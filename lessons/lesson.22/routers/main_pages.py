from fastapi import APIRouter, Query, HTTPException, status


router = APIRouter()


@router.get("/")
async def index():
    return {"Hello123": "World567"}