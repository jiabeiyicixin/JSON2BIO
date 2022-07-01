import json

with open("text1.json",encoding='utf-8',mode='r') as f:
    json_dic=json.load(f)
start=[]
end=[]
result=[]
enity=[]
lable=[]
n=0
content=json_dic["content"]
# print(content)
output=json_dic["outputs"]["annotation"]["T"]
# print(output)
# print(json_dic)
for dic in output:
    if dic:
        lable.append(dic["name"])
        start.append(dic["start"])
        end.append(dic["end"])
for i in range(len(start)):
    str=''
    for j in range(start[n],end[n]):
        str+=content[j]
    n=n+1
    enity.append(str)

if(len(enity)==len(lable)):
    for i,j in zip(enity,lable):
        result.append(i+" "+j)
print(result)
result=set(result)
        
with open("./result.txt",mode='w',encoding='utf-8') as file:
    for item in result:
        file.write(item)
        file.write("\n")

