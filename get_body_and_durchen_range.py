from pathlib import Path
from utils import from_yaml, to_yaml

CANON_IMG_GRP_INFO = {
    'kangyur': {
        'img_grp_base':'I1PD96',
        'img_grp_offset':783
    },
    'tengyur': {
        'img_grp_base':'I1PD95',
        'img_grp_offset':845
    }
}

def get_img_grp_id(img_grp_base, img_grp_offset, text_vol_num):
    img_grp_id = f"{img_grp_base}{img_grp_offset+text_vol_num}"
    return img_grp_id

def get_body_img_range(text_info, img_grp_id):
    text_durchen_info = text_info.get('durchen')
    body_start_img = f'{img_grp_id}{int(text_info.get("img_loc_start")):04}'
    body_end_img = f'{img_grp_id}{int(text_durchen_info.get("img_loc_start")):04}'
    body_img_range = [body_start_img, body_end_img]
    return body_img_range

def get_durchen_img_range(durchen_info, img_grp_id):
    durchen_start_img = f'{img_grp_id}{int(durchen_info.get("img_loc_start")):04}'
    durchen_end_img = f'{img_grp_id}{int(durchen_info.get("img_loc_end")):04}'
    durchen_img_range = [durchen_start_img, durchen_end_img]
    return durchen_img_range


def get_body_and_durchen_range(canon, outline):
    img_grp_base = CANON_IMG_GRP_INFO[canon]['img_grp_base']
    img_grp_offset = CANON_IMG_GRP_INFO[canon]['img_grp_offset']
    body_img_ranges = {}
    durchen_img_ranges = {}
    for _, text_info in outline.items():
        text_id = text_info.get('pedurma_id')
        text_vol_num = int(text_info.get('vol'))
        durchen_info = text_info.get('durchen')
        img_grp_id = get_img_grp_id(img_grp_base, img_grp_offset, text_vol_num)
        body_img_range = get_body_img_range(text_info, img_grp_id)
        durchen_img_range = get_durchen_img_range(durchen_info, img_grp_id)
        body_img_ranges[text_id] = body_img_range
        durchen_img_ranges[text_id] = durchen_img_range
    return body_img_ranges, durchen_img_ranges


if __name__ == "__main__":
    canon = 'kangyur'
    outline = from_yaml(Path(f'./data/{canon}/new_{canon}_outline.yml'))
    body_img_ranges, durchen_img_ranges = get_body_and_durchen_range(canon, outline)
    body_img_ranges_yml = to_yaml(body_img_ranges)
    durchen_img_ranges_yml = to_yaml(durchen_img_ranges)
    Path(f'./data/{canon}/body_img_ranges.yml').write_text(body_img_ranges_yml)
    Path(f'./data/{canon}/durchen_img_ranges.yml').write_text(durchen_img_ranges_yml)