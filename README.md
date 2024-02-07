# Data Structures and Algorithms

This is used to provide an easy nvim based workflow in Pyton. Rust and Go to grind on leet code.

The Python portion of this is very much the most developed. The Rust and Go portions still need to be fleshed out. Mostly because that reflects my skill level in those languages.

## Commands

The following commands are available:

- pyleet
- rsleet
- goleet

These are just thin wrappers around the tools below to enable a consistent workflow and decent tests for the problems in the three languages.

The workflow for doing leetcode problems requires setting up the following tools:

## Basic code loop (base code generation, testing, and submission):

- [leetcode-cli](https://github.com/clearloop/leetcode-cli)

```bash
cargo install leetcode-cli
```

Need to upadate the database before using any of this.

```bash
leetcode data -u
```

## Rust Testing code generation:

- [cargo-leet](https://github.com/rust-practice/cargo-leet)

I use my own fork in case of breaking changes in the main repo.

```bash
cargo install --git https://github.com/cjon256/cargo-leet.git --branch develop --features=tool
```

## Go Testing code generation:

- [gotests](https://github.com/cweill/gotests)

```bash
go install github.com/cweill/gotests/gotests@latest
```

## My own dsa.nvim plugin:

- [dsa.nvim](https://github.com/cjon256/dsa.nvim)

Install using lazy.nvim:

```lua
    {
        'cjon256/dsa.nvim',
        config = function()
            require('dsa').setup()
        end,
    }
```

This nvim plugin depends is just to enable working with this repo.

## Direnv and Misc

This repo deponds on having direnv installed and configured. Need to direnv allow the .envrc file in the root of this repo.

Also need some basic cli commands: `gsed`, `ex` (from vim) and `make`. Lastly, the Makefile in the config directory depends on the `op` command from 1password.

## Makefile

Making the config for leetcode-cli uses a Makefile in the config directory.

My cookies in the leetcode-cli config are in 1password and the Makefile needs 1password's op tool to generate so it is unliely to work for anyone else. But copying this workflow is easily adjusted by hardcoding the values for anyone who does not use 1password.

Mostly the config enables using leetcode-cli to download problems and submit solutions in multiple languages. Switching between languages is done by using the `pyleet`, `rsleet` and `goleet` files in the `bin` directory.

## Grind75

After I finish Grind75 (The full 169 question version) in Python, I will move on to Rust and Go (probably in that order).

(Grind75)[https://www.techinterviewhandbook.org/grind75?weeks=26&hours=40&grouping=none]

## Why Rust and Go?

Both seem worthwhile in a Perlis kind of way:

A language that doesn't affect the way you think about programming is not worth knowing.
-- Alan J. Perlis
