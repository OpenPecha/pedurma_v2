from pathlib import Path


def get_volume_text(volume_path):
    volume_text = ""
    page_paths = list(volume_path.iterdir())
    page_paths.sort()
    for page_path in page_paths:
        page_text = page_path.read_text()
        volume_text += f'{page_text}\n\n\n'
    return volume_text

