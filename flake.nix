{
  description = "Python S-Expression Parser";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree rec {
          sexp-python = pkgs.python3Packages.buildPythonPackage {
            name = "sexp-python";
            src = nixpkgs.lib.cleanSource ./.;
            nativeBuildInputs = [
            ];
            propagatedBuildInputs = [
            ];
          };
        };
        defaultPackage = packages.sexp-python;
      });
}
