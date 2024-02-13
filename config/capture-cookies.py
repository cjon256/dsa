#!/usr/bin/env python3

import os
import re
import subprocess

BROWSER = "firefox"

hostname = os.uname().nodename.split(".")[0]

cmd = ["cookies", "-b", BROWSER, "https://leetcode.com/"]
result = subprocess.run(cmd, stdout=subprocess.PIPE)
cookies_raw = result.stdout.decode("utf-8")
carr = cookies_raw.split(";")

with open(f"{hostname}-leetcode-creds.toml", "w") as f:
    f.write("[cookies]\n")
    for cook in carr:
        csrf = re.compile(r"csrftoken=(.*)")
        leet = re.compile(r"LEETCODE_SESSION=(.*)")
        if csrf_match := csrf.match(cook):
            f.write(f'csrf = "{csrf_match.group(1)}"\n')
        if leet_match := leet.match(cook):
            f.write(f'session = "{leet_match.group(1)}"\n')
    f.write("\n")
