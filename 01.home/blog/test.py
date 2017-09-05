import os

replace= """'Shashank Agarwal'"""
replacement = """'Shashank Agarwal'"""

for dname, dirs, files in os.walk("/Library/WebServer/Documents/hackiteasy/user/pages/01.home/blog/"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
            s = s.replace(replace, replacement)
            print(s)
            with open(fpath, "w") as f:
            	f.write(s)