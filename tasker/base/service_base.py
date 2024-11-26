import abc
from typing import Any, Tuple


class ServiceBase(abc.ABC):
    def perform(self):
        return self._perform()

    @abc.abstractmethod
    def _perform(self) -> Tuple[bool, str, Any]:
        pass
