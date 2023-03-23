resource "aws_sns_topic" "my_topic" {
  name = "my_topic"
}

resource "aws_sns_topic_subscription" "my_topic_subscription" {
  topic_arn = aws_sns_topic.my_topic.arn
  protocol  = "email"
  endpoint  = "james.c.salvatore.services@gmail.com"
}
