import os
import sys 
from datetime import datetime


datetime = datetime.now()
datetime_bytes = datetime.isoformat()

while True: 
    fd = os.open('/tmp/my_fifo_g8', os.O_WRONLY)
    os.write(fd, datetime_bytes.encode('utf-8'))
    os.close(fd)
