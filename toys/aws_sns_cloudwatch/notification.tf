resource "aws_cloudwatch_event_rule" "watch-ec2" {
  name = "watch-ec2-state"

  event_pattern = <<EOF
{
  "detail-type": [
    "EC2 Instance State-change Notification"
  ]
}
EOF
}

resource "aws_cloudwatch_event_target" "sns" {
  rule      = aws_cloudwatch_event_rule.watch-ec2.name
  target_id = "SendToSNS"
  arn       = aws_sns_topic.my_topic.arn
}
