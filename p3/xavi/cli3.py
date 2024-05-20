import os
import sys 

if os.path.exists('/tmp/my_fifo_g8'):
    fd = os.open('/tmp/my_fifo_g8', os.O_RDONLY)

    content = os.read(fd, 512) + b'\n'

    os.write(sys.stdout.fileno(), content) 

    # os.close(fd)
else:  
    os.mkfifo('/tmp/my_fifo_g8')

    fd = os.open('/tmp/my_fifo_g8', os.O_RDONLY)

    content = os.read(fd, 512) + b'\n'
    os.write(sys.stdout.fileno(), content) 

    # os.close(fd)

    

