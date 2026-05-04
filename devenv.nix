{ pkgs, lib, config, inputs, ... }:

{
  packages = [
    pkgs.git
    pkgs.harper
    pkgs.iwe
    pkgs.panache
    pkgs.quarto
    pkgs.rumdl
  ];

  languages.python = {
    enable = true;
    package = pkgs.python314;
    lsp.enable = false; # Devenv's LSP setup system doesn't meet my requirements.
    venv.enable = true;
    venv.requirements = ''
      jupyter==1.1.1
    '';
  };

  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
    harper-ls --version | grep --color=auto "${pkgs.harper.version}"
    iwe --version | grep --color=auto "${pkgs.iwe.version}"
    panache --version | grep --color=auto "${pkgs.panache.version}"
    quarto --version | grep --color=auto "${pkgs.quarto.version}"
    rumdl --version | grep --color=auto "${pkgs.rumdl.version}"
  '';
}
