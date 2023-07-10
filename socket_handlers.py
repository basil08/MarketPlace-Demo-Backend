from .main import socket as sock
from .main import app


# @app.on_event('startup')
# async def startup():
#     await socket.start_background_task(background_task)

# async def background_task():
#     while True:
#         await socket.sleep(1)
#         await socket.emit('message', {'data': 'Hello, world!'})


@sock.on('connect')
async def handle_client_connect_event(sid, *args, **kwargs):
    print("Connected", sid)
	await app.sio.emit('server_antwort01', {'data': 'connection was successful'})    


@sock.on('join_room')
async def handle_client_connect_event(sid, *args, **kwargs):
    print("Connected", sid)

@sock.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

@sock.on('message')
def message(sid, data):
    print('message ', data)

# @sm.on("join")
# async def handle_connection(sid, *args, *kwargs):
#     print("User with {} connected to room".format(sid))

# @sm.on("join_room")
# async def join_room_hand(sid, *args, *kwargs):
#     username, _ = args
#     print(*args)