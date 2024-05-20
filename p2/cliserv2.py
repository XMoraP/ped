import os
import sys
import time

r, w = os.pipe()
pid = os.fork()
file_path = sys.argv[1]

def is_text_file(file_path):
    try:
        with open(file_path, 'r') as f:
            f.read(1)
            return True
    except UnicodeDecodeError:
        return False

if pid:
    os.close(r)
    if is_text_file(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        os.write(w, content.encode('utf-8'))
    else:
        with open(file_path, "rb") as f:
            content = f.read()
        os.write(w, content)

    os.close(w)
else:
    os.close(w)
    info = f"[{os.getppid()}] cli2\n[{os.getpid()}] serv2\n"
    os.write(sys.stderr.fileno(), info.encode('utf-8'))
    while True:
        data = os.read(r, 512)
        if not data:
            break
        os.write(sys.stdout.fileno(), data)
    os.close(r)
