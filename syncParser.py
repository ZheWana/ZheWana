import feedparser

res = feedparser.parse('https://zhewana.cn/?feed=atom')
anchor = "<!-- Python Anchor -->"

with open("./README.md") as f:
    txt = f.read().split(anchor)[0] + anchor
    f.seek(0)
    f.write(txt)

    f.write("|in Blog|\r\n| --- |")
    for i,entry in enumerate(res.entries):
        title = entry.title if entry.title != "" else "SmallTalk"
        f.write("| " + entry.updated.split('T')[0] + ": [" + title + "]" + "(" + entry.link + ")" + " |")
