data = { "철수": 98, "영희": 80, "순이": 100, "돌이": 70}
sum=0
for k, v in data.items():
    print('%s%10d'%(k,v))
    sum += v
print("="*14)
print("평균%10.f"%(sum/len(data)))