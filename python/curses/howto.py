#!/usr/bin/env python
import curses


def exitme(stdscr):
    #exit(0)
    print("!@#$%^&*(*&^%$)")
    return

curses.wrapper(exitme)

# this refer to whole screen

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
#keypad mode
stdscr.keypad(1)

#print ("test")



begin_x = 8
begin_y = 8
height = 20
width = 80

# a small screen we need 
win = curses.newwin(height, width, begin_y, begin_x)

win.refresh()

pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)

stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
stdscr.refresh()


def show_my_win():
    try :
        win.addstr("TEST", curses.A_BLINK)
        win.addstr("BOLD", curses.A_BOLD)
        win.addstr("reverse", curses.A_REVERSE)
        win.addstr("A_STANDOUT", curses.A_STANDOUT)
        win.refresh()
    except curses.error:
        win.clear()
        win.move(0,0)
        win.refresh()

x = y=0
while 1:
    c = stdscr.getch()
    if c == ord('p'):
        #PrintDocument()
        show_my_win()
    elif c == ord('q'):
        break  # Exit the while()
    elif c == curses.KEY_LEFT:
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        stdscr.addstr("Pretty text", curses.color_pair(1))
    elif c == curses.KEY_HOME:
        x = y = 0
    else:
        x+=1
        y+=1
        stdscr.addch(y,x, 'a')
        stdscr.refresh()

curses.endwin()




