#파일열기
finput = open("article.txt","r")
lineCount = 1
for aline in finput:
    print("---[Line %d]----"%lineCount)
