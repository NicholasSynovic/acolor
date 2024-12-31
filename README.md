# `acolor`: Convert Colors To ANSI Codes

## About

`acolor` is a small utility to convert color codes to ANSI codes. This is
primarily to facilitate shell prompt customization.

Currently only named colors (e.g., red, green, blue) are supported.

## How To Install

Using `pipx`:

`pipx install git+https://github.com/NicholasSynovic/acolor`

A binary is provided
[per release](https://github.com/NicholasSynovic/acolor/tags).

## How To Use

```shell
acolor --help

Usage: acolor [OPTIONS]

Options:
  -c, --color TEXT  Color name to generate ANSI code
  -r, --reset       Print ANSI reset code
  --help            Show this message and exit.
```
