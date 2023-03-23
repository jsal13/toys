output "website_bucket_arn" {
  description = "ARN of the bucket"
  value       = module.cool_s3_bucket.arn
}

output "website_bucket_name" {
  description = "Name (id) of the bucket"
  value       = module.cool_s3_bucket.name
}
