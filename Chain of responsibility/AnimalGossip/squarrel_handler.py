from typing import Any
from parent import AbstractHandler


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

