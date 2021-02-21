#!/bin/bash

aws s3 cp s3://col-env-bucket/contract_app_env/.env /home/github-actions/contract_marketplace/.env

cd home/github-actions/contract_marketplace

flask run -h 0.0.0.0