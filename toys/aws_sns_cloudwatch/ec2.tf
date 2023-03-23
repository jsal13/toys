data "aws_ami" "linux_box" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm-2.0.20220805.0-x86_64-gp2"]
  }
}

resource "aws_instance" "test" {
  ami           = data.aws_ami.linux_box.id
  instance_type = "t2.micro"
}
