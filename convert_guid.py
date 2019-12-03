#! /usr/bin/python3

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='GUID to MSI compressed GUID converter')
    parser.add_argument('GUID')
    args = parser.parse_args()
    
    guid1 = args.GUID

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

