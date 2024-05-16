import sys
import fitz
import argparse
argsParser = argparse.ArgumentParser(description='pdf ToC modifier.')
argsParser.add_argument('source',
                            help='source pdf file directory')
args = argsParser.parse_args()
source = fitz.open(str(args.source))
toc = source.get_toc(True)
for lvl, title, page in toc:
    print(f'{"    " * (lvl - 1)}{title}')
