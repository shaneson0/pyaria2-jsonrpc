#! /usr/bin/env python

"""Notify that aria2 download is complete.

This implements the --on-download-complete hook interface.
"""

import sys

# ['/Users/csx/GitProject/snowmusic/pyaria2-jsonrpc/hook.py', 'e3f97be6d4490a5a', '1', './temp/aa.mp3']
Argv = sys.argv

def Hook(Argv):
    print Argv
