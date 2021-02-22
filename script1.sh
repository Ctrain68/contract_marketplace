#!/bin/bash

aws s3 cp s3://col-env-bucket/contract_app_env/.env /home/github-actions/contract_marketplace/.env


# gunicorn -b 0.0.0.0 -w 3 "src:create_app()"
