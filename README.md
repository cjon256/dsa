# Data Structures and Algorithms

This is used to play around on leet code and the like. First in Python, then likely in Rust, Go or other languages.

My workflow for doing leetcode problems uses the following tools:

## Basic code loop (base code generation, testing, and submission):

- [leetcode-cli](https://github.com/clearloop/leetcode-cli)

```
$ cargo install leetcode-cli
$ leetcode data -u
```

## Rust Testing code generation:

- [cargo-leet](https://github.com/rust-practice/cargo-leet)

```
$ cargo install --git https://github.com/cjon256/cargo-leet.git --branch develop --features=tool
```

## Go Testing code generation:

- [gotests](https://github.com/cweill/gotests)

```
$ go install github.com/cweill/gotests/gotests@latest
```

## My own dsa.nvim plugin:

- [dsa.nvim](https://github.com/cjon256/dsa.nvim)
  Install using lazy.nvim:

```
{ "cjon256/dsa.nvim", config = function() require("dsa").setup() end }
```

This on having this repo and having direnv installed and configured. Need to direnv allow the .envrc file in the root of this repo.

The cookies in the leetcode-cli config are in 1password and the Makefile needs their op tool to generate.

The Python portion of this is very much the mast developed. The Rust and Go portions still need to be fleshed out.

## Grind75

After I finish Grind75 (The full 169 question version) in Python, I will move on to Rust and Go (probably in that order).

(Grind75)[https://www.techinterviewhandbook.org/grind75?weeks=26&hours=40&grouping=none]

## Why Rust and Go?

Both seem worthwhile in a Perlis kind of way:

A language that doesn't affect the way you think about programming is not worth knowing.
-- Alan J. Perlis
