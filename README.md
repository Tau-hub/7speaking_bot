# How to use 



Create a file named `creds.py`  ìn the same directory as `main.py`. 

Add two variables in it : 

````python
user = 'mymail@mail.fr'
password = '<my_password>'
````

Add selenium package 
````sh
pip install selenium
````

Check if the path of firefox in `main.py` is the same as yours.

You can go !

```
python main.py
```

Has been tested on windows only. If you want to use linux, modify the path of firefox and download geckodriver for linux.

Selenium should start and fill in the username & password you have to do the captcha then press enter on the bot.

You can go to sleep now, or play some games....
