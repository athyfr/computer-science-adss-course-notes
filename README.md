# CS ADSS Course Submissions

This repository contains various project submissions for a CS 12 course at ADSS.

These projects (located under the `projects/` directory) each contain a
`about.qmd` file, describing what variable mutability/immutability is, and its
uses. It may contain some Python code (which Quarto executes on rendering) to
demonstrate concepts.

## Compiling

The `qmd` file extension indicates a file uses [Quarto](https://quarto.org/)
flavoured Markdown. These may use additional feature regular Markdown doesn't
have, and use YAML-frontmatter to declare metadata.

To compile `qmd` files into HTML format, you must first install Quarto. To
install on Ubuntu, download the [deb file], and install with `dpkg`:

```bash
sudo dpkg -i quarto-<version>-linux-amd64.deb
```

You can then compile an individual `qmd` file by running `quarto`:

```bash
cd projects/mutability
quarto render about.qmd -o about.pdf
```

Or render the whole document tree by running it in the `projects` directory:

```bash
cd projects
quarto render -o out/
```
