variables {
  access_key="${env("AWS_ACCESS_KEY_ID")}"
  secret_key="${env("AWS_SECRET_ACCESS_KEY")}"
}

source "docker" "python" {
  image = "python"
  commit = true
  changes = [
    "ENV FOO bar",
    "WORKDIR /spacecadetpinballleaderboard",
    "CMD [\"gunicorn\", \"/spacecadetpinballleaderboard/SpaceCadetPinballLeaderboard/wsgy.py\", \"--bind\", \"0.0.0.0:80\"]"
  ]
}

build {
  sources = ["source.docker.python"]

  provisioner "shell" {
    inline = ["mkdir /spacecadetpinballleaderboard"]
  }

  provisioner "file" {
    source = "./"
    destination = "/spacecadetpinballleaderboard"
  }

  provisioner "shell" {
    inline = ["pip install -r /spacecadetpinballleaderboard/requirements.txt"]
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/spacecadetpinballleaderboard-python"
      tags       = ["latest"]
    }

    post-processor "docker-push" {
      ecr_login = true
      aws_access_key = var.access_key
      aws_secret_key = var.secret_key
      login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
    }
  }
}
