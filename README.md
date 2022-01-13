## Flask-Login
--->Build With Flask, SQlAlchemy and Bootstrap...!

### Requirements

Download and install Python 3.8.10 or Above make sure to check the box Add Python to PATH on the installation setup screen.


### Installation
          
Navigate to your current project directory for this case it will be **Flask-Login**. <br>
          
### 1. Create an Virtual environment
          
Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies.

**Windows**
          
```cd Flask-Login
py -3 -m venv venv
```
            
**macOS/Linux**
          
```cd Flask-Login
python3 -m venv venv
```

### 2. Activate the Virtual environment
          
**Windows** 

```
venv\Scripts\activate
```
          
**macOS/Linux**

```
. venv/bin/activate
```
or
```
source venv/bin/activate
```
### 3. Setup Config.env File
**SECRET_KEY ='Your secret Key'**  --> Secret key can any string at any length. <br>
**SQLALCHEMY_DATABASE_URI='sqlite:///flasklogin.db'** --> provide your own database url or leave it default for to use ***flasklogin.db***.<br>
For sqlite ref:https://sqlitebrowser.org/. If you want to use MySQl Change the value to **mysql://user:password@HostAddress/databasename'**.<br>
**MAIL_SERVER = 'smtp.googlemail.com'** ---> Email server provider, here Iam using google server. <br>
**MAIL_PORT = '465'** --> Goolge Server Port. <br>
**MAIL_USERNAME = 'Your Gmail Address'** --> Provide Your own or Work Gmail. <br>
**MAIL_PASSWORD = 'Your Gamil App Password'** --> Create gmail app passsword and fill it, Ref this article:https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882 <br>
**MAIL_DEFAULT_SENDER = 'Your Sender Address'** -->Provide Your own or Work Gmail, this should be displayed on the receiver Email. <br>

### 4. Install the requirements

Applies for windows/macOS/Linux

```
pip install -r requirements.txt
```
  
### 5. Run the application 

**For linux and macOS**

Make the run file executable by running the code

```
chmod 777 run.sh
```

Then start the application by executing the run.sh file

```
./run.sh
```

**On windows**
```
set FLASK_APP=app
$env:FLASK_APP = "app.py"
flask run
```
**Demo and Caution** <br>
Click **https://flaskweblogin.herokuapp.com/** <br>
All Data in demosite Will store On My personal Database..!
