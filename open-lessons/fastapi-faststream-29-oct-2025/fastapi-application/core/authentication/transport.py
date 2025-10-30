from fastapi_users.authentication import (
    BearerTransport,
    CookieTransport,
)

from core.config import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.api.bearer_token_url,
)
cookie_transport = CookieTransport(
    # TODO: move to settings
    cookie_max_age=3600,
    cookie_secure=False,
)
