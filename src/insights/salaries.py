from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries = read(path)
    max_salary = 0
    for salary in salaries:
        if salary["max_salary"].isdigit() and int(salary["max_salary"]) > int(
            max_salary
        ):
            max_salary = salary["max_salary"]
    return int(max_salary)


def get_min_salary(path: str) -> int:
    salaries = read(path)
    min_salary = 1000000
    for salary in salaries:
        if salary["min_salary"].isdigit() and int(salary["min_salary"]) < int(
            min_salary
        ):
            min_salary = salary["min_salary"]
    return int(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["max_salary"]) < int(job["min_salary"]):
            raise ValueError
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except Exception:
        raise ValueError
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    matching_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                matching_jobs.append(job)
        except ValueError as v:
            print(v)
    return matching_jobs
