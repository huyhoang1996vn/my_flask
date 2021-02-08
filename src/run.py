from app import app
from queue import ch
import threading



print '========================= in file run ', __name__

if __name__ == '__main__':
	# app.run('localhost', 7002, True)
	# ch.start_consuming()
    threading.Thread(target=app.run).start()
    threading.Thread(target=ch.start_consuming).start()
