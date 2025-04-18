#!/usr/bin/env python
import os
import sys
from decouple import config

if __name__ == "__main__":
    # ✅ Default Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory_management.settings")

    # ✅ Optional: Set environment variables if using config from .env
    # You don’t need to do anything here unless you want to log or extend behavior

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH?"
        ) from exc

    execute_from_command_line(sys.argv)
