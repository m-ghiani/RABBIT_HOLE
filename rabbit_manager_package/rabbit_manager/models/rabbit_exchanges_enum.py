from enum import Enum


class RabbitExchangesEnum(Enum):
    UI_COMMANDS = "ui_commands_exchange"
    FRAME_PROCESSING = "frame_processing_exchange"
    VIDEO_READER = "videoreader_exchange"
    FRAME_READY = "frame_ready_exchange"