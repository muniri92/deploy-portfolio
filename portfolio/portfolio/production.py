from settings import *

DEBUG = True
TEMPLATE_DEBUG = False
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['ec2-52-36-87-67.us-west-2.compute.amazonaws.com', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
