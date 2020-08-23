from enum import Enum

class NodeType(Enum):
    """
    Represents possible type of a Node and its color.
    """
    WALL = (0x00, 0x34, 0x59)
    START = (0x00, 0xc0, 0x41)
    END = (0xff, 0x28, 0x00)
    PATH = (0xff, 0xb4, 0x00)
    EMPTY = (0xf4, 0xf4, 0xf4)
    VISITED = (0x00, 0xa8, 0xe8)