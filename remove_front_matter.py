import re
from pathlib import Path
from utils import from_yaml, get_pages
from pg_num_to_img_num import convert_pg_no_to_img_num



def remove_front_matter(vol_text, vol_offset):
    new_vol_text = ''
    pages = get_pages(vol_text)
    for pg_ann, page in pages.items():
        img_num = int(re.search('\d+', pg_ann)[0])
        if img_num >= vol_offset:
            new_vol_text += f'{pg_ann}\n{page}\n'
    return new_vol_text

if __name__ == "__main__":
    canon = 'tengyur'
    vol_offset_mapping = from_yaml(Path(f'./data/{canon}/{canon}_vol_offset_mapping.yml'))
    vol_paths = list(Path(f'./data/{canon}/derge_google_pedurma').iterdir())
    vol_paths.sort()
    for vol_path in vol_paths:
        vol_text = vol_path.read_text(encoding='utf-8')
        vol_num = int(vol_path.stem[1:])
        vol_offset = vol_offset_mapping.get(vol_num)
        new_vol_text = convert_pg_no_to_img_num(vol_text)
        new_vol_text = remove_front_matter(new_vol_text, vol_offset)
        Path(f'./data/{canon}/dg_pedurma/{vol_path.stem}.txt').write_text(new_vol_text,encoding='utf-8')
