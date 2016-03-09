"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# import os
# import sys
# 
# print sys.path
# print len(sys.path)
# 
# sys.path[:] = []
# 
# #activate_env=os.path.expanduser('c:\\app\\Scripts\\activate_this.py')
# #execfile(activate_env, dict(__file__=activate_env))
# os.environ["PYTHONHOME"] = "c:\\app\\Scripts;c:\\app\\Scripts"
# os.environ["PYTHONPATH"] = "c:\\app\\lib;c:\\app\\lib\\site-packages"
# sys.path.append("c:\\Git\\repo\\app\\app")
# sys.path.append("c:\\Git\\repo\\app")
# sys.path.append("c:\\app\\")
# sys.path.append("c:\\app\\DLLs")
# sys.path.append("c:\\app\\include")
# sys.path.append("c:\\app\\lib")
# sys.path.append("c:\\app\\lib\\lib-tk")
# sys.path.append("c:\\app\\lib\\plat-win")
# sys.path.append("c:\\app\\Scripts")
# sys.path.append("c:\\app\\Scripts\\python")
# sys.path.append("c:\\app\\lib\\distutils")
# sys.path.append("c:\\app\\lib\\encodings")
# sys.path.append("c:\\app\\lib\\site-packages")
# sys.path.append("c:\\app\\lib\\site-packages\\django-1.9.2-py2.7.egg")
# sys.path.append("c:\\app\\lib\\site-packages\\psycopg2-2.6.1-py2.7-win32.egg")
# sys.path.append("c:\\app\\lib\\site-packages\\django_phonenumber_field-1.0.0-py2.7.egg")
# sys.path.append("c:\\app\\lib\\site-packages\\babel-2.2.0-py2.7.egg")
# sys.path.append("c:\\app\\lib\\site-packages\\phonenumbers-7.2.4-py2.7.egg") 
# sys.path.append("c:\\app\\lib\\site-packages\\pytz-2015.7-py2.7.egg")
# sys.path.append("c:\\python27\\Lib")
# sys.path.append("c:\\python27\\Lib\\lib-tk")
# sys.path.append("c:\\python27\\lib\\plat-win")
# sys.path.append("c:\\python27\\lib\\site-packages")
# sys.path.append("c:\\python27\\Scripts\\python27.zip")
# sys.path.append("c:\\python27\\DLLs")
# 
# print sys.path
# print len(sys.path)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()