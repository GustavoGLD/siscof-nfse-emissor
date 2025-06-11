from io import StringIO

from loguru import logger


class LogBufferHandler:
    def __init__(self, **logger_add_params) -> None:
        self.log_id = int()
        self.log_buffer = None
        self.logger_add_params = logger_add_params

    def __enter__(self) -> StringIO:
        self.log_buffer = StringIO()
        self.log_id = logger.add(self.log_buffer.write, **self.logger_add_params)  # type: ignore

        return self.log_buffer

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.remove(self.log_id)
