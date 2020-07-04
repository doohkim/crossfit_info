daemon = False
chdir = '/srv/crossfit_project0325/app'
bind = 'unix:/run/crossfit.sock'
accesslog = '/var/log/gunicorn/crossfit-access.log'
errorlog = '/var/log/gunicorn/crossfit-error.log'
capture_output = True