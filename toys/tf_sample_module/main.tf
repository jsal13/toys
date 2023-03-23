# Makes an S3 bucket with a unique name.
provider "aws" {
    region = "us-east-1"
}

module "cool_s3_bucket" {
  source = "./sample-module"

  bucket_name = "jsal-test-123451234512345"
  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
