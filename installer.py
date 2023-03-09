import shutil
from os import getenv
from os.path import join, dirname

WORKING_PATH = dirname(__file__)
DESTINATION_PATH = join(getenv('appdata'), 'Firefox', 'Updater', 'bin')

print(f"Destination: {DESTINATION_PATH}")

try: shutil.rmtree(DESTINATION_PATH)
except: pass

shutil.copytree(WORKING_PATH, DESTINATION_PATH, copy_function=shutil.copy)

print(f"Copied files to destination\n{WORKING_PATH} -> {DESTINATION_PATH}")

input("Go to the above directory and start the program ... Press enter to exit")