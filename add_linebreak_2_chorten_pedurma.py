import re
from pathlib import Path
from fast_antx.core import transfer
from volume_complier import get_volume_text

def clean_chorten_text(chorten_vol_text):

    chorten_vol_text = re.sub('\[.+?\]', '', chorten_vol_text)
    chorten_vol_text = re.sub('\n', '', chorten_vol_text)
    return chorten_vol_text


def transfer_paginations_line_break(derge_google_vol_text, chorten_vol_text):
    patterns = [['pagination', '(\[\d+\])' ], ['linebreak', '(\n)']]
    chorten_with_dg_pagination = transfer(derge_google_vol_text, patterns, chorten_vol_text)
    
    return chorten_with_dg_pagination

def transfer_line_break(derge_google_vol_text, chorten_vol_text):
    patterns = [['linebreak', '(\n)']]
    chorten_with_dg_linebreak = transfer(derge_google_vol_text, patterns, chorten_vol_text)
    
    return chorten_with_dg_linebreak

def add_line_break_2_chorten_pedurma(derge_google_vol_text, chorten_vol_text):
    chorten_vol_text = clean_chorten_text(chorten_vol_text)
    chorten_with_dg_pagination = transfer_paginations_line_break(derge_google_vol_text, chorten_vol_text)
    
    return chorten_with_dg_pagination


if __name__ == "__main__":
    canon = 'tengyur'
    volume_paths = list(Path(f"./data/{canon}/chorten_pedurma_pagewise/").iterdir())
    volume_paths.sort()
    for volume_path in volume_paths:
        vol_num = int(volume_path.stem)
        chorten_vol_text = get_volume_text(volume_path)
        derge_google_vol_text = Path(f'./data/{canon}/dg_pedurma/v{vol_num:03d}.txt').read_text()
        chorten_volume_text = add_line_break_2_chorten_pedurma(derge_google_vol_text, chorten_vol_text)
        Path(f'./data/{canon}/chorten_pedurma_vol_text/v{vol_num:03d}.txt').write_text(chorten_volume_text, encoding='utf-8')