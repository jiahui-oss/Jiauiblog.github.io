#!usr/bin/env python3
import sys,os,time,threading,re,fractions,json,math
save = os.path.expanduser("./py1.json")
计算器 = {
    "+": (1, "L", "二元加"), "-": (1, "L", "二元减"),
    "×": (2, "L"), "÷": (2,"L"),
    "^": (4, "R"), "(": 0, ")": 999,
    "eE": "科学计数", "neg": (5, "R", "一元负"),
    "pos": (5, "R", "一元正"), "q":"退出"
}
prio = {k: v[0] for k, v in 计算器.items() if isinstance(v, tuple)}
assoc = {k: v[1] for k, v in 计算器.items() if isinstance(v, tuple)}
prio['*'] = 2;  assoc['*'] = 'L'
prio['/'] = 2;  assoc['/'] = 'L'
prio['**'] = 4; assoc['**'] = 'R'
背包 = {}
人物 = {}
user_list = [计算器, 背包, 人物]
user_save=[user_list[1], user_list[2]]
a = "接入"
b = "抛弃"
c = "收起"
def o(a=0):
    return ' '.join(f"[{ch}]" for ch in user_list[a])
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
        try:
            if any(c in user_list[0] for c in l):
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
                        while j < leno and (l[j].isdigit() or l[j] == "."):
                            j += 1
                        if j < leno and l[j] in "eE":
                            j += 1
                            if j < leno and l[j] in "+-":
                                j += 1
                            while j < leno and l[j].isdigit():
                                j += 1
                        try:
                            num = float(l[i:j])
                            t.append(num)
                        except ValueError:
                            raise ValueError(f"无效的数字格式: {l[i:j]}")
                        i = j
                        continue
                    if i + 1 < leno and l[i] == '*' and l[i + 1] == '*':
                        t.append('**')
                        i += 2
                        continue
                    if s in "+-*/()":
                        prev = l[i-1] if i > 0 else ''
                        is_unary = (i == 0) or (prev in "+-*/(" and prev != ")")
                        if s == '-' and is_unary:
                            t.append("neg")
                            i += 1
                            continue
                        elif s == '+' and (i == 0 or l[i-1] in "+-*/("):
                            t.append("pos") 
                            i += 1
                        else:
                            t.append(s)
                            i += 1
                        continue
                    raise ValueError(f"看看，看看，你在搞什么：{s!r} {i}\n\n简直糟糕透了")
                exp = "".join(str(f)for f in t)
                tst = []
                st = []
                for tok in t:
                    if isinstance(tok, float):
                        tst.append(tok)
                    elif tok in ['neg', 'pos']:
                        while st and st[-1] != '(' and prio[st[-1]] >= prio[tok]:
                            tst.append(st.pop())
                        st.append(tok)
                    elif tok == '**':
                        while st and st[-1] != '(' and (prio[st[-1]] > prio['**'] or (prio[st[-1]] == prio['**'] and assoc['**'] == 'L')):
                            tst.append(st.pop())
                        st.append('**')
                    elif tok in prio:
                        while st and st[-1] != "(" and (prio[st[-1]] > prio[tok] or (prio[st[-1]] == prio[tok] and assoc[tok] == "L")):
                            tst.append(st.pop())
                        st.append(tok)
                    elif tok == "(":
                        st.append(tok)
                    elif tok == ")":
                        while st and st[-1] != "(":
                            tst.append(st.pop())
                        if st and st[-1] == "(":
                            st.pop()
                while st:
                    tst.append(st.pop())
                v = []
                for tok in tst:
                    if isinstance(tok, float):
                        v.append(tok)
                    elif tok == "neg":
                        if not v:
                            raise ValueError("操作数不足")
                        v.append(-v.pop())
                    elif tok == "pos":
                        if not v:
                            raise ValueError("操作数不足")
                        v.append(v.pop())
                    else:
                        if len(v) < 2:
                            raise ValueError("操作数不足")
                        b = v.pop()
                        a = v.pop()
                        v.append({"+": a+b, "-": a-b, "*": a*b, "/": a/b, "**": a**b}[tok])
                exo = str(v[0]) if v else 'NaN'
                tim(0.5)               
                print("\n\n正在连接超算枢纽")
                tim(0.5)
                clone(0.001)         
                tim(0.5)
                print("\n\n连接成功")
                tim(0.6)
                print("\n\n正在解析输入")
                tim(0.6)            
                clone(0.002)
                tim(0.6)
                print("\n\n解析完成")
                tim(0.7)
                print("\n\n正在遍历")
                tim(0.7)
                clone(0.003)
                tim(0.7)
                print("\n\n遍历完成")
                tim(0.8)
                print("\n\n正在计算")
                tim(0.8)
                clone(0.004)
                tim(0.8)
                print("\n\n计算完成")
                tim(0.9)
                print(f"\n\n{read}\n\n")
                tim(0.9)
                print(f"{t}\n\n")
                tim(0.9)
                print(f"{tst}\n\n")
                tim(0.9)
                print(f"{v}\n\n")
                tim(0.9)
                print(f"{exp} = {exo}\n\n")
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
        except IndexError as ie:
            print(ie)
            print("我说什么来着")
            print("啊，对，去找驱动，修理😎")
            tim(5)
        except AttributeError as ae:
            print(ae)
            print("我早就推荐去web大厦了，你不信🤣")
def 对话0():
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
def 对话2():
    print("先收起来\n\n")
    print(link[1])
    tim(3)
    print("继续去别的地方看看吧\n\n")
    tim(1)
    print("对了，还没知道你叫什么呢")
    link[2]["姓名"]= input("姓名：")
    tim(1)
    link[2]["性别"]= input("性别：")
    tim(1)
    link[2]["年龄"]= input("年龄：")
    print("正在备注")
    tim()
    clone(0.6)
    print("备注完毕")
    tim()
    print(f"{o(2)}")
    tim()

if os.path.exists(save):
    user_save = json.load(open(save))
else:
    print("噢，没有记忆条？\n\n")
    print("web大厦提供有很多渠道，有不少便宜货，也有不少重量级的\n\n")
    print("你可以坐信道列车去看看\n\n")
    print("实在没钱，拾荒也可以😎\n\n")
    print("不过建议去枢纽中心找点活，但是单干可不好办😎\n\n")
    time.sleep(7)
对话0()
cal()
对话2()
while True:
    print(f"{o(1)}\n")
    read = input("输入：")

    print("🤗")
with open(save, "w") as f:
    json.dump(user_save, f, ensure_ascii = False, indent = 2)
