#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import alfred
import zencoding

def main(query):
    query = query.decode('utf-8')
    if query:
        title = zencoding.expand_abbreviation(query).replace('\n', '\\n')
    else:
        title = 'Expand selected text'
    alfred.write(alfred.xml([alfred.Item(
        attributes = { 'uid': 1, 'arg': query },
        title = title,
        subtitle = 'Paste html',
        icon = 'icon.png')
        ]))

if __name__ == '__main__':
    main(' '.join(sys.argv[1:]))

