#
# Provider Configuration
#

provider "aws" {
  region  = "eu-west-1"
  profile = "development"
  version = ">= 2.57"
}