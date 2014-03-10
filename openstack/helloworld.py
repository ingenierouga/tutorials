
import unittest

# Hello world
def HelloWorld(s):
    return "Hello, " + s + "!"

def print_values(a,b,c):
    print "So, you're %r years old, %r meters tall and %r Kg heavy." % (
    a, b, c)

# Unit test
class HelloWorldTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(HelloWorld("Joe") == "Hello, Joe!")

    def testTwo(self):
        self.assertTrue(HelloWorld("world") == "Hello, world!")

def main():
#    unittest.main()
#    print (HelloWorld("Emilio"))
#    HelloWorld("Emilio2")
    print "How old are you",
    age = raw_input()
    print "How Tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()
    print_values(age,height,weight)

if __name__ == '__main__':
    main()	