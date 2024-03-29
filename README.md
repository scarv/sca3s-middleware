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
SCA3A is, more specifically, pitched as offering
"side-channel analysis as a service":
it allows users to acquire and analyse side-channel data-sets which stem 
from execution of their implementation, without (necessarily) owning or 
operating the associated infrastructure.
Mirroring the goals of SCARV, it places particular emphasis on analogue 
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

## Questions?

- read the
  [wiki](https://github.com/scarv/sca3s-middleware/wiki),
- raise an
  [issue](https://github.com/scarv/sca3s-middleware/issues),
- raise a
  [pull request](https://github.com/scarv/sca3s-middleware/pulls),
- drop us an 
  [email](mailto:sca3s@scarv.org).

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
