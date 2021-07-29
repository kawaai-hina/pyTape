def cpl():
    from pyTape import pyTape
    import sys
    tape=pyTape.Tape()
    if len(sys.argv)==1:
        count=1
        print("Use 'exit()' or 'q' to exit")
        while count:
            content=input("[{}]:".format(count))
            if content=="q" or content=="exit()":
                break
            tape.exce(content)
            print("tape:{}\nptr:{}\n".format(tape,tape.ptr))
            count+=1
    else:
        for each in sys.argv:
            print("\nIn {}:\n".format(each))
            with open(fileName,"r") as f:
                content=f.read()
            tape.exce(content)
if __name__ == '__main__':
    cpl()