from pathlib import Path
from utils import to_yaml, from_yaml, get_unique_id

def parse_pg_info(pg_info, type_):
    try:
        return pg_info["span"][type_]
    except:
        return ""

def get_char_index(pg_start, pg_end, cur_vol_paginations):
    pg_start = int(pg_start)
    pg_end = int(pg_end)
    pagination_layer = cur_vol_paginations
    pagination = list(pagination_layer["annotations"].values())
    try:
        start_pg_info = pagination[pg_start - 1]
        end_pg_info = pagination[pg_end - 1]
    except:
        start_pg_info = {}
        end_pg_info = {}
    pg_start = parse_pg_info(start_pg_info, "start")
    pg_end = parse_pg_info(end_pg_info, "end")
    return pg_start, pg_end

def parse_outline_text(text, cur_vol_paginations):
    span = []
    cur_text = {}
    start, end = get_char_index(text["img_loc_start"], text["img_loc_end"], int(text["vol"]), cur_vol_paginations)
    cur_text = {"vol": int(text["vol"]), "start": start, "end": end}
    span.append(cur_text)
    return span

def reconstruct_index(outline_texts, pecha_path, pecha_id):
    text_annotations = {}
    cur_vol = '1'
    for text_num, (id_, cur_outline_text) in enumerate(outline_texts.items(),1):
        cur_text = {}
        if cur_vol != cur_outline_text["vol"]:
            cur_vol = cur_outline_text["vol"]
            cur_vol_paginations = from_yaml((pecha_path / f"layers/v{cur_vol:03}/Pagination.yml"))
        print(f"D{text_num:04} {cur_outline_text['title']}processing..")
        span = parse_outline_text(cur_outline_text, cur_vol_paginations)
        cur_text[get_unique_id()] = {
            "parts": {},
            "work_id": f"D{text_num:04}",
            "span": span,
        }
        text_annotations.update(cur_text)
        cur_text = {}
    new_index = {
        "id": get_unique_id(),
        "annotation_type": "index",
        "revision": "00001",
        "annotations": text_annotations,
    }
    print(f"Total {len(text_annotations)} text were found..")
    return new_index