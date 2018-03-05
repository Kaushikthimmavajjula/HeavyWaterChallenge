from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',default = 'p#w$eeyeny!jt3(8t*gst$8li#k(=#n%%uz@e_fid&(#qwt2u@')
DEBUG = env.bool('DJANGO_DEBUG', default=True)