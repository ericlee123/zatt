from zatt.client import mtdd

if __name__ == "__main__":
	dd = mtdd.MTDD('localhost', 5254)
	print(dd.send_mt({}, {'x': 0}, []))
	print(dd.send_mt({}, {}, ['x']))
