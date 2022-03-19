# Smart-SNS

## FaceBook

## Instagram

## Twitter

- [Tools and Libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2)

## Youtube

## pip package update

Pip can be used to upgrade all packages on either Windows or Linux (and Mac OS X).):

1. Output a list of installed packages into a requirements file (requirements.txt): 
  `pip freeze > requirements.txt`
2. Edit requirements.txt, and replace all ‘==’ with ‘>=’. Use the ‘Replace All’ command in the editor.
3. Upgrade all outdated packages: 
  `pip install -r requirements.txt --upgrade`

[References](https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/)

## Visual Studio Code Python Intelligence 

pip で install したパッケージ関連でエラーが出たのを解消した手順

setting.json に 以下を加えるだけ

```
"python.analysis.extraPaths": ["./sources", "lib/python"],
```

[参考](https://github.com/microsoft/pylance-release/issues/29)