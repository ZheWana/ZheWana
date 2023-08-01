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
    f.write(txt + "\r\n")

    f.write("|in Blog|\r\n| --- |" + "\r\n")
    for i,entry in enumerate(res.entries):
        title = entry.title if entry.title != "" else "SmallTalk"
        f.write("| " + entry.updated.split('T')[0] + ": [" + title + "]" + "(" + entry.link + ")" + " |" + "\r\n")

for repo in g.get_user().get_repos():
    print(repo.name)
    if repo.name == "BlogBook":
        for commit in repo.get_commits():
            print("    " + commit.commit.message)
