import sys
import feedparser
from github import Github
from github import Auth

auth = Auth.Token(sys.argv[1])
g = Github(auth=auth)

res = feedparser.parse('https://zhewana.cn/?feed=atom')
anchor = "<!-- Python Anchor -->"
global txt

with open("./README.md", "r") as f:
    txt = f.read().split(anchor)[0] + anchor

with open("./README.md", "w") as f:
    f.write(txt + "\r\n" + "***\r\n")

    f.write("🎃Blog新鲜事: \r\n")
    for i,entry in enumerate(res.entries):
        print(entry.content)
        print("******************************************************")
        title = entry.title if entry.title != "" else "Small Talk: " + (str)(entry.content[0]["value"].split("\n")[0].replace("<p>", "").replace("</p>", ""))[0:16] + "..."
        f.write("* " + entry.updated.split('T')[0] + " - [" + title + "]" + "(" + entry.link + ")" + "\r\n")
    
    f.write("***\r\n📕Book新章节: \r\n")

repo = g.get_repo("ZheWana/BlogBook")
for commit in repo.get_commits():
    if commit.commit.message != commit.commit.message.split("chap: ")[0]:
        with open("./README.md", "a") as f:
            f.write("* " + str(commit.commit.author.date).split(" ")[0] + " - [" + commit.commit.message.split("chap: ")[1] + "](https://doc.zhewana.cn)\r\n")
