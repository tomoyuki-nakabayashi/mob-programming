
with open("ics.txt", "r") as file:
  y=""
  for line in file:
    y+=line
    
  print("y:"+y)
    

# xとyを比較して、差を表示する
# 一致した場合は、空文字
# 完全に違う場合は、y
def diff(x, y):
  # 2文字以上で比較
  # 比較対象の文字列のi-j
  
  if(x in y):
    y=y.replace(x, " "*len(x))
  print("diff:" + y)
  return y



x = "abc"
#y = "bbbaaab"

# 複数行に対応したい
# forで1行ごと読み込んでdiffをとる
for i in range(len(x),0,-1):
  print("")
  print("target:"+ x[0:i])
  #print("diff" + str(i))
  y = diff(x[0:i], y)
  
  print(y)
    
  


    
    
