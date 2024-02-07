# Data Structures and Algorithms

This is used to play around on leet code and the like. First in Python, then likely in Rust, Go or other languages.

My workflow for doing leetcode problems uses the following tools:

## Basic code loop (base code generation, testing, and submission):

- [leetcode-cli](https://github.com/clearloop/leetcode-cli)

```bash
cargo install leetcode-cli
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

## Direnv

Lastly, this repo deponds on having direnv installed and configured. Need to direnv allow the .envrc file in the root of this repo.

## Makefile

Making the config for leetcode-cli uses a Makefile in the config directory.

The cookies in the leetcode-cli config are in 1password and the Makefile needs 1password's op tool to generate. If anyone else wants to copy this workflow that is easily adjusted by hardcoding the values.

Mostly the config enables using leetcode-cli to download problems and submit solutions in multiple languages. Switching between languages is done by using the `pyleet`, `rsleet` and `goleet` files in the `bin` directory.

The Python portion of this is very much the most developed. The Rust and Go portions still need to be fleshed out. Mostly because that reflects my skill level in those languages.

## Grind75

After I finish Grind75 (The full 169 question version) in Python, I will move on to Rust and Go (probably in that order).

(Grind75)[https://www.techinterviewhandbook.org/grind75?weeks=26&hours=40&grouping=none]

## Why Rust and Go?

Both seem worthwhile in a Perlis kind of way:

A language that doesn't affect the way you think about programming is not worth knowing.
-- Alan J. Perlis
