from typing import Any
from fastapi import Depends, APIRouter, Query, Response, Body
from app.config import config
from app.utils import get_async_client
import httpx
from uuid import UUID
from app.models.user import User


router = APIRouter()


@router.get("/{station_id}")
async def get_station(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    station_id: UUID,
) -> Any:
    """Get a station by id"""

    res = await client.get(
        f"{config.MEMOIRES_API_URL}/v1/stations/{station_id}",
    )

    return res.json()


@router.get("")
async def get_stations(
    response: Response,
    *,
    filter: str = Query(None),
    sort: str = Query(None),
    range: str = Query(None),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all stations"""

    res = await client.get(
        f"{config.MEMOIRES_API_URL}/v1/stations",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_station(
    station: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Creates a station"""

    res = await client.post(
        f"{config.MEMOIRES_API_URL}/v1/stations",
        json=station,
    )

    return res.json()


@router.put("/{station_id}")
async def update_station(
    station_id: UUID,
    station: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Updates a station by id"""

    res = await client.put(
        f"{config.MEMOIRES_API_URL}/v1/stations/{station_id}", json=station
    )

    return res.json()


@router.delete("/{station_id}")
async def delete_station(
    station_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
) -> None:
    """Delete a station by id"""

    res = await client.delete(f"{config.MEMOIRES_API_URL}/v1/stations/{station_id}")

    return res.json()
