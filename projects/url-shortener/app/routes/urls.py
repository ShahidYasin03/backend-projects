from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.database import get_connection
from app.schemas import URLCreate, URLResponse, URLInfo
from app.utils import to_base62

router = APIRouter()


@router.post("/urls", response_model=URLResponse)
def create_url(data: URLCreate):
    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO urls (long_url)
                VALUES (%s)
                RETURNING id
                """,
                (str(data.long_url),)
            )

            url_id = cursor.fetchone()[0]

            short_code = to_base62(url_id)

            cursor.execute(
                """
                UPDATE urls
                SET short_code = %s
                WHERE id = %s
                """,
                (short_code, url_id)
            )

    return {
        "short_code": short_code,
        "long_url": str(data.long_url)
    }

@router.get("/urls/{short_code}", response_model=URLInfo)
def get_url_info(short_code: str):
    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT short_code, long_url, click_count, created_at
                FROM urls
                WHERE short_code = %s
                """,
                (short_code,)
            )

            result = cursor.fetchone()

            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail="Short URL not found"
                )

    return {
        "short_code": result[0],
        "long_url": result[1],
        "click_count": result[2],
        "created_at": result[3]
    }

@router.get("/{short_code}")
def redirect_url(short_code: str):
    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT long_url
                FROM urls
                WHERE short_code = %s
                """,
                (short_code,)
            )

            result = cursor.fetchone()

            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail="Short URL not found"
                )

            long_url = result[0]

            cursor.execute(
                """
                UPDATE urls
                SET click_count = click_count + 1
                WHERE short_code = %s
                """,
                (short_code,)
            )

    return RedirectResponse(url=long_url, status_code=307)