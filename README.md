# [`lab.scarv.org`](https://github.com/scarv/lab.scarv.org): specification

<!--- -------------------------------------------------------------------- --->

[![Build Status](https://travis-ci.com/scarv/lab-spec.svg)](https://travis-ci.com/scarv/lab-spec)
[![Documentation](https://codedocs.xyz/scarv/lab-spec.svg)](https://codedocs.xyz/scarv/lab-spec)

<!--- -------------------------------------------------------------------- --->

*Acting as a component part of the
[SCARV](https://www.scarv.org)
project,
`lab.scarv.org` is a collection of resources that support the
development and analysis of cryptographic implementations wrt.
[side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack):
it places particular emphasis on analogue side-channels (e.g.,
power and EM) stemming from
[RISC-V](https://riscv.org)-based
platforms.
The main
[repository](https://github.com/scarv/lab.scarv.org)
acts as a general container for associated resources;
this specific submodule houses
the `lab.scarv.org` specification (i.e., overarching documentation).*

<!--- -------------------------------------------------------------------- --->

## Organisation

```
├── bin                     - scripts (e.g., environment configuration)
├── build                   - working directory for build
├── doc                     - documentation
│   └── tex                   - LaTeX content
└── extern                  - external resources (e.g., submodules)
    └── texmf                 - submodule: scarv/texmf
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
   git clone https://github.com/scarv/lab-spec.git
   cd ./lab-spec
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

This work has been supported in part by EPSRC via grant 
[EP/R012288/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R012288/1),
under the [RISE](http://www.ukrise.org) programme.

<!--- -------------------------------------------------------------------- --->
