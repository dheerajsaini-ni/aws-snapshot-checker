# aws-snapshot-checker
Project to manage AWS EC2 Instance snapshots

## About

This project is a sample, uses pipenv and boto3 to manage EC2 instances

## Configuring

It uses the AWS profile configured using 

`aws configure --profile <aws_profile>`

## Running

This project requires Python 3. Install pipenv
```
pip3 install pipenv
```

Then run the project
```
pipenv install
pipenv run python aws/ec2-manager.py <command> <--project=PROJECT>
```

*Command* is list, start or stop