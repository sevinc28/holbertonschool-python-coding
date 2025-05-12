#!/usr/bin/python3
python3 -c "d = __import__('0-square').__doc__ ; r = 'OK\n' if d is not None and len(d.strip()) > 0 else '' ; print(r, end='')" | wc -l
