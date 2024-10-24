# coding: utf-8
import psutil
def show_children(pid):
    p = psutil.Process(pid)
    while p:
        clist = []
        for c in p.children(recursive=True):
            try:
                clist.append([c.pid, c.name(), c.exe(), ' '.join(c.cmdline())])
            except psutil.Error as e:
                clist.append([c.pid, c, e])
           
        yield clist
def iterate_children(pid):
    cout = ''
    for c in show_children(pid):
        if c != cout:
            cout = c
            print(c)
            time.sleep(0.5)
            
    
