#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'Supreme Court to Rule on Release of Trump’s Financial Records - The New York Times'
    print(translate(to_translate))
    print(translate(to_translate, 'ml'))
    print(translate(to_translate, 'ru'))

if __name__ == '__main__':
    main()
