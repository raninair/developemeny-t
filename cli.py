import argparse
import pandas as pd
from pubmed_paper_fetcher.fetcher import fetch_pubmed_ids, fetch_pubmed_details

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech affiliations.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching IDs for query: {args.query}")

    ids = fetch_pubmed_ids(args.query)

    if args.debug:
        print(f"Found {len(ids)} papers")

    results = fetch_pubmed_details(ids)

    df = pd.DataFrame(results)

    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df.to_string(index=False))
