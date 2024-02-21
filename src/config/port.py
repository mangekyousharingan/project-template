from abc import ABC, abstractmethod
from typing import Any

from src.config.models import HttpServer


class AbstractConfig(ABC):
    @property
    @abstractmethod
    def http_server(self) -> HttpServer:
        raise NotImplemented
