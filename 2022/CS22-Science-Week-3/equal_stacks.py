def get_min(s1,s2,s3):
    s = min(len(s1),len(s2),len(s3))
    if len(s1)==s:
        return s1
    elif len(s2)==s:
        return s2
    else:
        return s3

input()
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))
h3 = list(map(int,input().split()))
s1, s2, s3 = sum(h1), sum(h2), sum(h3)
while True:

    if s1==s2==s3:
        print(s1)
        break
    if s1>=s2 and s1>=s3:
        s1-=h1[0]
        h1.pop(0)
    elif s2>=s1 and s2>=s3:
        s2 -= h2[0]
        h2.pop(0)
    elif s3>=s1 and s3>=s2:
        s3 -= h3[0]
        h3.pop(0)
# h1 = sorted(h1)
# h2 = sorted(h2)
# h3 = sorted(h3)
# print(h1)
# s1,s2,s3 = [0],[0],[0]
# for i in range(max(len(h1),len(h2),len(h3))-1,-1,-1):
#     if i < len(h1):
#         s1.append(h1[i]+s1[-1])
#     if i < len(h2):
#         s2.append(h2[i]+s2[-1])
#     if i < len(h3):
#         s3.append(h3[i]+s3[-1])
# s = sorted(get_min(s1,s2,s3))
# for j in range(len(s)-1,-1,-1):
#     if s[j] in s1 and s[j] in s2 and s[j] in s3:
#         print(s[j])
#         break
# s1 = sorted(s1)
# s2 = sorted(s2)
# s3 = sorted(s3)
#
# #
# # print(s1)
# # print(s2)
# # print(s3)
# # s1,s2,s3 = -1,1,0
# # i,j,k=0,0,0
# # while s1!=s2 and s1!=s3 and s2!=s3:
# #     s1 = sum(h1[i:])
# #     s2 = sum(h2[j:])
# #     s3 = sum(h3[k:])
# #     target = min(s1,s2,s3)
# #     if s1>target:
# #         i+=1
# #     if s2> target:
# #         j+=1
# #     if s3 > target:
# #         k+=1
# # print(s1)