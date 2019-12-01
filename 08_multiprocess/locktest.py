from multiprocessing import Pool, Lock


def send_request(data):
    #lock.acquire()
    for item in data:
        print item
    #lock.release()

def init(l):
	global lock
	lock = l

if __name__ == '__main__':
	data_list = ['d1', 'd2']
	lock = Lock()
	pool = Pool(8, initializer=init, initargs=(lock,))
	pool.map(send_request, data_list)
	pool.close()
	pool.join()
