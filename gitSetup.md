# Introduction #

Setting up git on google code


# Details #

for some reason, the default origin didn't work, so I had to use
```
git remote add googlecode https://sasa-tool.googlecode.com/git
git push googlecode master
```

I also used the .netrc setup step described in the **source** tab

another thing that worked: editing .git/config file as described in

http://code.google.com/p/mdanalysis/issues/detail?id=89

## Windows ##

(windows users: Git Push may give you errors regarding username and password for google code.  Look up your auto generated password for code.google. It should probably be at https://code.google.com/hosting/settings. Then follow the instructions given here - http://stackoverflow.com/questions/6031214/git-how-to-use-netrc-file-on-windows-to-save-user-and-password)