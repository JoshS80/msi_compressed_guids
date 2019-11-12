#! /usr/bin/python3

import sys
import os

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: convert_guid {GUID}")
        return -1
    
    guid1 = sys.argv[1]

    if len(guid1) != 38:
        print("Invalid GUID: '{}'".format(guid1))
        return -1

    print("GUID to convert: '{}'".format(guid1))

    guid_stripped = guid1.strip('{}')

    components = guid_stripped.split('-')
    print("Component parts: {}".format(components))

    if len(components) != 5:
        print("Invalid GUID")
        return -1

    final_guid = ""

    for i, c in enumerate(components):
        _c = ""

        if i >= 3:
            groups = int(len(c) / 2)
            for j in range(groups):
                _t = c[j * 2:(j * 2) + 2]
                _t = _t[::-1]
                _c = _c + _t
        else:
            # Reverse the characters
            _c = c[::-1]
        
        final_guid = final_guid + _c

    print("Compressed GUID: {}".format(final_guid))


if __name__ == "__main__":
    exit(main())

