dmhy-catcher-python
===================
This is a python bot which can grab the magnet link from dmhy(http://share.dmhy.org)

<h1>Installation</h1>

  Install the relative python package
  
  apt-get install python-django python-bs4
  easy_install --upgrade pytz
  
<h1>run</h1>
```
  cd dmhy-catcher-python
  
  ./manage.py syncdb 
  # ( then key in your administrator username/password )
  ./manage.py runserver [port]
  # (use 0.0.0.0:port can let someone access your site from the internet)
```
<h4>Before using this program, remember to set DEBUG = False @setting.py</h4>
