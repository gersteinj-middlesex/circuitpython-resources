import shutil, os
from pathlib import Path
board_dir = Path('E:/')
lib_dir = board_dir / 'lib'
source_dir = Path('board-resetter-files')

# # copy test file
# shutil.copy(source_dir / 'testfile.txt', board_dir)

def rm_subdir(dirname):
    """Remove a subdirectory from the board"""
    try:
        shutil.rmtree(board_dir / dirname)
        return f"{dirname} deleted successfully"
    except FileNotFoundError:
        return f"{dirname} not found"
    except:
        return f"I don't know what to do about {dirname}"

# Erase .vscode, .fseventsd
rm_subdir('.vscode')
rm_subdir('.fseventsd')
rm_subdir('Android')

# Erase any .txt files other than boot_out.txt and README.txt, any .py files other than main.py
for f in board_dir.glob('*.txt'):
    if f in [board_dir / 'boot_out.txt', board_dir / 'README.txt']:
        print(f"Keep {f}")
    else:
        os.unlink(f)

# Erase all .py files
for f in board_dir.glob('*.py'):
    os.unlink(f)

# Erase contents of 'lib' directory other than neopixel.mpy
if not lib_dir.exists():
    shutil.copytree(source_dir / 'lib', board_dir / 'lib')
else:
    try:
        for f in lib_dir.glob('*'):
            if f in [lib_dir / 'neopixel.mpy', lib_dir / 'adafruit_dotstar.mpy']:
                print(f'Keep {f}')
            else:
                if f.is_dir():
                    # print(f'{f} is a folder to delete')
                    shutil.rmtree(f)
                else:
                    # print(f'{f} is a file to delete')
                    os.unlink(f)
    except:
        print("I don't know what to do")

# Copy 'main.py' from the source directory
shutil.copy(source_dir / 'main.py', board_dir / 'main.py')

print('complete')