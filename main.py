"""Hold game code in this file"""

def main():
        print me()

class me(object):
        def __init__(self, pos = [0,0]):
                self.pos = pos
        def __repr__(self):
                y, x = self.pos
                if y%2 == 0:
                        return '\033[%s;%sH\xe2\x81\xb0' % (str(y/2), str(x))
                else:
                        return '\033[%s;%sH\xe2\x82\x80' % (str(y/2), str(x))

if __name__=='__main__':
        main()
