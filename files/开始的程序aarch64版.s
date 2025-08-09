//------------------------
.section .data            // 数据段，养字符串的地方
  msg: .ascii "\nhello 汇编 ，hello 二进制 ，hello hugo ，我来了 ，好吧，我又走了\n\n"                                                    // 我要说的全在这
  len = . -msg
  msg0: .ascii "挖槽，这不就是高级语言的内部模块化吗，哦买嘎？\n\n"               //牛逼啊我超😂😂😂😎
  len0 = . -msg0
  msg1: .ascii "靠，这不妥妥的高级语言吗\n\n"
  len1 = . -msg1          //必须狠狠的吐槽一波😎
  msg2: .ascii "❌⚠︎⚠️⚠️⚠️aarch64学习资料中断，无法继续，请待后续加载⛽⛽⛽\n\n"   //还有这里
  len2 = . -msg2          // 长度，别动，动了就错位
//先搞个时间玩玩😎--------
.align 3
ms:
  .quad 8                 //秒
  .quad 0                 //还是纳秒😎
  .quad 2                 //秒~~~😇
  .quad 0                 //又是纳秒😂

.align 3
buf:
  .quad 8 
  .quad 0 
  .quad 2 
  .quad 0
//------------------------

.section .bss             // 空着，但得留，仪式感
  .balign 16              //现在有了😂😂
stack_bottom:
  .skip 8192              //既然建了当然要给内存啊😡
stack_top:
//------------------------

.section .text            // 正文开始，干活！
  .global _start          // 告诉链接器：入口在这儿！
_start:                   // 真正开跑的地方

//------------------------

  //初始化指针
  ldr x3, =stack_top
  mov sp, x3
//------------------------

  bl write_tim            //这里也放一个😂

  mov x0, #1              // 1 = stdout，写给屏幕看的
  ldr x1, = msg           // msg 地址丢进去
  mov x2, #len            // 多长？len 说了算
  mov x8, #64             // Linux 的 write 系统调用号
  svc #0                  // 喊内核干活！

//输出实验----暂不介绍--😉
  mov x0, #1 
  mov x1, #0
  mov x8, #85             //某愣甘多，仲系系统调用咋
  svc #0
  mov x19, x0 

  mov x0, x19
  mov x1, #0 
  ldr x2, = ms 
  mov x3, #0 
  mov x8, #86              //太多了，这几段也给他封了😎
  svc #0 

  mov x0, x19
  ldr x1, =buf
  mov x2, #8 
  mov x8, #63
  svc #0

//模块化调用实验-----------
  ldr x1, = msg0
  mov x2, #len0
  bl write_msg
  bl write_tim
//-------------------------

  ldr x1, = msg1          // ┓
  mov x2, #len1           // ┣>☞len和msg可以自定义😱？
  bl write_msg            // ┛
  bl write_tim

//同上上面的（也就是代码段开始的地方），打印第二段-----
  ldr x1, = msg2         
  mov x2, #len2
  bl write_msg
  brk #2333               //哇得发颗，2333，什么玩意
//------------------------

  mov x0, #0              // 退出码，0 表示“我没事”
  mov x8, #93             // Linux 的 exit 系统调用号
  svc #0                  // 拜拜了您内

//-封装区！！！----------------------------------

//看到某个建议我把一段常用的指令封装起来，于是，我封装了
write_msg:
  stp x29, x30, [sp, #-16]!                                                       //保留x30(返回地址)和x29（必要）
  mov x29, sp             //建立帧指针（可选哦）
  mov x0, #1
  mov x8, #64
  svc #0
  ldp x29, x30, [sp], #16 //恢复寄存器（必要）
  ret

//现在可以说了😂---------------------------
write_tim:
  stp x29, x30, [sp, #-16]!                                                        //还是一样，保存现场
  mov x29, sp              //创建帧指针，一定要记得加上这些哦😎（你也可以试试不加）
  mov x0, #1               //把新成员#1放x0
  mov x1, #0               //一样的把#0放x1
  mov x8, #85              //把新成员#85放x8，即timerfd_create
  svc #0                   //别忘了不svc新成员就不会进来😎
  mov x19, x0              //把返回值放到x19
                           //fb
  mov x0, x19              //我猜你应该想到了，哦吼没错😉，把保存的值再拉回来
  mov x1, #0               //一样，还是给新成员房子
  ldr x2, = ms             //设置时间，记得先在data或bss先定义
  mov x3, #0               //开门，听到没有
  mov x8, #86              //随便再把timerfd_settime拉进来，即#86
  svc #0                   //拉新员工别忘了发邀请函☺️

  mov x0, x19              //我就多说了
  ldr x1, =buf             //不说了……………………
  mov x2, #8               //读取八字节↑↑↑↑
  mov x8, #63              //…………………………||||
  svc #0                   //-----------|||
  ldp x29, x30, [sp], #16  //~~~~~~~~~~~~||
  ret                      //=============|

//-封装区！！！----------------------------------
