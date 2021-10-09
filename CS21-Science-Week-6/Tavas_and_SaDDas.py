n = input()
bin_list = ["","0","1"]
# l = ["4","7"]
bin_n = ""
for i in range(2,len(n)+1):
    f = str("{:0"+str(i)+"d}") #format
    for j in range(0,2**i):
        bin_list.append(f.format(int(bin(j)[2:])))

for i in n:
    if i == '4':
        bin_n+="0"
    elif i == "7":
        bin_n+="1"
print(bin_list.index(bin_n))
