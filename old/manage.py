#!/usr/bin/env python
import os
import sys

vendor_libs_path = os.path.join(os.getcwd(), 'lib')
if os.path.exists(vendor_libs_path):
    sys.path.insert(0, vendor_libs_path)

import dotenv

dotenv.read_dotenv()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homepage.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
