from enum import Enum


class RabbitQueuesEnum(Enum):
    UI_COMMANDS = "ui_commands_queue"
    FRAME_PROCESSING = "frame_processing_queue"
    VIDEO_READER = "videoreader_queue"
    NDI = "ndi_queue"
    FRAME_READY = "frame_ready_queue"


