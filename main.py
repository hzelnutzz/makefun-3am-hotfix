import os
line = "git commit -am 'fixed it'"
with open(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt", "w") as f:
    f.write(line)
