'''
This code has copied from https://qiita.com/Esfahan/items/275b0f124369ccf8cf18
'''

# -*- coding:utf-8 -*-
import queue
from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG, Handler, INFO
import logging
import datetime as dt

now = dt.datetime.now()
time = now.strftime('%Y%m%d-%H%M%S')

mapping = {
    "TRACE": " trace ]",
    "DEBUG": " \x1b[0;36mdebug\x1b[0m ",
    "INFO": "  \x1b[0;32minfo\x1b[0m ",
    "WARNING": "  \x1b[0;33mwarn\x1b[0m ",
    "WARN": "  \x1b0;33mwarn\x1b[0m ",
    "ERROR": "\x1b[0;31m error \x1b[0m",
    "ALERT": "\x1b[0;37;41m alert \x1b[0m",
    "CRITICAL": "\x1b[0;37;41m alert \x1b[0m",
}


class ColorfulHandler(logging.StreamHandler):
    def emit(self, record: logging.LogRecord) -> None:
        record.levelname = mapping[record.levelname]
        super().emit(record)


class QueueHandler(Handler):
    def __init__(self, log_que):
        super().__init__()
        self.log_queue = log_que

    def emit(self, record):
        self.log_queue.put(record)


def root_logger():
    # logging.basicConfig(handlers=[ColorfulHandler()], level=logging.DEBUG)
    # root loggerを取得

    logger = getLogger()
    log_queue = queue.Queue()

    # formatterを作成
    formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')

    # handlerを作成しフォーマッターを設定
    # handler = ColorfulHandler()
    handler = StreamHandler()
    handler.setFormatter(formatter)

    # ファイルハンドラを作成
    rh = logging.FileHandler(
        r'./log/log_' + time + '.log',
        encoding='utf-8',
    )

    rh.setFormatter(formatter)
    qh = QueueHandler(log_queue)
    qh.setFormatter(formatter)

    # loggerにhandlerを設定、イベント捕捉のためのレベルを設定
    logger.addHandler(handler)
    logger.addHandler(rh)
    logger.addHandler(qh)
    # log levelを設定
    logger.setLevel(DEBUG)
    qh.setLevel(INFO)
    # logger.debug("hello")
    # logger.info("hello")
    # logger.warning("hello")
    # logger.error("hello")
    # logger.critical("hello")

    return logger, log_queue
