from fastapi import APIRouter, Query, HTTPException, status


router = APIRouter()


@router.get("/{author_id}/{age}/{city}/")
async def author_detail(author_id: int, age: int, city: str):
    print(author_id, city, age)
    print(type(author_id))
    print(author_id * 100 + 10)

    return {"author_id": author_id}


@router.get("/")
async def author_detail(
    name: str = Query(None, description="Name author"),
    age: int = Query(None, description="Age author"),
    city: str = Query(None, description="City author"),
):
    print(name, age, city)

    return {"author": f"{name} {age} {city}"}