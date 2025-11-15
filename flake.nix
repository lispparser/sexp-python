{
  description = "Python S-Expression Parser";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python311Packages;
      in {
        packages = rec {
          default = sexp-python;

          sexp-python = pythonPackages.buildPythonPackage {
            name = "sexp-python";
            src = nixpkgs.lib.cleanSource ./.;
            pyproject = true;
            build-system = [ pythonPackages.setuptools ];
          };
        };
      }
    );
}
