# [SCA3S](https://github.com/scarv/sca3s): middle-ware (or support infrastructure)

<!--- -------------------------------------------------------------------- --->

[![Build Status](https://travis-ci.com/scarv/sca3s-middleware.svg)](https://travis-ci.com/scarv/sca3s-middleware)
[![Documentation](https://codedocs.xyz/scarv/sca3s-middleware.svg)](https://codedocs.xyz/scarv/sca3s-middleware)

<!--- -------------------------------------------------------------------- --->

*Acting as a component part of the wider
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
various 
[middle-ware](https://en.wikipedia.org/wiki/Middleware)
components (e.g., relating to interaction between front- and back-end).*

<!--- -------------------------------------------------------------------- --->

## Organisation

```
├── bin                     - scripts (e.g., environment configuration)
├── build                   - working directory for build
└── src
    └── sca3s               - source code for SCA3S
        └── middleware      - source code for SCA3S middle-ware
            ├── acquire       - acquire-specific functionality
            ├── analyse       - analyse-specific functionality
            └── share         - shared           functionality
```

<!--- -------------------------------------------------------------------- --->

## Quickstart


<!--- -------------------------------------------------------------------- --->

## Acknowledgements

This work has been supported in part 

- by EPSRC via grant 
  [EP/R012288/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R012288/1) (under the [RISE](https://www.ukrise.org) programme), 
  and 
- by the
  [AWS Cloud Credits for Research](https://aws.amazon.com/research-credits)
  programme.

<!--- -------------------------------------------------------------------- --->
