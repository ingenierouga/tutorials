def print_values(a, b, c):
    print "You're %r years old, %r m tall and %r kg." % (a, b, c)


def main():
    print "How old are you",
    age = raw_input()
    print "How Tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()
    print_values(age, height, weight)


if __name__ == '__main__':
    main()
