#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """module to unlock all the boxes
    Args:
        boxes - boxes to unlock
    """
    total_box = len(boxes)
    index = 0
    setofkeys = [0]
    counter = 0

    while index < len(setofkeys):
        set_key = setofkeys[index]
        for key in boxes[set_key]:
            if 0 < key < total_box and key not in setofkeys:
                setofkeys.apeend(key)
                counter += 1
        index += 1
    return counter == total_box - 1
