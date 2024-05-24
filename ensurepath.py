import os
import sys
import subprocess
import sys
import json
import userpath

def ensurepath():
    # get all installed packages as json and parse them
    pip_json = subprocess.run([sys.executable, "-m", "pip", "list", '-v', '--format', 'json'], stdout=subprocess.PIPE)
    packages = json.loads(pip_json.stdout)

    # get python binary directory path
    python_path = os.path.dirname(os.path.realpath(sys.executable))

    locations = set()
    locations.add(python_path)
    for pkg in packages:
        for subdir in ['bin','Scripts']:
            # add possible binary containing folders to locations
            locations.add(os.path.join(os.path.dirname(pkg['location']), subdir))

    path_added = False
    need_shell_restart = False

    for location in locations:
        # if location is directory and not in PATH add it to the PATH
        if os.path.isdir(location):
            if not userpath.in_current_path(location):
                userpath.append(location)
                if not path_added:
                    path_added = True
                print(f"Succes! Added the following path to your PATH environment variables:\n {location}")
                need_shell_restart = need_shell_restart or userpath.need_shell_restart(location)

    if need_shell_restart:
        print("\nPlease now restart your shell or terminal")

    if not path_added:
        print("It seems like there was nothing todo, here (that is probably a good thing)!")
    return path_added

if __name__ == "__main__":
    ensurepath()
