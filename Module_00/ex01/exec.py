import sys   #

if len(sys.argv) > 1:                       # sys.argv takes all the arguments
    text = " ".join(sys.argv[1:])           # " ".join(...) merge arguments with one space
    print(text[::-1].swapcase(), end="")    # ::-1 reverse the string
                                            # .swapcase() swaps its letters
                                            # end="" avoid adding additional empty line
