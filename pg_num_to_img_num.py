import re
from pathlib import Path

def get_page_folio(pg_ann):
    folio = re.search('a|b', pg_ann)[0]
    return folio

def get_pg_num(pg_ann):
    pg_num = re.search('\d+', pg_ann)[0]
    return pg_num

def get_img_num(pg_ann):
    pg_folio = get_page_folio(pg_ann)
    pg_num = get_pg_num(pg_ann)
    if pg_folio == "a":
        img_num = int(pg_num)*2-1
    else:
        img_num = int(pg_num)*2
    return img_num

def convert_pg_no_to_img_num(vol_text):
    pg_anns = re.findall('\[[𰵀-󴉱]?\d+[a|b]\]', vol_text)
    for pg_ann in pg_anns:
        img_num = get_img_num(pg_ann)
        vol_text = vol_text.replace(pg_ann, f'[{img_num}]')
    return vol_text

