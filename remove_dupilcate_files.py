#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, argparse, hashlib

BLOCK_SIZE = 2**20

parser = argparse.ArgumentParser(description='Find duplicate files')
parser.add_argument('-s', '--minsize', default=0, type=int, help='Minimal size')
parser.add_argument('-c', '--command', default='kfmclient exec', help="A command to use to open files in prompt")
parser.add_argument('-S', '--symlinks', help='Follow symlinks', action='store_true')
#parser.add_argument('-p', '--prompt', help='Prompt', action='store_true')
#parser.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('directories', metavar='files', help='A list of files/directories to compare', action='append')
args = parser.parse_args()

#output = None if options.quiet else sys.stdout
output = sys.stdout

def get_files_dict():
    def add_to_dict(d, f):
        size = os.path.getsize(f)
        if size < args.minsize:
            return
        try:
            d[size].append(f)
        except KeyError:
            d[size] = [f]

    files = {}
    for f in args.directories:
        if os.path.isfile(f):
            add_to_dict(files, f)
        elif os.path.isdir(f):
            for root, dir_list, file_list in os.walk(f):
                for f in file_list:
                    f = os.path.join(root, f)
                    if args.symlinks or not os.path.islink(f):
                        add_to_dict(files, f)

    return files


file_size = get_files_dict()

print('%s files found, %s different size, %s size in conflict.' % (sum(len(k) for k in file_size.values()), len(file_size), len([True for k in file_size if len(file_size[k]) > 1])), file=output)


for key in file_size:
    if len(file_size[key]) < 2:
        continue

    file_hash = {}
    for filename in file_size[key]:
        try:
            f = open(filename, 'rb')
        except IOError as error:
            print(error)
            continue
        sha1 = hashlib.sha1()
        while True:
            data = f.read(BLOCK_SIZE)
            if not data:
                break
            sha1.update(data)
        f.close()
        sha1 = sha1.hexdigest()
        # now we have the hash

        try:
            file_hash[sha1].append(filename)
        except KeyError:
            file_hash[sha1] = [filename]

    for k in file_hash:
        while len(file_hash[k]) > 1:
            print('')
            print("Duplicate files detected :")
            for i, f in enumerate(file_hash[k]):
                try:
                    print('%s : %s' % (i + 1, f))
                except UnicodeEncodeError as error:
                    print(error)
            cmd = input("Delete file n° : ").lower()
            if cmd in ('skip', 's', '0'):
                break
            elif cmd in ('cat', 'c'):
                f = open(file_hash[k][0])
                print(f.read())
                f.close()
                continue
            elif cmd in ('open', 'o'):
                os.system('%s "%s"' % (args.command, file_hash[k][0]))
                continue
            elif cmd == 'all':
                for i in file_hash[k]:
                    os.unlink(i)
                break
            n = int(cmd) - 1
            os.unlink(file_hash[k][n])
            try:
                print("File deleted : %s" % file_hash[k][n])
            except UnicodeEncodeError as error:
                print(error)
            del file_hash[k][n]
