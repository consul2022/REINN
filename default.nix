{ lib
, python
, poetry2nix
}:

poetry2nix.mkPoetryApplication {
  inherit python;

  projectDir = ./.;
  pyproject = ./pyproject.toml;
  poetrylock = ./poetry.lock;

  pythonImportsCheck = [ "reinn" ];

  meta = with lib; {
    homepage = "https://github.com/consul2022/REINN";
    description = "This project was generated with fastapi-mvc.";
  };
}
