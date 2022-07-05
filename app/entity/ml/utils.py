import os



def mla(a,b):
    first=str(a.lower()).split()
    second=str(b.lower()).split()

    if first == second:
        return True
    else:
        return False