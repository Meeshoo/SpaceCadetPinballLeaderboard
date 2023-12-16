source "docker" "base_pinball" {
  image = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/base-pinball"
  commit = true
  ecr_login = true
  login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
  changes = [
    "ENV FOO bar",
    "ENTRYPOINT [\"nginx\", \"-g\", \"daemon off;\"]"
  ]
}

build {
  sources = ["source.docker.base_pinball"]

  provisioner "shell" {
    inline = ["mkdir /spacecadetpinballleaderboard"]
  }

  provisioner "file" {
    source = "../static"
    destination = "/spacecadetpinballleaderboard"
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/spacecadetpinballleaderboard-static"
      tags       = ["latest"]
    }

    post-processor "docker-push" {
      ecr_login = true
      login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
    }
  }
}
