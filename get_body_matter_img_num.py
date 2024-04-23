from pathlib import Path
from utils import from_yaml, to_yaml


def get_body_start_img_num(outline):
    vol_start_img_nums = {}
    cur_vol = 0

    for _, text_info in outline.items():
        text_vol_num = int(text_info['vol'])
        if cur_vol != text_vol_num:
            vol_start_img_nums[text_vol_num] = int(text_info['img_loc_start'])
            cur_vol = text_vol_num
    return vol_start_img_nums


if __name__ == "__main__":
    canon = 'tengyur'
    outline = from_yaml(Path(f'./data/{canon}/new_{canon}_outline.yml'))
    vol_start_img_nums = get_body_start_img_num(outline)
    vol_start_img_nums_yml = to_yaml(vol_start_img_nums)
    Path(f'./data/{canon}/{canon}_vol_offset_mapping.yml').write_text(vol_start_img_nums_yml)


            
        
