# 입력자료 처리 조건
# 0. 파일명을 입력받아 처리시작
# 1. 모든 단어는 소문자로 통일하며 처리한다.
# 2. 알파벳과 숫자를 제외한 모든 문장부호(. ! [ ])는 모두 제거한다
# 3. 파일에 등장하는 단어는 빈 칸으로만 구분한다.

# 출력조건
# 0. 출력할 파일명도 입력받아 출력한다.
# 1. 등장한 단어들을 알파벳 순으로 표시한다.
# 2. 등장한 단어의 등장 횟수를 옆에 표시한다.

# fileName = input("파일 이름 입력 : ")
# f = open(fileName,"r")

def fileRead(read, name):
    readFile = open(name,"r")
    read = readFile.read()
    readFile.close()
    return read
def fileWrite(name, content):
    writeFile = open(name,"w")
    writeFile.write(content)
    writeFile.close()


def findAdd(d, nw):
    if nw in d:
        d[nw] += 1
    else:
        d[nw] = 1
#=========================================================================================
content = ""
content = fileRead(content, "newsContent.txt")
content = content.lower()

# print(content)
# print("="*100)
word={}
delWord="![]123456789(),-.;\n"
for x in range(len(delWord)):
    content = content.replace(delWord[x]," ")

content = content.split(" ")
while '' in content:
    content.remove('')

for i in range(len(content)):
    findAdd(word,content[i])
print(word)

print(word.keys())
print(word.values())
print(list(word.keys(), word.values()))
# print(list(word.keys(), word.values()))