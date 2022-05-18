import argparse, os, time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from transpiler import transpileRMS

parser = argparse.ArgumentParser(description='RainMeterScript Transpiler')

# Required positional arguments
parser.add_argument('inputFile', help='input .rms file in folder "src"')
parser.add_argument('outputFile', help='output .ini file in folder "dist"')

# Optional flags
parser.add_argument('-w' ,'--watch', action='store_true', help='Turn watch mode on')
parser.add_argument('-e', '--export-to-skins', type=str, help='Export to Rainmeter/Skins/rmsdev folder')
# parser.add_argement('-f', '--force-overwrite', action='store_true', help="Overwrite existing skin config file at export location")

if not os.path.isdir('dist'):
    os.mkdir('dist')

args = parser.parse_args()

path = ""
skin_folder = ""
export_path = ""

app_refresh_required = False

if args.export_to_skins:
    try:
        path = os.environ['RMPATH']
    except:
        path = "%USERPROFILE%/Documents/Rainmeter"
        
    print(f"Rainmeter path set to {path}")

    skin_folder = args.export_to_skins
    print(f"Skin folder is {skin_folder}")

    export_path = os.path.join(path, "Skins", skin_folder)

    if not os.path.isdir(export_path):
        print(f"Creating folder {export_path}...")
        os.mkdir(export_path)
        app_refresh_required = True

def transpile():
    with open(os.path.join('src', args.inputFile), 'r') as inputFile, open(os.path.join('dist', args.outputFile), 'w') as outputFile:
        ScriptString = inputFile.read()
        SkinString = transpileRMS(ScriptString)
        outputFile.write(SkinString)

def copyToSkinFolder():
    print(f"Exporting skin to {export_path}")
    shutil.copyfile(os.path.join("dist", args.outputFile), os.path.join(export_path, args.outputFile))

    global app_refresh_required
    if app_refresh_required:
        print('Refreshing Rainmeter to load new skin...')
        os.system(f'{path}/Rainmeter.exe !RefreshApp')
        app_refresh_required = False

    print("Refreshing skin...")
    # Activate skin config
    os.system(f'{path}/Rainmeter.exe !ActivateConfig {skin_folder} {args.outputFile}')
    # Refresh skin
    os.system(f'{path}/Rainmeter.exe !Refresh {skin_folder}')

def action():
    transpile()
    if args.export_to_skins:
        copyToSkinFolder()

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print('Change detected, transpiling new file')
        action()

if args.watch:
    action()
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
    action()    