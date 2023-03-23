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
  region = "us-west-2"
}

resource "aws_kms_key" "tmp_kms_key_for_de_toys" {
  description             = "Temporary KMS Key for DE Toys"
  deletion_window_in_days = 7
}

output "arn_for_kms_key" {
  value = aws_kms_key.tmp_kms_key_for_de_toys.arn
}
