#!/usr/bin/python3

import argparse, os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

parser = argparse.ArgumentParser(description='Rainmeter Skin Builder')

# Required positional argument
parser.add_argument('inputFile', help='input .rms file')
parser.add_argument('outputFile', help='output .ini file')

parser.add_argument('--watch', action='store_true', help='Turn watch mode on')
parser.add_argument('--export-to-skins', action='store_true', help='Turn dev mode on')

args = parser.parse_args()

path = '.'

if args.export_to_skins:
    default_path = "/mnt/d/Software/_portable/Rainmeter/Skins"

    try:
        path = os.environ['RMSKINPATH']
        print(f"Exporting to {path} from RMSKINPATH variable...")
    except KeyError:
        path = default_path
        print("Environment variable RMSKINPATH not set.")
        print(f"Exporting to {path}...")
        
    if not os.path.isdir('{}/rmsdev'.format(path)):
        os.mkdir('{}/rmsdev'.format(path))
    path += "/rmsdev"

def transpile():
    # just copies inputFile contents to outputFile
    # doesn't actually transpile anything yet
    with open(args.inputFile, 'r') as inputFile, open(f'{path}/{args.outputFile}', 'w') as outputFile:
        outputFile.write(inputFile.read())


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'Change detected, transpiling new file')
        transpile()

if args.watch:
    transpile()
    print(f'Watching {args.inputFile} for changes')
    print('Press Ctrl+C to stop watching')
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=f'./{args.inputFile}', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
else:
    transpile()