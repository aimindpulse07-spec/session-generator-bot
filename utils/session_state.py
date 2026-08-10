import asyncio
from dataclasses import dataclass
from time import monotonic
from typing import Optional


@dataclass
class UserSessionState:
    library: Optional[str] = None
    method: Optional[str] = None
    created_at: float = 0.0


class SessionStateManager:
    def __init__(self, timeout: int = 600) -> None:
        self._states: dict[int, UserSessionState] = {}
        self._lock = asyncio.Lock()
        self._timeout = timeout

    async def create(
        self,
        user_id: int,
        library: str,
    ) -> UserSessionState:
        async with self._lock:
            state = UserSessionState(
                library=library,
                created_at=monotonic(),
            )

            self._states[user_id] = state
            return state

    async def get(
        self,
        user_id: int,
    ) -> Optional[UserSessionState]:
        async with self._lock:
            state = self._states.get(user_id)

            if state is None:
                return None

            if monotonic() - state.created_at > self._timeout:
                self._states.pop(user_id, None)
                return None

            return state

    async def delete(self, user_id: int) -> None:
        async with self._lock:
            self._states.pop(user_id, None)

    async def clear_all(self) -> None:
        async with self._lock:
            self._states.clear()


session_states = SessionStateManager()
