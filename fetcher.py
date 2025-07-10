import requests
from typing import List, Dict
from lxml import etree
from .utils import is_non_academic, extract_email, extract_affiliations

def fetch_pubmed_ids(query: str, retmax: int = 100) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_pubmed_details(pubmed_ids: List[str]) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    root = etree.fromstring(response.content)
    results = []
    for article in root.xpath("//PubmedArticle"):
        pubmed_id = article.xpath("MedlineCitation/PMID/text()")[0]
        title = article.xpath(".//ArticleTitle/text()")[0]
        pub_date = " ".join(article.xpath(".//PubDate/*/text()"))

        authors = article.xpath(".//AuthorList/Author")
        non_academic_authors = []
        affiliations = set()
        email = ""

        for author in authors:
            affs = extract_affiliations(author)
            for aff in affs:
                if is_non_academic(aff):
                    affiliations.add(aff)
                    name_parts = author.xpath("LastName/text()") + author.xpath("ForeName/text()")
                    non_academic_authors.append(" ".join(name_parts))
                    if not email:
                        email = extract_email(aff)

        if affiliations:
            results.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(affiliations),
                "Corresponding Author Email": email
            })

    return results
