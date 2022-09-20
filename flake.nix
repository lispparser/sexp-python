{
  description = "Python S-Expression Parser";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        packages = rec {
          default = sexp-python;

          sexp-python = pkgs.python3Packages.buildPythonPackage {
            name = "sexp-python";
            src = nixpkgs.lib.cleanSource ./.;
          };
        };
      }
    );
}
