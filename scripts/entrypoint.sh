#!/bin/bash

APP_DIR="/app/employee"
APP_HOST="0.0.0.0"
APP_PORT=8000

echo Run application without reload option.;
exec uvicorn main:app --app-dir $APP_DIR \
                      --host  $APP_HOST \
                      --port $APP_PORT \
                      --header server:HIDDEN; # Security
