import socket
import tkinter as tk

keyls = []
num = ['1', '2', '3', '4', '5', '6', '7']
keyvaild = ['1', '2', '3', '4', '5', '6', '7', 'z', 'x', 'plus', 'minus']
keynote = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'Z', 'X']
bttn = []
addbutton = ''
minusbutton = ''
levelLabel = ''
lev = 1


def Key(action, key):
    global keyls
    global lev
    if (action == 'press'):
        if not (key in keyls):
            keyls.append(key)
            #print(keyls)

            if key != "plus" and key != "minus":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(("127.0.0.1", 8888))
                text = str(lev) + ":" + str(keyls[0])
                sock.send(text.encode('ascii'))
                # Send
                if (key in num):
                    bttn[int(key) - 1]['bg'] = 'pink'
                else:
                    if (key == 'z'):
                        bttn[7]['bg'] = 'yellow'
                    if (key == 'x'):
                        bttn[8]['bg'] = 'yellow'
            elif (key == 'plus'):
                addbutton['bg'] = 'green'
                if (lev < 3):
                    lev += 1
                    levelLabel['text'] = str(lev)
            elif (key == 'minus'):
                minusbutton['bg'] = 'green'
                if (lev > 1):
                    lev -= 1
                    levelLabel['text'] = str(lev)

    else:
        keyls.remove(key)
        #print(keyls)
        if not (key in num):
            if (key == 'z'):
                bttn[7]['bg'] = 'white'
            if (key == 'x'):
                bttn[8]['bg'] = 'white'
            if (key == 'plus'):
                addbutton['bg'] = 'white'
            if (key == 'minus'):
                minusbutton['bg'] = 'white'
        else:
            bttn[int(key) - 1]['bg'] = 'white'


def __keyPress(event):
    if (event.keysym in keyvaild):
        Key('press', event.keysym)


def __keyRelease(event):
    if (event.keysym in keyvaild):
        Key('release', event.keysym)


def main():
    global bttn
    global addbutton
    global minusbutton
    global levelLabel
    __master = tk.Tk()
    __master.bind("<KeyPress>", __keyPress)
    __master.bind("<KeyRelease>", __keyRelease)
    launchpad = tk.Frame(__master)
    launchpad.grid()
    __master.title('Launchpad')
    i = 0
    for j in reversed(range(1, 4)):
        for k in range(3):
            bttn.append(tk.Button(launchpad, text=keynote[i], height=5, width=10))
            bttn[i].grid(row=j, column=k)
            i += 1

    addbutton = tk.Button(launchpad, text="+", height=2, width=10)
    addbutton.grid(row=4, column=0, pady=5)
    levelLabel = tk.Label(launchpad, text=lev)
    levelLabel.grid(row=4, column=1, pady=5)
    minusbutton = tk.Button(launchpad, text="-", height=2, width=10)
    minusbutton.grid(row=4, column=2, pady=5)
    tk.mainloop()

main()
