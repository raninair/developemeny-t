# PubMed Paper Fetcher

## Description

Fetches PubMed papers with at least one non-academic author affiliated with pharmaceutical or biotech companies.

## Features

- PubMed API search
- Filters out academic authors
- Extracts emails, affiliations
- Outputs CSV or console
- Poetry-based CLI

## Setup

```bash
git clone https://github.com/yourname/pubmed-paper-fetcher
cd pubmed-paper-fetcher
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer treatment" -f results.csv
```

## Tools Used

- [Poetry](https://python-poetry.org/)
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [LXML](https://lxml.de/)
- [pandas](https://pandas.pydata.org/)
