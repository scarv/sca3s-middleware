# [SCA3S](https://github.com/scarv/sca3s): specification

<!--- -------------------------------------------------------------------- --->

[![Build Status](https://travis-ci.com/scarv/sca3s-spec.svg)](https://travis-ci.com/scarv/sca3s-spec)
[![Documentation](https://codedocs.xyz/scarv/sca3s-spec.svg)](https://codedocs.xyz/scarv/sca3s-spec)

<!--- -------------------------------------------------------------------- --->

*Acting as a component part of the
[SCARV](https://www.scarv.org)
project,
SCA3S is a collection of resources that support the development 
and analysis of cryptographic implementations wrt.
[side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack):
mirroring the goals of SCARV, it places particular emphasis on analogue 
side-channels (e.g., power and EM) stemming from
[RISC-V](https://riscv.org)-based
platforms.
The main
[repository](https://github.com/scarv/sca3s)
acts as a general container for associated resources;
this specific submodule houses
the overarching specification and documentation.*

<!--- -------------------------------------------------------------------- --->

## Organisation

```
├── bin                     - scripts (e.g., environment configuration)
├── build                   - working directory for build
├── doc                     - documentation
│   └── tex                   - LaTeX content
├── extern                  - external resources (e.g., submodules)
│   └── texmf                 - submodule: scarv/texmf
└── src
    └── sca3s               - source code for SCA3S
        └── spec            - source code for SCA3S specification
            ├── acquire       - acquire-specific functionality
            ├── analyse       - analyse-specific functionality
            └── share         - shared           functionality
```

<!--- -------------------------------------------------------------------- --->

## Quickstart

1. Install any associated pre-requisites, e.g.,

   - a modern 
     [LaTeX](https://www.latex-project.org)
     distributation,
     such as
     [TeX Live](https://www.tug.org/texlive),
     including any required packages.

2. Execute

   ```sh
   git clone https://github.com/scarv/sca3s-spec.git
   cd ./sca3s-spec
   git submodule update --init --recursive
   source ./bin/conf.sh
   ```

   to clone and initialise the repository,
   then configure the environment;
   for example, you should find that the environment variable
   `REPO_HOME`
   is set appropriately.

3. Use targets in the top-level `Makefile` to drive a set of
   common tasks, e.g.,

   - execute

     ```sh
     make doc
     ```

     to build the documentation,

   - execute

     ```sh
     make clean
     ```

     to clean-up
     (e.g., remove everything built in `${REPO_HOME}/build`).

<!--- -------------------------------------------------------------------- --->

## Acknowledgements

This work has been supported in part 

- by EPSRC via grant 
  [EP/R012288/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R012288/1)
  under the 
  [RISE](https://www.ukrise.org) 
  programme, 
  and 
- by the
  [AWS Cloud Credits for Research](https://aws.amazon.com/research-credits)
  programme.

<!--- -------------------------------------------------------------------- --->
