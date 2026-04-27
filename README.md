# CS ADSS Course Submissions

This repository contains various project submissions for a CS 12 course at ADSS.

These projects (located under the `projects/` directory) each contain a simple
demonstrating Python script, and an `about.qmd` file, describing what variable
mutability/immutability is, and its uses.

## Compiling

The `qmd` file extension indicates a file uses [Quarto](https://quarto.org/)
flavoured Markdown. These may use additional feature regular Markdown doesn't
have, and use YAML-frontmatter to declare metadata.

To compile `qmd` files into PDF format, you must first install Quarto. To
install on Ubuntu, download the [deb file], and install with `dpkg`:

```bash
sudo dpkg -i quarto-<version>-linux-amd64.deb
```

You can then compile an individual `qmd` file by running `quarto`:

```bash
quarto render about.qmd --to pdf
```
