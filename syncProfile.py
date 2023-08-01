import feedparser              
import sys
import importlib

importlib.reload(sys)
sys.setdefaultencoding('utf8')

res = feedparser.parse('https://zhewana.cn/?feed=atom')
anchor = "<!-- Python Anchor -->"
global txt

with open("./README.md", "r") as f:
    txt = f.read().split(anchor)[0] + anchor

with open("./README.md", "w") as f:
    f.write(txt + "\r\n")

    f.write("|in Blog|\r\n| --- |" + "\r\n")
    for i,entry in enumerate(res.entries):
        title = entry.title if entry.title != "" else "SmallTalk"
        f.write("| " + entry.updated.split('T')[0] + ": [" + title + "]" + "(" + entry.link + ")" + " |" + "\r\n")
