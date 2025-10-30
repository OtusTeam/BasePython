from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Awaitable

from fastapi import Request, Response


type CallNext = Callable[[Request], Awaitable[Response]]


@dataclass
class PathCounts:
    count: int = 0
    statuses_counts: defaultdict[int, int] = field(
        default_factory=lambda: defaultdict(int)
    )


class RequestsCountMiddlewareDispatch:
    def __init__(self):
        self.counts = defaultdict[str, PathCounts](PathCounts)

    async def __call__(
        self,
        request: Request,
        call_next: CallNext,
    ) -> Response:
        path = request.url.path
        self.counts[path].count += 1
        try:
            response = await call_next(request)
        except Exception:
            self.counts[path].statuses_counts[999] += 1
            raise
        self.counts[path].statuses_counts[response.status_code] += 1
        return response


requests_count_middleware_dispatch = RequestsCountMiddlewareDispatch()
