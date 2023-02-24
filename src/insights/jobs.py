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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
