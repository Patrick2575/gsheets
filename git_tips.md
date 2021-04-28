## How to add my current project to an already existing GitHub repository ?
Open your Terminal, access to this folder and write:
```shell
git init
git add .
git commit -m "my commit"
git remote set-url origin git@github.com:username/repo.git
git push origin master
```