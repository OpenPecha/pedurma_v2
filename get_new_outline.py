from pathlib import Path
import yaml



def read_yaml(file_path: Path) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(file_path: Path, data: dict) -> None:
    with open(file_path, 'w') as file:
        yaml.dump(data, file, encoding='utf-8', 
                  allow_unicode=True, default_flow_style=False,sort_keys=False)


def get_new_outline(outline: dict, canon: str) -> dict:
    new_outline = {}
    for text_walker, (key, value) in enumerate(outline.items(),1):
        if canon == 'kangyur':
            pedurma_id = f'PK{text_walker:04}'
        else:
            pedurma_id = f'PT{text_walker:04}'
        value['pedurma_id'] = pedurma_id
        new_outline[key] = value
    return new_outline

if __name__ == "__main__":
    canon = 'kangyur'
    old_outline = read_yaml(Path(f'./data/{canon}/old_{canon}_outline.yml'))
    new_outline = get_new_outline(old_outline, canon)
    write_yaml(Path(f'./data/{canon}/new_{canon}_outline.yml'), new_outline)