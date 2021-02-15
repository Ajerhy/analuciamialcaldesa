import os

try:
    if(os.environ['ENV'] == "prod"):
        DEBUG = False
        ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']
        SECRET_KEY = os.environ['SECRET_KEY']
        print("Usando la configuración de PRODUCCIÓN.")
    else:
        DEBUG = True
        ALLOWED_HOSTS = ['*']
        #ALLOWED_HOSTS = ['analuciamialcaldesa.herokuapp.com']
        SECRET_KEY = '0oc305u3geb+wlwy!quqdxt$d0_*!9#7f1lm#a+wzh3*wk1+oq'
        DEBUG_PROPAGATE_EXCEPTIONS = True
except:
    DEBUG = True
    #DEBUG = False
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = '0oc305u3geb+wlwy!quqdxt$d0_*!9#7f1lm#a+wzh3*wk1+oq'
    DEBUG_PROPAGATE_EXCEPTIONS = True
    print("Usando la configuración DEBUG.")
