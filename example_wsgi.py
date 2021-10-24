def hello():
    return 'HELLO'

def world():
    return 'WORLD'


urlpatterns = {
   '/hello/': hello,
   '/world/': world,
}

def application(environ, start_response):
    path = environ['PATH_INFO']
    function = urlpatterns.get(path)
    if function:
        data = function()
    else:
        data = 'No path match'

    data = str(data).encode()

    start_response(f"200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])
