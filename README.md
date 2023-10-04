# LanguageLearning
A web application for language learning using Flask, MongoDB, and Bootstrap 5 written in Python, javascript, jQuery and html.
  
This is deployed to [http://language.kkangshawn.com](http://language.kkangshawn.com) via AWS Elastic Beanstalk.
  
![image](https://github.com/kkangshawn/languagelearning/assets/16316511/713b71dc-3d33-4b62-933d-02300339f63e)
----
![image](https://github.com/kkangshawn/languagelearning/assets/16316511/4020492a-259d-4e58-911a-66df91fc6453)
----
### Requirements
- Python 3
- Flask
  ```bash
  pip install flask
  ```
- MongoDB
  ```
  pip install pymongo
  ```

### Run
```
python application.py
```

> If you want to run in debug mode, add FLASK_DEBUG environmental variable. The debug mode provides ***dynamic loading*** of web server everytime you save any documents and ***traceback***.
>- in Linux or MAC
>```
>export FLASK_DEBUG=True
>```
>
>- in Windows, open powershell and
>```
>$Env:FLASK_DEBUG = "True"
>```
