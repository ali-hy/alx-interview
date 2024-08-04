#!/usr/bin/python3
""" Module that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
