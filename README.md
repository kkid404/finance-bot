<h1 align="center">Hi there, I'm <a href="https://github.com/kkid404" target="_blank">Andrew</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

<h3 align="center">Backebnd developer</h3>

<br>

<h1>Secretary Bot</h1>


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)


<h2>Project Description</h2>

<p>Telegram bot written in python using the aiogram framework. The main functions are recording income, expenses and recording and deleting cases.</p>
<hr>
<h3>The finance block includes: </h3>
<li> Adding expenses and income</li>
<li> Adding categories to expenses and income</li>
<li> Selecting expenses and income by date</li>
<li> Selecting expenses and income by category</li>
<br>
<h3>To-do block includes: </h3>
<li> Adding and removing do</li>
<li> Selecting do by date and state</li>
<hr>

<h2>Project Launch </h2>


<p>
Install all dependencies from the requirements.txt file with the command:
</p>

``` pyton
pip install -r requirements.txt
```
<p>
Remove the word example from the setting.example.ini file name and put the bot token there, which you can get here: <a>
https://t.me/BotFather
</a></p>
<p>
Enter the bot's token and data for connecting to the database in the settings.ini file
</p>

If you are using sqlite, switch the setting in **data/data.py**
<br>
<br>

with
```python
db = Database(**settings['mysql'])
```
to 
```python
db = Database(**settings['sqlite'])
```
Run the bot with the command:

```python
python main.py
```

<hr>
<h2>Links to framework documentation</h2>
<h3><a href="https://docs.aiogram.dev/en/latest/">Aiogram</a></h3>
<h3><a href="https://docs.ponyorm.org/">Pony ORM</a></h3>

<hr>
<h2>Other</h2>
<h3><a href="https://t.me/secretartattooBot">Link to working copy</a></h3>
<h3><a href="https://t.me/kkidy">Contact me on Telegram</a></h3>

