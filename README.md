# ensurepath

Does exactly one thing:

- ensure that python, pip and with pip installed binarys are in your path.

## use

```bash
$ pip install ensurepath
...
$ python -m ensurepath
...
```

## why

The need occured for me when we started using pipx in a python class just to use `pipx ensurepath`.
That is because the micrsoft store (msstore) install of python does add `python` and `pip` to the path, but not the `scripts` folder where with pip installed shell commands are located.
I tried to also make this script add pip and python to the path if they are not in yet, but have not tested this further.

# issues

If you encouter any error feel free to create an issue and I will try to help, when I have the time. But this is not a python install support service ;-)

This how not been tested thoroughly use at your own risk!

# thanks
This script only uses the [`userpath`](https://pypi.org/project/userpath/) module from [ofek](https://github.com/ofek), thank you!
