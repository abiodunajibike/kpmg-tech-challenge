## Overview

This project contains modules to create a Three-Tier Architecture in AWS with [Terraform](https://www.terraform.io/docs/providers/aws/index.html).

A three-tier architecture is a software architecture pattern where the infrastructure is divided into three logical tiers: the presentation layer (frontend in public subnets), the business logic layer (backend in private subnets) and the data storage layer (database in private subnets).

I have chosen to use the [AWS VPC Terraform module](https://github.com/terraform-aws-modules/terraform-aws-vpc) to reduce the amount of boilerplate code required to achieve a Three-Tier Architecture in AWS.

### Requirements
- Download the proper [Terraform](https://www.terraform.io/downloads.html) package for your operating system and architecture.
- Set up a named [AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) with the name `development`:
    - Create an AWS IAM user with appropriate permissions to provision `VPC` resources and copy the access keys.
    - Install `awscli` by following this [guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), if not already installed
    -  Execute `aws configure --profile development` to create a named AWS IAM profile

### Usage
- Initialize terraform inside this folder with:
    - `terraform init`
- Validate the terraform configuration with:
    - `terraform validate`
- Check to confirm that terraform is going to create the appropriate resources with:
    - `terraform plan`
- After you have verified the plan generated above by terraform, apply the plan to create the resources with:
    - `terraform apply`

- These AWS VPC resources should be created if the IAM user/role has the appropriate permissions:
    ```
    1 VPC
    3 Public Subnets (1 in each availability zone in eu-west-1)
    6 Private Subnets (2 in each availability zone in eu-west-1)
    4 Route Tables (1 for the Public Subnets and 3 for the Private Subnets)
    1 Internet gateway for the VPC
    3 Elastic IPs for the NAT Gateways
    3 NAT Gateways for the private subnets (deployed in the public subnets for internet connectivity)
    ```
