__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    return "<h1> hello brave OpenShift Ninja Warrior</h1><br>to fire up build do curl -X POST -v insert_generic_webhook_url_here</br>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
