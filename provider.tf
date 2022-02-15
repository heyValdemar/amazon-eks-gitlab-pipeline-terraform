provider "aws" {
  version = "~> 2.57.0"
}

provider "random" {
  version = "~> 2.2.1"
}

data "aws_caller_identity" "current" {} # Accesing Account ID and ARN
