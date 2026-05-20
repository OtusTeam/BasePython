import asyncio
from collections import defaultdict

from fastapi.sse import ServerSentEvent

type ChannelID = str

type EventQueue = asyncio.Queue[ServerSentEvent]


class PubSub:
    def __init__(self) -> None:
        self._subscribers = defaultdict[ChannelID, set[EventQueue]](set)

    async def subscribe(self, channel: ChannelID) -> EventQueue:
        queue: EventQueue = asyncio.Queue()
        self._subscribers[channel].add(queue)
        return queue

    def unsubscribe(
        self,
        channel: ChannelID,
        queue: EventQueue,
    ) -> None:
        self._subscribers[channel].discard(queue)

    async def publish(
        self,
        channel: ChannelID,
        message: ServerSentEvent,
    ) -> None:
        for queue in list(self._subscribers[channel]):
            await queue.put(message)
