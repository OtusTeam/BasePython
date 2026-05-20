import asyncio
import signal
from collections.abc import Callable


class ShutdownCoordinator:
    def __init__(self) -> None:
        self._event = asyncio.Event()
        self._handlers_installed = False

    @property
    def event(self) -> asyncio.Event:
        return self._event

    @property
    def is_shutting_down(self) -> bool:
        return self._event.is_set()

    def request_shutdown(self) -> None:
        self._event.set()

    def install_shutdown_handlers(self) -> None:
        if self._handlers_installed:
            return

        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                previous = signal.getsignal(sig)

                def handler(
                    *,
                    _sig: signal.Signals = sig,
                    _previous: Callable[..., object] | int | None = previous,
                    _coordinator: ShutdownCoordinator = self,
                ) -> None:
                    _coordinator.request_shutdown()
                    if not callable(_previous):
                        return
                    try:
                        _previous()
                    except TypeError:
                        _previous(_sig, None)  # type: ignore[misc]

                loop.add_signal_handler(sig, handler)
            except NotImplementedError, RuntimeError, ValueError:
                pass

        self._handlers_installed = True


shutdown = ShutdownCoordinator()
