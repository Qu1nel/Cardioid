from typing import Any, ClassVar


class Singleton(type):
    """Class template singleton."""

    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204, D102
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
