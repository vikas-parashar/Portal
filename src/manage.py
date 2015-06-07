#!/usr/bin/env python
import os
import sys
#THIRD PARTY IMPORTS
import dotenv
dotenv.read_dotenv()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studyportal.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
