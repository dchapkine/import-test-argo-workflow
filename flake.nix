{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.11";
    flake-parts = { url = "github:hercules-ci/flake-parts"; inputs.nixpkgs-lib.follows = "nixpkgs"; };
    devenv.url = "github:cachix/devenv";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs = inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
      imports = [ inputs.treefmt-nix.flakeModule ];
      perSystem = { pkgs, lib, config, ... }:
        let
          argoConfig = import ./conf.nix;
          myyarn = pkgs.yarn.override { nodejs = pkgs.nodejs-16_x-openssl_1_1; };
          src = 
            builtins.filterSource
              (path: type: !(type == "directory" && baseNameOf path == "hack"))
              (lib.sourceFilesBySuffices inputs.self [ ".go" ".mod" ".sum" ]);
          package = {
            name = "controller";
            version = argoConfig.version;
          };

          nodejs = pkgs.nodejs-16_x-openssl_1_1;
          nodeEnv = import ./node-env.nix {
            inherit (pkgs) stdenv lib python2 runCommand writeTextFile writeShellScript;
            inherit pkgs nodejs;
            libtool = if pkgs.stdenv.isDarwin then pkgs.darwin.cctools else null;
          };

          nodePackages = import ./node-packages.nix {
            inherit (pkgs) fetchurl nix-gitignore stdenv lib fetchgit;
            inherit nodeEnv;
          };
          pythonPkgs = pkgs.python310Packages;
          mkdocs = with pythonPkgs;
            buildPythonPackage rec {
              pname = "mkdocs";
              version = "1.2.4";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-jnlwomGDSH/ioQQZQMb9A6oNvlVJ5Qw+cZT1Zcs8Z4o=";
              };
              propagatedBuildInputs = [
                mergedeep
                markdown
                click
                pyyaml
                pyyaml-env-tag
                jinja2
                watchdog
                importlib-metadata
                typing-extensions
                packaging
                colorama
                ghp-import
              ];
              doCheck = false;
            };
          mkdocs-material-extensions = with pythonPkgs;
            buildPythonPackage rec {
              pname = "mkdocs_material_extensions";
              version = "1.1.1";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-nAA9px4swkk9kQI3RIxnLgDO/IANPWrpPS/GmXnjvZM=";
              };
              buildInputs = [ hatchling babel ];
              format = "pyproject";
            };
          mkdocs-material = with pythonPkgs;
            buildPythonPackage rec {
              pname = "mkdocs-material";
              version = "8.1.9";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-oVhzpeEWv0YVr0/O3IWgU3SSRkNlKGy6UDENlvsGaVg=";
              };
              propagatedBuildInputs = [
                mkdocs-material-extensions
                pygments
                markdown
                mkdocs
                pymdown-extensions
                jinja2
                colorama
                regex
                requests
              ];
              doCheck = false;
            };
          editdistpy = with pythonPkgs;
            buildPythonPackage rec {
              pname = "editdistpy";
              version = "0.1.3";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-s8rQcxnXn+izumv5IpPelikykX2I6cYk33tqRL3fHcw=";
              };
            };
          symspellpy = with pythonPkgs;
            buildPythonPackage rec {
              pname = "symspellpy";
              version = "6.7.7";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-9sMVGHeAvC3TD8nKMu8Hb4m7/LKns/mjd5JvH2reAIU=";
              };
              buildInputs = [ setuptools ];
              propagatedBuildInputs = [ editdistpy ];
              format = "pyproject";
            };
          mkdocs-spellcheck = with pythonPkgs;
            buildPythonPackage rec {
              pname = "mkdocs-spellcheck";
              version = "0.2.1";
              src = fetchPypi {
                inherit pname version;
                hash = "sha256-g8neboAWGGN04EWsSBKj4oHyKVN/iKP4wANO+Ba3nI4=";
              };
              format = "pyproject";
              buildInputs = [
                pdm-pep517
              ];
              propagatedBuildInputs = [
                symspellpy
              ];
            };
          pythonEnv = pkgs.python310.withPackages (ps: [
            ps.pytest
            ps.typing-extensions
            ps.mypy
            ps.autopep8
            ps.pip
            mkdocs
            mkdocs-material-extensions
            mkdocs-material
            mkdocs-spellcheck
          ]);

          mkEnvSerialize = (envKey: envValue: "export ${envKey}=${envValue};");
          mkEnv = (envAttrs:
            lib.concatStrings
              (lib.mapAttrsToList
                mkEnvSerialize
                envAttrs)
          );
          mkExec = (execName: envAttrs: execArgs:
            "${mkEnv envAttrs}${execName} ${execArgs}"
          );
          controllerCmd = mkExec "workflow-controller" argoConfig.controller.env argoConfig.controller.args;
          argoServerCmd = mkExec "argo" argoConfig.argoServer.env argoConfig.argoServer.args;
          uiCmd = mkExec "yarn" argoConfig.ui.env argoConfig.ui.args;
        in
        {
          packages = {
            ${package.name} = pkgs.buildGoModule {
              pname = package.name;
              inherit (package) version;
              inherit src;
              vendorSha256 = "sha256-1ivPt7m65B89jOTlYA21AcrW6OZeMlgpoPZd9Lw2Ohc=";
              doCheck = false;
            };

            mockery = pkgs.buildGoModule rec {
              pname = "mockery";
              version = "2.10.0";

              src = pkgs.fetchFromGitHub {
                owner = "vektra";
                repo = "mockery";
                rev = "v${version}";
                sha256 = "sha256-udzBhCkESd/5GEJf9oVz0nAQDmsk4tenvDP6tbkBIao=";
              };
              doCheck = false;
              vendorHash = "sha256-iuQx2znOh/zsglnJma7Y4YccVArSFul/IOaNh449SpA=";
            };

            protoc-gen-gogo-all = pkgs.buildGoModule rec {
              pname = "protoc-gen-gogo";
              version = "1.3.2";

              src = pkgs.fetchFromGitHub {
                owner = "gogo";
                repo = "protobuf";
                rev = "v${version}";
                sha256 = "sha256-CoUqgLFnLNCS9OxKFS7XwjE17SlH6iL1Kgv+0uEK2zU=";
              };
              doCheck = false;
              vendorHash = "sha256-nOL2Ulo9VlOHAqJgZuHl7fGjz/WFAaWPdemplbQWcak=";
            };
            grpc-ecosystem = pkgs.buildGoModule rec {
              pname = "grpc-ecosystem";
              version = "1.16.0";

              src = pkgs.fetchFromGitHub {
                owner = "grpc-ecosystem";
                repo = "grpc-gateway";
                rev = "v${version}";
                sha256 = "sha256-jJWqkMEBAJq50KaXccVpmgx/hwTdKgTtNkz8/xYO+Dc=";
              };
              doCheck = false;
              vendorHash = "sha256-jVOb2uHjPley+K41pV+iMPNx67jtb75Rb/ENhw+ZMoM=";
            };

            go-swagger = pkgs.buildGoModule rec {
              pname = "go-swagger";
              version = "0.28.0";

              src = pkgs.fetchFromGitHub {
                owner = "go-swagger";
                repo = "go-swagger";
                rev = "v${version}";
                sha256 = "sha256-Bw84HQxrI8cSBEM1cxXmWCPqKZa5oGsob2iuUsiAZ+A=";
              };
              doCheck = false;
              vendorHash = "sha256-lhb3tvwhTPNo5+OhGgc3p3ddxFtL1gaIVTpZw0krBhM=";
            };

            controller-tools = pkgs.buildGoModule rec {
              pname = "controller-tools";
              version = "0.4.1";

              src = pkgs.fetchFromGitHub {
                owner = "kubernetes-sigs";
                repo = "controller-tools";
                rev = "v${version}";
                sha256 = "sha256-NQlSP9hRLXr+iZo0OeyF1MQs3PourQZN0I0v4Wv5dkE=";
              };
              vendorHash = "sha256-89hzPiqP++tQpPkcSvzc1tHxHcj5PI71RxxxUCgm0BI=";
              doCheck = false;
            };

            k8sio-tools = pkgs.buildGoModule rec {
              pname = "k8sio-tools";
              version = "0.21.5";

              src = pkgs.fetchFromGitHub {
                owner = "kubernetes";
                repo = "code-generator";
                rev = "v${version}";
                sha256 = "sha256-x05eAO2oAq/jm1SBgwjKo6JRt/j4eMn7oA0cwswLxk8=";
              };
              vendorHash = "sha256-Re8Voj2nO8geLCrbDPqD5rLyiUqE7APcgOnAEJzlkOk=";
              doCheck = false;
            };

            goreman = pkgs.buildGoModule rec {
              pname = "goreman";
              version = "0.3.11";
              src = pkgs.fetchFromGitHub {
                owner = "mattn";
                repo = "goreman";
                rev = "v${version}";
                sha256 = "sha256-TbJfeU94wakI2028kDqU+7dRRmqXuqpPeL4XBaA/HPo=";
              };
              vendorHash = "sha256-87aHBRWm5Odv6LeshZty5N31sC+vdSwGlTYhk3BZkPo=";
              doCheck = false;
            };

            stern = pkgs.buildGoModule rec {
              pname = "stern";
              version = "1.25.0";
              src = pkgs.fetchFromGitHub {
                owner = "stern";
                repo = "stern";
                rev = "v${version}";
                sha256 = "sha256-E4Hs9FH+6iQ7kv6CmYUHw9HchtJghMq9tnERO2rpL1g=";
              };
              vendorHash = "sha256-+B3cAuV+HllmB1NaPeZitNpX9udWuCKfDFv+mOVHw2Y=";
              doCheck = false;
            };

            staticfiles = pkgs.buildGoModule {
              pname = "staticfiles";
              version = "0.0.1"; # no official version
              src = pkgs.fetchFromGitHub {
                owner = "isubasinghe";
                repo = "staticfiles";
                rev = "3d5ddde4d52ddef391b5f4f37e06c80980a5c0c2";
                sha256 = "sha256-fyamqYhKXnY0fzNhS3SL15yHDA/pIuoQ+NsehfA7BCE=";
              };
              vendorHash = null;
            };
            default = config.packages.${package.name};
          };

          devShells = {
            ${package.name} = pkgs.mkShell {
              inherit (package) name;
              shellHook = ''
                unset GOROOT;
                unset GOPATH;
              '';
              inputsFrom = [ config.packages.${package.name} ];
              packages = with pkgs; [
                config.packages.mockery
                config.packages.protoc-gen-gogo-all
                config.packages.grpc-ecosystem
                config.packages.go-swagger
                config.packages.controller-tools
                config.packages.k8sio-tools
                config.packages.goreman
                config.packages.stern
                config.packages.staticfiles
                config.packages.${package.name}
                nodePackages.shell.nodeDependencies
                gopls
                go
                jq
                nodejs
                pythonEnv
                clang-tools
                protobuf
                myyarn
              ];
            };

            devEnv = inputs.devenv.lib.mkShell {
              inherit inputs pkgs;
              modules = [
                ({ pkgs, ... }: {
                  env = argoConfig.env;
                  # This is your devenv configuration
                  packages = with pkgs; [
                    config.packages.mockery
                    config.packages.protoc-gen-gogo-all
                    config.packages.grpc-ecosystem
                    config.packages.go-swagger
                    config.packages.controller-tools
                    config.packages.k8sio-tools
                    config.packages.goreman
                    config.packages.stern
                    config.packages.staticfiles
                    config.packages.${package.name}
                    nodePackages.shell.nodeDependencies
                    gopls
                    go
                    jq
                    nodejs
                    pythonEnv
                    clang-tools
                    protobuf
                    myyarn
                  ];
                  enterShell = ''
                    unset GOPATH;
                    unset GOROOT;
                    ./hack/port-forward.sh;
                    ./hack/free-port.sh 9090;
                    ./hack/free-port.sh 2746;
                    ./hack/free-port.sh 8080;
                    yarn --cwd ui install;
                  '';
                  processes = {
                    workflow-controller = {
                      exec = controllerCmd;
                    };
                    argo-server = {
                      exec = argoServerCmd;
                    };
                    ui = {
                      exec = uiCmd;
                    };
                  };
                })
              ];
            };
            default = config.devShells.devEnv;
          };

          treefmt = {
            projectRootFile = "flake.nix";
            programs.nixpkgs-fmt.enable = true;
            programs.gofmt.enable = true;
          };
        };
    };

}
