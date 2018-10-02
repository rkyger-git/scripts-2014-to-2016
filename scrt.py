
def main():
    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch)+ 1)
    print(msg)

main()
