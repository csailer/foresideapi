#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

# This is an extension point so the extra environment points can be added in later
# development iterations, e.g. Local, Test, QA, Prod etc.
# Currently, on LOCAL is valid and it must be set. This environment variable tells
# the app which Django Settings Module to Load.
ENV = os.environ.get('ENV', None)

config_settings = ""
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.info("Entering manage.py main()")

    if len(sys.argv) > 1:
        if ENV and ENV.upper() == 'LOCAL':
            print("Manage.py - config.local is set.")
            print("LOCAL")
            config_settings = "config.local"
        else:
            print("")
    else:
        if ENV and ENV.upper() == 'LOCAL':
            print("Manage.py - config.local is set.")
            print("DEBUG")
            config_settings = "config.local"
        else:
            print("Env Variable not set indicating the Env to run the API. e.g. Local, QA, Prod.")

    print("Manage.py - Setting DJANGO_SETTINGS_MODULE env variable to {0}.".format(config_settings))
    logger.info("Manage.py - Setting DJANGO_SETTINGS_MODULE env variable to {0}.".format(config_settings))
    if config_settings is None or len(config_settings) == 0:
        raise SystemError("ENV env variable is not set.")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config_settings)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(str(exc))
        logging.error("Manage.py - {0}.".format(str(exc)))
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(str(e))
        logging.error("Manage.py - {0}".format(str(e)))
        raise Exception("Failed to run execute: execute_from_command.")
