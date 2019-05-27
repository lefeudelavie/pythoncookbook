from collections import deque

def search(lines,pattern,history=5):
    prev_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line,prev_lines
        prev_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt','r') as f:
        for line,prev_lines in search(f,'python'):
            for pline in prev_lines:
                print(pline, end='')
            #print('_'*20)
            print(line,end='')
            print('_'*20)





