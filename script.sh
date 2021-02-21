#!/bin/bash

aws s3 cp s3://col-env-bucket/contract_app_env/.env /code/.env

flask run -h 0.0.0.0
