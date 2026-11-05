
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger():
    """初始化项目日志配置。"""

    logger = logging.getLogger("ecommerce_autotest")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # 防止重复添加 Handler
    if logger.handlers:
        return logger

    # 项目根目录下创建 logs 文件夹
    log_dir = Path(__file__).resolve().parents[1] / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 文件日志：最大 5MB，保留 3 个备份
    file_handler = RotatingFileHandler(
        log_dir / "autotest.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_logger(name=None):
    """获取项目 Logger，可指定模块名称。"""

    setup_logger()

    if name:
        return logging.getLogger(f"ecommerce_autotest.{name}")

    return logging.getLogger("ecommerce_autotest")
