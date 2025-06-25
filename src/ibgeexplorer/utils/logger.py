import logging
from datetime import datetime
from pathlib import Path

# ROOT = Path(__file__).parent.parent.parent


class StepFilter(logging.Filter):
    def __init__(self, step):
        super().__init__()
        self.step = step

    def filter(self, record):
        record.step = f"{self.step} - " if self.step else ""
        return True


class LogWriter:
    def __init__(self, step: str = None, log_dir: str = "logs"):
        log_filename = f"log_{datetime.now().strftime('%Y-%m-%d')}.log"
        self.log_file = Path(log_dir) / log_filename
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        logger_name = f"{__name__}.{step}" if step else __name__
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        self.logger.propagate = False
        self.logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(step)s%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.addFilter(StepFilter(step))
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.addFilter(StepFilter(step))
        self.logger.addHandler(console_handler)

    def debug(self, msg: str):
        """Registra uma mensagem com nível DEBUG."""
        self.logger.debug(msg)

    def info(self, msg: str):
        """Registra uma mensagem com nível INFO."""
        self.logger.info(msg)

    def warning(self, msg: str):
        """Registra uma mensagem com nível WARNING."""
        self.logger.warning(msg)

    def error(self, msg: str):
        """Registra uma mensagem com nível ERROR."""
        self.logger.error(msg)

    def critical(self, msg: str):
        """Registra uma mensagem com nível CRITICAL."""
        self.logger.critical(msg)


if __name__ == "__main__":
    log = LogWriter("DEBUG")
    log.info("Mensagem de informação.")
    log.warning("Aviso.")
    log.error("Erro.")
    log.debug("Debug.")
