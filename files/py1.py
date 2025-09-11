#!usr/bin/env python3
import sys,os,time,threading,re,fractions,json,math
save = os.path.expanduser("./py1.json")

计算器 = {
    "+":(1,"L"), "-":(1,"L"),
    "×":(2,"L"), "÷":(2,"L"),
    "^":(3,"R"), "(":0, ")":999,
    "e/E":"科学计数", "q":"退出"
}
prio = {k: v[0] for k, v in 计算器.items() if isinstance(v, tuple)}
assoc = {k: v[1] for k, v in 计算器.items() if isinstance(v, tuple)}
#就地补*/
prio['*'] = 2;  assoc['*'] = 'L'
prio['/'] = 2;  assoc['/'] = 'L'
prio['**'] = 3; assoc['**'] = 'R'

背包 = {}
人物 = {}
link = [计算器, 背包, 人物]

a = "接入"
b = "抛弃"
c = "收起"

def o(a=0):
    return ' '.join(f"[{ch}]" for ch in link[a])
def op():
    #num = eval(exp)
    tim()               
    print("\n\n正在连接超算枢纽\n\n")
    tim(0.6)
    clone(0.007)         
    tim(1)
    print("\n\n连接成功，正在计算\n\n")
    tim(0.9)            
    clone(0.01)          
    print("计算成功\n\n")
    tim(0.8)            
    #print(f"{read} = {num}\n\n")
    #print(f"{exp} = {exo}")
def tim(byt=1.5):
    time.sleep(byt)
def klll():
    os.system("cls" if os.name == "nt" else "clear")
def clone(bye=0.08):
    total = 100
    for i in range(total + 1):
        prog = f"{i/total*100:.1f}%|{">"*int(i/2)}|{i}/{total}"
        klll()
        print(prog, end="\r", flush=True)       
        time.sleep(bye)
def cal():
    while True:
        print(f"{o()}\n")
        read = input("输入：")
        l = read
        l = l.replace("×", "*").replace("÷", "/").replace("^", "**")
        if l == "q":
            tim(1)
            print("\n\n正在断开连接\n\n")
            tim(1)
            clone()
            tim(1)
            print("\n\n成功终断\n\n")
            break
        try:#原版代码量接近150行，所以决定用eval和re
            if any(c in link[0] for c in l):
                i = 0
                leno = len(l)
                t = []
                while i < leno:
                    s = l[i]
                    if s.isspace():
                        i += 1
                        continue
                    if s.isdigit() or s == ".":
                        j = i
                        while j < leno and (l[j].isdigit() or l[j] == "." ):
                            j += 1
                        if j < leno and l[j] in "eE":
                            j += 1
                            if j < leno and l[j] in "+-":
                                j += 1
                            while j < leno and l[j].isdigit():
                                j += 1
                        t.append(float(l[i:j]))
                        i = j
                        continue
                    if s in "+-*/()":
                        t.append(s)
                        i += 1
                        continue
                    raise ValueError(f"看看，看看，你在搞什么：{c!r} {i}\n\n简直糟糕透了")
                exp = "".join(str(f)for f in t)
                tst = []
                st = []
                for tok in t:
                    if isinstance(tok, float):
                        tst.append(tok)
                    elif tok in prio:
                        while st and st [-1] != "(" and (prio[st[-1]] > prio[tok] or (prio[st[-1]] == prio[tok] and assoc[tok] == "L")):
                            tst.append(st.pop())
                        st.append(tok)
                    elif tok  == "(":
                        st.append(tok)
                    elif tok  == ")":
                        while st and st[-1] != "(":
                            tst.append(st.pop())
                        st.pop()
                while st:
                    tst.append(st.pop())
                v = []
                for tok in tst:
                    if isinstance(tok, float):
                        v.append(tok)
                    else:
                        b = v.pop()
                        a = v.pop()
                        v.append({"+":a+b, "-":a-b,"*":a*b, "/":a/b}[tok])
                exo = str(v[0]) if v else 'NaN'
                #print(f"{exp} = {exo}")
                op()
                print(f"\n\n{t}\n\n")
                tim()
                print(f"{tst}\n\n")
                tim()
                print(f"{exp} = {exo}\n\n")
#还是补了一个🤣🤣🤣
            elif l == "收起":
                link[1]["终端机<可扩展款>"] = cal
        except ValueError as ve:
            tim()
            print(ve)
            print("\n\n抱歉，枢纽中心缺失驱动\n\n")
            tim()
            print("嘿，我记得枢纽中心好像发布有关于驱动收集的通报，你可以到节点中转站乘坐管道列车去看看😎\n\n")
            tim()
            print("说不定能接到大单子呢😄\n\n")
            tim(5)                      
            klll()
        except SyntaxError as se:
            tim()
            print(se)
            print("\n\n嘿，你好像不太懂算式")
            tim()
            print("\n\n不过没关系")
            tim(0.7)
            print("\n\n因为web大厦会经常更新大量知识，重点是有大量免费的知识，你可以到节点中转站乘坐信道列车去看看😎")
            tim(5)
            klll()
        except NameError as ne:
            tim()
            print(ne)
            print("\n\n看来你有很多不懂的🤓")
            tim()
            print("\n\n不过没关系")             
            tim(0.7)                            
            print("\n\n因为web大厦会经常更新大量知识，重点是有大量免费的知识，你可以到节点中转站乘坐信道列车去看看😎")                              
            tim(5)                     
            klll()

if os.path.exists(save):
    link[1] = json.load(open(save))
    link[2] = json.load(open(save))
else:
    print("噢，没有记忆条？\n\n")
    print("web大厦提供有很多渠道，有不少便宜货，也有不少重量级的\n\n")
    print("你可以坐信道列车去看看\n\n")
    print("实在没钱，拾荒也可以😎\n\n")
    print("不过建议去枢纽中心找点活，但是单干可不好办😎\n\n")
    time.sleep(7)

tim()
klll()
tim()
print("\n\n嘿，你好啊!\n\n")
tim()
print("好吧，忘了😭\n\n")
tim()
print("先搞点东西回忆一下吧😭\n\n")
tim()
print("等等，这是………终端？\n\n")
tim(2)

while True:
    print(f"{a}\n\n{b}\n\n")
    read = input("你不会是想……😱:")
    if read == a:
        tim()
        klll()
        print("\n\n正在为你连接脑机接口")
        tim(1)
        klll()
        clone()
        tim(1)
        print("\n\n脑机接口链接完毕\n\n")
        tim(1)
        klll()
        print("欢迎进入计算机世界\n\n")
        tim()
        break
    elif read == b:
        break
        print("\n\n感觉不安全，还是丢了吧（我走）\n\n")
        tim(1)
        print("说不定能捡到比这更好的东西😤\n\n")
        sys.exit()
    else:
        tim()
        print("\n\n不对不对\n\n")
        tim()
        print("你不会是想找其他东西吧\n\n")
        tim()
        print("放心，这里方圆百里基本都没什么东西可以捡😎\n\n")

cal()
print("先收起来\n\n")
print(link[1])
tim(3)
print("继续去别的地方看看吧\n\n")
tim(1)
print("对了，还没知道你叫什么呢")
n=input("姓名：")
link[2]["姓名"]=n
tim(1)
s=input("性别：")
link[2]["性别"]=s
tim(1)
print(link[2])
while True:
    print(f"{o(1)}\n")
    read = input("输入：")

    print("🤗")
with open(save, "w") as f:
    json.dump(link[1], f)
    json.dump(link[2], f)
