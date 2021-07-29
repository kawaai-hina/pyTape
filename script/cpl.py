def cpl():
    from pyTape import pyTape as pt
    import sys
    tape=pt.Tape()
    if len(sys.argv)==1:
        count=1
        print("Use 'exit()' or 'q' to exit")
        while count:
            content=input("[{}]:".format(count))
            if content=="q" or content=="exit()":
                break
            tape(content)
            print("\ntape:{}\nptr:{}\n".format(tape,tape.ptr))
            count+=1
    else:
        for each in sys.argv[1:]:
            print("\nIn {}:\n".format(each))
            with open(each,"r") as f:
                content=f.read()
            tape(content)
if __name__ == '__main__':
    cpl()