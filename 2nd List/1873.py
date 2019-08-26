n = int(input())
tryouts = ['tesoura', 'papel', 'lagarto', 'papel', 'pedra', 'spock', 'pedra', 'lagarto', 'tesoura',
            'lagarto', 'spock', 'papel', 'spock', 'tesoura', 'pedra']

for i in range(n):
    r, s = input().split()
    if (r == s):
        print("empate")
    else:
        win = "sheldon"
        for j in range(0,len(tryouts),3):
            if(r == tryouts[j] and (s == tryouts[j+1] or s == tryouts[j+2])):
                win = "rajesh"
        print(win)