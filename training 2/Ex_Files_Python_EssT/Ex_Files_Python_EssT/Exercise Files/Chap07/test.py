ports = [
    ['jhsjs',180,190],
    ['as',376,585],
    ['sdd',580,495]
]

# print(ports[2][-2])

def run(n:int):
    if n==0 or n==1:
        return 1
    else:
        return n*run(n-1)*run(n-2)\
        


def main():
    print(run(5))
if __name__ == '__main__':
    main()
