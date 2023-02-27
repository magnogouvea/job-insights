from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = read(path)
    unique_industries = []
    for ind in industries:
        if ind["industry"] not in unique_industries and ind["industry"] != "":
            unique_industries.append(ind["industry"])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_list_of_industry = [
        ind for ind in jobs if ind["industry"] == industry
    ]
    return filtered_list_of_industry
