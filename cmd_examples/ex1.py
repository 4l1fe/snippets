import cmd, sys
import turtle

def parse(arg):
    return tuple(map(int, arg.split()))

class TurtleShell(cmd.Cmd):
    intro = 'wellcom to shell'
    prompt = 'turtle>>'
    file = None

    def do_forward(self, arg):
        turtle.forward(*parse(arg))

    def do_right(self, arg):
        turtle.right(*parse(arg))

    def do_left(self, arg):
        turtle.left(*parse(arg))

    def do_goto(self, arg):
        turtle.goto(*parse(arg))

    def do_home(self, arg):
        turtle.home()

    def do_circle(self, arg):
        turtle.circle(*parse(arg))

    def do_position(self, arg):
        print('current position is {0}\n'.format(turtle.position()))

    def do_heading(self, arg):
        print('current heading is {}'.format(turtle.heading()))

    def do_color(self, arg):
        turtle.color(arg.lower())

    def do_undo(self):
        'Undo (repeatedly) the last turtle action(s):  UNDO'

    def do_reset(self, arg):
        turtle.reset()

    def do_bye(self, arg):
        print(' bye bye')
        self.close()
        return True
        turtle.bye()

    def do_record(self, arg):
        self.file = open(arg, 'w+')

    def do_playback(self, arg):
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self, arg):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    TurtleShell().cmdloop()