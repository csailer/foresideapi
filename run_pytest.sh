#!/usr/bin/env bash



export DJANGO_SECRET="l8^!*o3^f_z-&17%je2smeeiju@%tya*!kx9v_^ggwepums+4+"
export DEBUG=True
export VERSION=$(bumpversion --dry-run minor --allow-dirty --list | grep current_version | sed  s,"^.*=",,)

find . -name "__pycache__" -type d -exec rm -rf {} \;

py.test