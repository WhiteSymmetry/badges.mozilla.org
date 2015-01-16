#!/usr/bin/env python
import os
import sys

sys.path.append("/virtualenv/lib/python2.6/site-packages")

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'badgus.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
