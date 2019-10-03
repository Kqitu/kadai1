me=list(map(int,input().split()))
n=int(input())
for i in range(n):
    enemy=list(map(int,input().split()))
    sdis=abs(me[0]-enemy[0])
    swid=(me[2]/2)+(enemy[2]/2)
    
    vdis=abs(me[1]-enemy[1])
    vhei=(me[3]/2)+(enemy[3]/2)
    if sdis<swid and vdis<vhei:
        print('“G‹@'+str(i+1)+'‚ª“–‚½‚è')