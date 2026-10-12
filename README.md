# AWS Cloud Resume Challenge — Backend

A serverless visitor counter built with Python and AWS as part of my Cloud Resume Challenge.

**Live website:** https://marriohinkle.com

**Frontend repository:** https://github.com/Aruande/cloud-resume-frontend

**Technical Blog Post:** [From Cloud Computing Student to Cloud Builder: My AWS Cloud Resume Challenge Journey](https://dev.to/aruande/from-cloud-computing-student-to-cloud-builder-my-aws-cloud-resume-challenge-journey-7b9)

## Project Overview

This backend provides a visitor counter for my cloud-hosted resume website. It uses AWS Lambda to process HTTP requests, Amazon DynamoDB to store the visitor count, and Amazon API Gateway to expose the functionality through an API.

The project also includes automated Python testing, infrastructure as code with AWS SAM, and a GitHub Actions CI/CD pipeline.

## Architecture

```text
Resume Website
      |
      v
Amazon API Gateway
      |
      v
AWS Lambda (Python)
      |
      v
Amazon DynamoDB
```

The backend uses the following AWS services and tools:

| Technology | Purpose |
|---|---|
| AWS Lambda | Executes the Python visitor counter |
| Amazon API Gateway | Provides the HTTP API endpoint |
| Amazon DynamoDB | Stores and updates the visitor count |
| AWS SAM | Defines and packages serverless infrastructure |
| AWS CloudFormation | Deploys and manages the test backend stack |
| AWS IAM | Controls access between AWS services |
| GitHub Actions | Automates testing and deployment |
| GitHub OIDC | Authenticates GitHub Actions to AWS without long-lived access keys |
| pytest | Runs automated Python tests |

## API

**Method:** `POST`

**Route:** `/visitor-count`

The Lambda function updates the visitor count in DynamoDB and returns the updated count to the requesting client.

## Repository Structure

```text
cloud-resume-backend/
├── .github/
│   └── workflows/
│       ├── backend-tests.yml
│       └── deploy-backend.yml
├── src/
│   ├── lambda_function.py
│   └── requirements.txt
├── tests/
│   └── test_lambda_function.py
├── .gitignore
├── requirements-dev.txt
├── samconfig.toml
├── template.yaml
└── README.md
```

## Automated Testing

The project uses pytest to test the Python backend.

To run the tests locally:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

GitHub Actions automatically runs backend tests when changes are pushed to the `main` branch.

## Infrastructure as Code

The test backend is defined in `template.yaml` using AWS SAM.

The template includes:

- An AWS Lambda function running Python 3.14
- An HTTP API Gateway endpoint
- A DynamoDB table for visitor counts
- IAM permissions allowing the Lambda function to update the table

The test environment is deployed in AWS Region `us-east-2` using the CloudFormation stack `cloud-resume-backend-test`.

The production backend was configured separately and is not managed by this test stack.

## Continuous Integration and Deployment

The GitHub Actions deployment workflow automates the following process:

1. Checks out the repository.
2. Sets up Python 3.14.
3. Installs test dependencies.
4. Runs pytest.
5. Authenticates to AWS using GitHub OIDC and an IAM deployment role.
6. Installs AWS SAM.
7. Builds the serverless application.
8. Deploys the test backend through AWS CloudFormation.

Deployment permissions are separated between the GitHub Actions IAM role and a dedicated CloudFormation execution role.

The deployment targets the test environment rather than modifying the production visitor counter.

## Verification

The test API was successfully invoked and returned incrementing visitor counts.

GitHub Actions successfully completed both automated testing and AWS deployment on commit `40a804a`.

## What I Learned

This project provided practical experience with:

- Developing and testing Python AWS Lambda functions
- Integrating API Gateway, Lambda, and DynamoDB
- Defining serverless resources using infrastructure as code
- Configuring IAM roles and least-privilege deployment permissions
- Troubleshooting AWS authorization failures
- Implementing secure GitHub-to-AWS authentication with OIDC
- Building and validating a CI/CD pipeline
- Separating test infrastructure from production resources

## Future Improvements

Potential improvements include expanding automated API integration tests, adding monitoring and alerts, and managing the production backend through infrastructure as code.