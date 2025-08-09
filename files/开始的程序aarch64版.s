.section .data            // 数据段，养字符串的地方
  msg: .ascii "hello 汇编 ，hello 二进制 ，hello hugo ，我来了 ，好吧，我又走了\n"  // 我要说的全在这
  len = . -msg
  msg0: .ascii "挖槽，这不就内部模块化吗？"                                          //😂😂😂😎
  len0 = . -msg0
  msg1: .ascii "aarch64学习资料中断，无法继续，请待后续加载\n"                       //还有这里
  len1 = . -msg1          // 长度，别动，动了就错位

.section .bss             // 空着，但得留，仪式感
// 现在有了😂-------------
  .balign 16
stack_bottom:
  .skip 8192
stack_top:
//------------------------
.section .text            // 正文开始，干活！
  .global _start          // 告诉链接器：入口在这儿！
_start:                   // 真正开跑的地方

  mov x0, #1              // 1 = stdout，写给屏幕看的
  ldr x1, = msg           // msg 地址丢进去
  mov x2, #len            // 多长？len 说了算
  mov x8, #64             // Linux 的 write 系统调用号
  svc #0                  // 喊内核干活！

//模块化调用实验-----------
  mov x0, #1
  ldr x1, = msg0
  mov x2, #len0
  bl write_msg
//-------------------------

//同上上面的（也就是代码段开始的地方），打印第二段---------
  mov x0, #1
  ldr x1, = msg1
  mov x2, #len1
  mov x8, #64
  svc #0

//看到某个建议我把一段常用的指令封装起来，于是，我封装了---
write_msg:
  stp x29, x30, [sp, #-16]!                                                          //保留x30(返回地址)和x29（可选栈帧）
  mov x29, sp             //建立帧指针
  mov x8, #64
  svc #0
  ldp x29, x30, [sp], #16 //恢复寄存器
  ret
//---------------------------------------------------------

  mov x0, #0              // 退出码，0 表示“我没事”
  mov x8, #93             // Linux 的 exit 系统调用号
  svc #0                  // 拜拜了您内

