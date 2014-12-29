"""Hold game code in this file"""

def main():
        from lib.keyboard import getch, Key
        from lib.display import loc
        me = Player([80,80])
        print me
        while True:
                ch = getch()
                if ch == Key.UP_ARROW:
                        #y,x = me.pos
                        #if y%2:
                        #        print loc(y,x) + ' '
                        me.pos[0] -= 1
                elif ch == Key.DOWN_ARROW:
                        #y,x = me.pos
                        #if y%2:
                        #        print loc(y,x) + ' '
                        me.pos[0] += 1
                elif ch == Key.LEFT_ARROW:
                        #y,x = me.pos
                        #print loc(y,x) + ' '
                        me.pos[1] -= 1
                elif ch == Key.RIGHT_ARROW:
                        #y,x = me.pos
                        #print loc(y,x) + ' '
                        me.pos[1] += 1
                elif ch == 'q':
                        break
                print me

class Player(object):
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
