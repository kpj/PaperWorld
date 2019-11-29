import os

from lxml import etree

from utils import scantree


def main(input_dir, output_dir):
    for entry in scantree(input_dir):
        if not entry.name.endswith('xml'):
            continue

        tree = etree.parse(entry.path)
        body = tree.find('body')

        if body is None:
            continue

        text = '\n'.join([e.text
                          for e in body.iterdescendants()
                          if e.text is not None])

        stem = entry.name.split('.')[0]
        with open(os.path.join(output_dir, f'{stem}.txt'), 'w') as fd:
            fd.write(text)


if __name__ == '__main__':
    main(snakemake.input.extracted_dir, snakemake.output.processed_dir)
