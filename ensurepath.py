import os
import sys
import subprocess
import sys
import json
import userpath

def ensurepath():
    pip_json = subprocess.run([sys.executable, "-m", "pip", "list", '-v', '--format', 'json'], stdout=subprocess.PIPE)

    python_path = os.path.dirname(os.path.realpath(sys.executable))

    packages = json.loads(pip_json.stdout)
    locations = set([pkg['location'] for pkg in packages] + [python_path] )

    path_added = False
    need_shell_restart = False

    for location in locations:
        for subdir in ['bin', 'Scripts', '']:
            path = os.path.join(os.path.dirname(location), subdir)
            if os.path.isdir(path):
                if not userpath.in_current_path(path):
                    userpath.append(path)
                    if not path_added:
                        path_added = True
                    print(f"added the following path to your environment variables: {path}")
                    need_shell_restart = need_shell_restart or userpath.need_shell_restart(path)

    if need_shell_restart:
        print("Please now restart your shell or terminal")

    if not path_added:
        print("It seems like there was nothing todo, here (that is probably a good thing)!")
    return path_added

if __name__ == "__main__":
    ensurepath()
