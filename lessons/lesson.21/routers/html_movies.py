from fastapi import APIRouter, Query, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas.movie import Movie, movie_list


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse,  name='html_movie_list')
async def html_movies(
    request: Request,
    year: int = Query(None, description="Год релиза"),
    title: str = Query(None, description="Заголовок фильма"),
):
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if title in movie.title]

    context = {
        "request": request,
        "movies": result,
        "user": 'Guest',
        "title": "Список фильмов"}
    return templates.TemplateResponse("movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name='html_movie_detail')
async def movie_details(request: Request, movie_id: int):
    """Получить детальную информацию по фильму."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")
    context = {
        "request": request,
        "movie": movie_list[movie_id],
        "user": 'Guest',
        # "title": f"Фильм {movie_list[movie_id].title}"
    }
    print(context)
    return templates.TemplateResponse("movies/movie_detail.html", context=context)

#
# @router.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
# async def create_movie(movie: Movie):
#     """Добавить фильм."""
#     for m in movie_list:
#         if m.title == movie.title and m.year == movie.year:
#             raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")
#     movie_list.append(movie)
#     return movie
#
#
# @router.put("/movies/{movie_id}/", response_model=Movie)
# async def update_movie(movie_id: int, movie: Movie):
#     """Обновить фильм."""
#     movie_id -= 1
#     if movie_id < 0 or movie_id >= len(movie_list):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")
#     movie_list[movie_id].title = movie.title
#     movie_list[movie_id].year = movie.year
#     return movie_list[movie_id]
#
#
# @router.delete("/movies/{movie_id}/")
# async def delete_movie(movie_id: int):
#     """Удалить фильм."""
#     movie_id -= 1
#     if movie_id < 0 or movie_id >= len(movie_list):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")
#
#     result = movie_list.pop(movie_id)
#     return {'message': f'Фильм {result.title} был удален'}
