import argparse, os, time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from transpiler import transpileRMS

parser = argparse.ArgumentParser(description='Rainmeter Skin Builder')

# Required positional argument
parser.add_argument('inputFile', help='input .rms file in folder "src"')
parser.add_argument('outputFile', help='output .ini file in folder "dist"')

parser.add_argument('--watch', action='store_true', help='Turn watch mode on')
parser.add_argument('--export-to-skins', action='store_true', help='Export to Rainmeter/Skins/rmsdev folder')

if not os.path.isdir('dist'):
    os.mkdir('dist')

args = parser.parse_args()

# path = 'D:/Software/_portable/Rainmeter'
path = "%USERPROFILE%/Documents/Rainmeter"

# if args.export_to_skins:
#     default_path = "D:/Software/_portable/Rainmeter"

#     try:
#         path = os.environ['RMPATH']
#         print(f"Exporting to {path}/Skins from RMPATH variable...")
#     except KeyError:
#         path = default_path
#         print("Environment variable RMPATH not set.")
#         print(f"Exporting to default {path}/Skins...")
        
#     if not os.path.isdir(f'{path}/Skins/rmsdev'):
#         os.mkdir(f'{path}/Skins/rmsdev')
#     dev = "/Skins/rmsdev"

def transpile():
    with open(f'src/{args.inputFile}', 'r') as inputFile, open(f'dist/{args.outputFile}', 'w') as outputFile:
        ScriptString = inputFile.read()
        SkinString = transpileRMS(ScriptString)
        outputFile.write(SkinString)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print('Change detected, transpiling new file')
        transpile()
        if (args.export_to_skins):
            print(f"exporting skin to {path}/Skins/rmsdev")
            shutil.copyfile("dist/" + args.outputFile, f"{path}/Skins/rmsdev/{args.outputFile}")
            print("refreshing skin")
            os.system(f'{path}/Rainmeter.exe !ActivateConfig "rmsdev" "test.ini"')
            os.system(f'{path}/Rainmeter.exe !Refresh rmsdev')

if args.watch:
    transpile()
    print(f'Watching {args.inputFile} for changes')
    print('Press Ctrl+C to stop watching')
    print('...')
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=f'./src', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

else:
    transpile()