# N과 M (8)

N, M = map(int, input().split())

Ns = sorted(map(int, input().split()))

def re(st, i, depth):
	if depth==M: 
	    print(st)
	    return
	for j, n in enumerate(Ns[i:]):
		re(f"{st} {n}", j+i, depth+1)

for i, n in enumerate(Ns):
	re(str(n), i, 1)