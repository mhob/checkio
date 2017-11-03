#!/usr/bin/env python3

def checkio(data):
    result = list()
    known_dupes = set()
    while len(data) > 0:
        consider = data.pop()
        if consider in known_dupes or consider in data:
            known_dupes.add(consider)
            result.append(consider)
    result.reverse()
    return result

if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio([1, 2, 3, 4, 5]) == []
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
