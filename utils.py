import re
from typing import List
from lxml import etree

ACADEMIC_KEYWORDS = ["university", "college", "institute", "hospital", "school", "lab", "department"]

def is_non_academic(affiliation: str) -> bool:
    return not any(keyword in affiliation.lower() for keyword in ACADEMIC_KEYWORDS)

def extract_email(text: str) -> str:
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match.group(0) if match else ""

def extract_affiliations(author: etree._Element) -> List[str]:
    return author.xpath("AffiliationInfo/Affiliation/text()")
