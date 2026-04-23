# Lessons Learned

This document keeps track of lessons I've learned from my own mistakes.

## KISS; Keep It Simple, Stupid

I often have a tendency to overcomplicate things, so many of my lessons will be
in this category.

- **When using data read from a file, keep it in a format closest to what's on
  the disk, as far as is possible.**

  I have an assumption I make sometimes that the ideal format for run-time is
  different than the ideal format for disk, which leads me to create unnecessary
  steps in saving/loading that data. In almost all cases, the overhead would
  outweigh any benefits.
