from app import app
from queue import ch
import threading

def run_app():
	app.run('localhost', 5000, True, use_reloader=False)

if __name__ == '__main__':
    print '========================'
    th1 = threading.Thread(target=ch.start_consuming)
    th1.start()

    th2 = threading.Thread(target=run_app)
    th2.start()

# To quit Ctrl + \
