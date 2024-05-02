import re

from pathlib import Path

from utils import get_pages, from_yaml



def get_pg_num(pg_ann):
    pg_num = re.search('\d+', pg_ann)[0]
    return pg_num

def preprocessing_note_text(note_text):
    patterns = [
        ['\n', '']
        ['《', '«'],
        ['》', '»']
        ['(\d+)', '<r\g<1>> ']
    ]
    for pattern in patterns:
        note_text = re.sub(pattern[0], pattern[1], note_text)
    return note_text

def get_durchen_pages(pages, durchen_page_span):
    durchen_pages = {}
    durchen_pg_start, durchen_pg_end = durchen_page_span
    for pg_ann, pg_text in pages.items():
        pg_num = get_pg_num(pg_ann)
        if pg_num >= durchen_pg_start and pg_num <= durchen_pg_end:
            durchen_pages[pg_num] = prepare_note_pages(pg_text)
    return durchen_pages

def save_pg_text(pg_num, pg_text,text_dir):
    (text_dir / f'{pg_num:04}.txt').write_text(pg_text, encoding='utf-8')

def save_pg_img(pg_num, text_info, text_dir):
    canon = text_info.get('canon', '')
    vol_num = text_info.get('vol_num', '')
    pg_img_link = f'{canon}/{vol_num}/{pg_num:04}..jpg'
    (text_dir / f'{pg_num:04}.img').write_text(pg_img_link, encoding='utf-8')


def save_note_pages(durchen_pages, text_dir, text_info):
    for pg_num, pg_text in durchen_pages.items():
        save_pg_text(pg_num, pg_text, text_dir)
        save_pg_img(pg_num, text_info, text_dir)

def prepare_note_pages(vol_text, text_info, output_dir):
    pages = get_pages(vol_text)
    text_id = text_info.get('text_id')
    durchen_page_span = text_info['durchen_span']
    durchen_pages = get_durchen_pages(pages, durchen_page_span)
    text_dir = output_dir / text_id
    text_dir.mkdir()
    save_note_pages(durchen_pages,text_dir, text_info)


def get_durchen_span(text_info):
    durchen_span = []
    text_durchen = text_info['durchen']
    durchen_span.append(int(text_durchen['img_loc_start']),int(text_durchen['img_loc_end']))
    return durchen_span

def prepare_text_note_pages(canon, text_id):
    text_info = {}
    canon_outline = from_yaml(Path(f'./{canon}/new_{canon}_outline.yml'))
    for _, text_meta in canon_outline.items():
        if text_id == text_meta.get('pedurma_id', ''):
            text_vol_num = f'v{int(text_info['vol']):03}'
            durchen_span = get_durchen_span(text_info)
            text_info = {
                'text_id' : text_id,
                'canon': canon,
                'vol_num': text_vol_num,
                'durchen_span': durchen_span
            }
            break
    vol_text = Path(f'./data/{canon}/chorten_pedurma_vol_text/{text_vol_num}.txt').read_text(encoding='utf-8')
    output_dir = Path(f'./data/{canon}/proofread_notes/')
    prepare_note_pages(vol_text, text_info, output_dir)

