from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class HttpClient(Extension):
    """Lightweight REST API client and request runner"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("HTTP Client extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("HTTP Client installed successfully.")
