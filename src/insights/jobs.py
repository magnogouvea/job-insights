import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        dict_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        data = [row for row in dict_reader]
        return data


def get_unique_job_types(path: str) -> List[str]:
    job_types = read(path)
    unique_jobs = []
    for job in job_types:
        if job["job_type"] not in unique_jobs:
            unique_jobs.append(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_list_of_jobs = [
        job for job in jobs if job["job_type"] == job_type
    ]
    return filtered_list_of_jobs
