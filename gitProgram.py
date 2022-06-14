voc=[input().lower() for i in range(int(input()))]
#print(voc)
tex=[input().lower().split() for i in range(int(input()))]
#print(tex)
s=set()
for i in range(len(tex)):
    for j in range(len(tex[i])):
        if tex[i][j] not in voc:
            s.add(tex[i][j])
print(*s,sep='\n')