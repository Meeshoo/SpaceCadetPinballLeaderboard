source "docker" "python" {
  image = "python"
  commit = true
  changes = [
    "ENV FOO bar",
    "WORKDIR /spacecadetpinballleaderboard",
    "CMD [\"SpaceCadetPinballLeaderboard.wsgi:application\", \"--bind\", \"0.0.0.0:80\"]",
    "ENTRYPOINT [\"gunicorn\"]"
  ]
}

build {
  sources = ["source.docker.python"]

  provisioner "shell" {
    inline = ["mkdir /spacecadetpinballleaderboard"]
  }

  provisioner "file" {
    source = "../"
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
      login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
    }
  }
}
