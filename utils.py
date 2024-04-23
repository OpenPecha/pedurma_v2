import yaml
import re
from pathlib import Path
from uuid import uuid4

def get_unique_id():
    return uuid4().hex


def from_yaml(yml_path):
    return yaml.safe_load(yml_path.read_text())

def to_yaml(yml):
    return yaml.safe_dump(yml,sort_keys=False, allow_unicode=True)

def get_pages(vol_text):
    pages = {}
    page_anns = re.split(r"(\[\d+\])", vol_text)
    pg_ann = ""
    for i, page in enumerate(page_anns[1:]):
        if i % 2 == 0:
            pg_ann = page
        else:
            pages[pg_ann] = page
    return pages