import asyncio
from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")


@app.route('/')
async def test(request):
    await asyncio.sleep(1)
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run()
