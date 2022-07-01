import json
with open("text1.json", encoding='utf-8', mode='r') as f:
    json_dic = json.load(f)
start = []
end = []
result = []
enity = []
lable = []

content = json_dic["content"]
content=str(content)
content.strip("\n").strip(" ")
output = json_dic["outputs"]["annotation"]["T"]
for dic in output:
    if dic:
        lable.append(dic["name"])
        start.append(dic["start"])
        end.append(dic["end"])
i = 0
j = 0
n = 0
print(len(lable),len(start),len(end))
with open("./result.txt", mode='w', encoding='utf-8') as file:
    while(i<len(content)):
        item=content[i]
        if item=="\n":
            i=i+1
            continue
        if item==" ":
            i=i+1
            continue
        if item=="。":
            file.write(item+" "+"O"+"\n")
            file.write("\n")
            i=i+1
            continue

        j=0
        flag=0
        while(j<len(start)):
            if i==start[j]:
                flag=1
                file.write(content[i] + " " + "B-" + lable[j] + "\n")
                if start[j]+1==end[j]:
                    i=i+1
                    print(i)
                    break
                for n in range(start[j] + 1, end[j]):
                    print(n)
                    file.write(content[n] + " " + "I-" + lable[j] + "\n")
                i=n+1
            else:
                j=j+1
        if flag==0:
            file.write(item + " " + "O" + "\n")
            i = i + 1
print("i" , i)


