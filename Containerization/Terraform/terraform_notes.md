# What is Terraform?
- Terraform is a Infrastructure as Code (IaC) tool that allows you to manage/configure/biuld/change your infrastructure with ease. You start with defining you resource configuration and pushing your Terraform file a supported vendor (AWS / Azure/ etc).

# Quick Getting Started:
- Terraform instalation (Make sure Terraform is in your PATH)
    - https://developer.hashicorp.com/terraform/install
- Validate the installation:
    - ```terraform -help```
- Connect your AWS account (You will need the AWS CLI installed):
    - Export your Access and Secret keys 
        - ```export AWS_ACCESS_KEY_ID```
        - ```export AWS_SECRET_KEY_ID```
    - Create a test directory then navigate to the test directory:
        - ```mkdir test-terraform-aws-instance```
        - ```cd test-terraform-aws-instance```
    - Create a configuration file:
        - ```touch main.tf```
    - Content of configuration file:
        ```s
        terraform {
        required_providers {
            aws = {
            source  = "hashicorp/aws"
            version = "~> 4.16"
            }
        }

        required_version = ">= 1.2.0"
        }

        provider "aws" {
        region  = "us-west-2"
        }

        resource "aws_instance" "app_server" {
        ami           = "ami-RANDOMIMAGE"
        instance_type = "t2.micro"

        tags = {
            Name = "ExampleAppServerInstance"
        }
        }

        ```
    - After any new configurations you need to initalize the file:
        - ```terraform init```
    - When your ready to create your infrastructure:
        - ```terraform apply```
        - Terraform will output its execution plan before applying the configuration.
    - Terraform will create a ".tfstate" file which stores ID's, properties, configs, etc. Terraform will reference this file when making update or dstroy decisions. To inpect this file:
        - ```terraform show```
    - When you make files changes, Terraform will flag those changes in the "apply" command is issued: 
    - The following prefix means delete then recreate: ```-/+```

# Commands
Initalize your directory:
```terraform init```<br>
Apply you configuration changes:
```terraform apply``` <br>
Show current state of your configuration:
```terraform show```<br>


### Terraform Training:
- https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code
- https://spacelift.io/blog/terraform-commands-cheat-sheet