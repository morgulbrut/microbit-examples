#!/bin/sh

pandoc --to=beamer --output=oed2018.pdf --pdf-engine=xelatex oed2018.md
# pandoc --to=beamer --output=oed2018.tex oed2018.md