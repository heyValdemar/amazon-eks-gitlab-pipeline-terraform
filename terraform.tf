terraform {
  required_version = "~> 0.12.24" # Which means ">= 0.12.24" and "< 0.13"
  backend "s3" {}
}
