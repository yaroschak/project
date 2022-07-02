provider "aws" {
#  ключі від створеного користувача
#  access_key = "xxxx"
#  secret_key = "xxxx"
  region = "us-east-1"
}


resource "aws_instance" "app_server" {
  ami                    = "ami-0729e439b6769d6ab"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.ssh_http_https.id]
  user_data              = file("init.sh")


  tags = {
    Name = "AppServerInstance"
  }
}

resource "aws_security_group" "ssh_http_https" {

  ingress {
    from_port   = 8081
    protocol    = "tcp"
    to_port     = 8081
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    protocol    = "tcp"
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

}
