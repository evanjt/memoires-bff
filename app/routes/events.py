from typing import Any
from fastapi import Depends, APIRouter, Response, Body, Request
from app.config import config
from app.utils import get_async_client
import httpx
from uuid import UUID
from app.models.user import User

router = APIRouter()


@router.get("/{event_id}")
async def get_event(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    event_id: UUID,
) -> Any:
    """Get an event by id"""

    res = await client.get(
        f"{config.MEMOIRES_API_URL}/v1/events/{event_id}",
    )

    return res.json()


@router.get("")
async def get_events(
    request: Request,
    response: Response,
    *,
    filter: str = None,
    sort: str = None,
    range: str = None,
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all events"""
    res = await client.get(
        f"{config.MEMOIRES_API_URL}/v1/events",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_event(
    event: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Creates an event"""

    res = await client.post(
        f"{config.MEMOIRES_API_URL}/v1/events",
        json=event,
    )

    return res.json()


@router.put("/{event_id}")
async def update_event(
    event_id: UUID,
    event: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """ "Updates an event by id"""

    res = await client.put(
        f"{config.MEMOIRES_API_URL}/v1/events/{event_id}", json=event
    )

    return res.json()


@router.delete("/{event_id}")
async def delete_event(
    event_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
) -> None:
    """Delete an event by id"""

    res = await client.delete(f"{config.MEMOIRES_API_URL}/v1/events/{event_id}")

    return res.json()
