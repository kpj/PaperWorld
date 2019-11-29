import os

from tqdm import tqdm


def scantree(path):
    """Apply `os.scandir` recursively."""
    for entry in tqdm(os.scandir(path)):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry
