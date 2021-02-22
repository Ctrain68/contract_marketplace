#!/bin/bash

# aws s3 cp s3://col-env-bucket/contract_app_env/.env /code/.env

gunicorn -b 0.0.0.0:8000 -w 3 "src:create_app()"
