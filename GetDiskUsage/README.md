# getdiskusage.py:

Takes a mountpoint (or directory) as an argument and returns a list of all the files on the mountpoint (or directory) and their disk usage in bytes, in JSON format. This tool will recurse the given mountpoint/directory and return only file stats. Directory stats are not included and if the user launching the script does not have permission to see the contents of a directory, that directory and its contents cannot be included in the output. Example usage: getdiskusage.py /tmp

Note: This has only been tested on Mac but should work on most Linux distros where python is installed.