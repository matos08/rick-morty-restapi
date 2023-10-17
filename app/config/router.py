from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    from app.modules.core import health_check_router
    from app.modules.character import routers as character_router
    from app.modules.location import routers as location_router

    app.include_router(health_check_router.router)

    app.include_router(character_router.router)
    app.include_router(location_router.router)

    add_pagination(app)
