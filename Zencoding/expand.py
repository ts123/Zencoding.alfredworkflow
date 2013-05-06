#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import zencoding

def main(query):
    if not query:
        query = get_selected_text()
        if not query:
            sys.exit(1)
    sys.stdout.write(zencoding.expand_abbreviation(query))

def get_selected_text():
    import subprocess
    clear_cb = 'tell application "System Events" to set the clipboard to ""'
    copy_to_cb = 'tell application "System Events" to keystroke "c" using {command down}'
    subprocess.Popen(['osascript', '-e', clear_cb, '-e', copy_to_cb]).wait()
    return subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE).communicate()[0]

if __name__ == '__main__':
    main(' '.join(sys.argv[1:]))

