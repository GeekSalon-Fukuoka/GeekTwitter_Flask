#!/bin/sh

python -c "from app import db; db.create_all()"