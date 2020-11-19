import asyncio
import websockets
import subprocess

async def time(websocket, path):
    script = await websocket.recv()
    with subprocess.Popen(script.split(' '),
                          stdout=subprocess.PIPE,
                          bufsize=1,
                          universal_newlines=True) as process:
        for line in process.stdout:
            line = line.rstrip()
            print(f"line = {line}")
            await websocket.send(line)

start_server = websockets.serve(time, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
