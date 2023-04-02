# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    choice = input()
    if "I" in choice:
        return (input().rstrip(), input().rstrip())
    elif "F" in choice:
        lines = open("./tests/06","r").readlines()
        return (lines[0].rstrip(), lines[1].rstrip())
    else:
        print("wrong command")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    d = 256
    prime_num = 101
    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(M-1):
        h = (h*d)%prime_num

    for i in range(M):
        p = (d*p + ord(pattern[i])) % prime_num
        t = (d*t + ord(text[i])) % prime_num

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j+=1
            if j==M:
                result.append(i)
        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % prime_num
            if t < 0:
                t = t+prime_num
                
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

