print "hello world"

def get_name():
	name = raw_input("what is your name: ")
	return name


def greeting():
	name = get_name()
	greeting = "Hi " + name + "!"
	print greeting


greeting() 