//---data段---------------
.section .data
  msg: .ascii "\n\n我记得上一个文件有个比较大线性控制流所以我把她搬过来了，并且决定进化一下🥰\n\n"
  len = . -msg
  msg1: .ascii "\n\n不过在此之前我们应该做点别的\n\n"
  len1 = . -msg1
  msg2: .ascii "\n\n来吧，展示\n\n"
  len2 =. -msg2
  hi: .ascii "hello\n"
  hilen = . -hi
  err: .ascii "\n\n错错错，重来\n\n"
  errlen = . -err
  pas: .ascii "\n\n啊哈，看来对了呢\n\n"
  paslen = . -pas
  kerz: .ascii "\n看来这对你来说并不难，那就上难度😎\n"
  kerzlen = . -kerz      //虽然我自己都不懂🤣
  jisir: .ascii "\n756875685×1235888955÷756875685等于多少\n"
  jisirlen = . -jisir    //我看你怎么算😎
  der: .ascii "1235888955\n"
  derlen = . -der
  baibai: .ascii "好吧，看来你赢了，拜拜👋👋🥳"
  baibailen = . -baibai  //谁让对面是科技与狠活🌚

.align 3
ms:
  .quad 1,3,1,4          //给汇编表个白怎么了😡
//---bss段----------------
.section .bss
  .balign 64
my64k:
  .skip 65536            //上次说了，留着以后用

  .equ my_stack_len, 1024
  .equ my_read_len, 4096

  .equ my_stack_off, 0   //这不就用上了吗？😎
  .equ my_read_off, my_stack_off + my_stack_len
//---bss------------------
//-text段加入程序口段-----
.section .text
.global _start
_start:                  //还有一件事，_start可以随便改 ，只要给ld加上-e就行
  ldr x0, =my64k + my_stack_off + my_stack_len
  mov sp, x0             //换一种初始化方式😎

  .equ sys_write, 64     //.equ是因为方便记忆
  .equ sys_exit, 93      //上一个文件注释了我就不注释了😎
  .equ sys_timerfd_c, 85
  .equ sys_timerfd_s, 86
  .equ sys_read, 63

  bl tim 
  ldr x1, =msg
  ldr x2, =len
  bl write_txt
  bl tim
  
  ldr x1, =msg1
  ldr x2, =len1
  bl write_txt
  bl tim

  ldr x1, =msg2
  ldr x2, =len2
  bl write_txt
  bl tim

  ldr x6, =hi
  ldr x7, =hilen
  bl loop_cmp_g

  ldr x1, =kerz
  ldr x2, =kerzlen
  bl write_txt
  bl tim

  ldr x1, =jisir
  ldr x2, =jisirlen
  bl write_txt
  bl tim

  ldr x6, =der
  ldr x7, =derlen
  bl loop_cmp_g
  bl tim

  ldr x1, =baibai
  ldr x2, =baibailen
  bl write_txt

//exit--------------------
  mov x0, #0
  mov x8, sys_exit
  svc #0
//子程序模块化阶段--------
write_txt:              //这一整串也可以自己看着办😉
  stp x29, x30, [sp, #-16]!                                                           //其实这里的空间可以在范围内自由分配
  mov x29, sp
  mov x0, #1
  mov x8, sys_write     // 用.equ定义的代替系统调用号 
  svc #0                //svc不能少
  ldp x29, x30, [sp],#16                                                              //还有一件事，记得恢复
  ret                   //一样的恢复不能少
tim:                    //都说了自己看着办
  stp x29, x30, [sp, #-32]!                                                           //别老看着-16，都说了自由发挥😤
  mov x29, sp
  mov x0, #1
  mov x1, #0
  mov x8, sys_timerfd_c
  svc #0
  mov x19, x0
  mov x0, x19
  mov x1, #0            //记不住最好查文档，不然会拔毛的
  ldr x2, =ms           //上次忘记说了，多指针参数别乱搞
  mov x3, #0            //😰😰😭😭😭😭😫😇
  mov x8, sys_timerfd_s
  svc #0
  mov x0, x19
  ldr x1, =ms
  mov x2, #8
  bl use_read
  ldp x29, x30, [sp], #32
  ret

cace_skip:
  stp x29, x30, [sp, #-16]!
  mov x29, sp
  adrp x1, my64k
  add x1, x1, :lo12:my64k
  add x1, x1, my_read_off
  mov x2, #my_read_len
  ldp x19, x20, [sp], #16
  ret
use_read:
  stp x29, x30, [sp, #-64]!                                                           //一会16，一会64，一会32
  mov x29, sp           //看到没，我就是玩😂
  bl cace_skip
  mov x8, sys_read
  svc #0
  ldp x29, x30, [sp], #64                                                             //别低于16就行，随便玩🥳
  ret

loop_cmp_g:
  stp x29, x30, [sp, #-16]!
  mov x29, sp
loop:
  mov x0, #0
  bl use_read
  cmp x0, #0
  beq no
  cmp x0, x7
  bne no
  mov x3, #0
cmp_loop:
  ldrb w4, [x1, x3]
  ldrb w5, [x6, x3]
  cmp w4, w5
  bne no
  add x3, x3, #1
  cmp x3, x7
  blt cmp_loop
  b yes
no:
  ldr x1, =err
  ldr x2, =errlen
  bl write_txt
  b loop
yes: 
  ldr x1, =pas
  ldr x2, =paslen
  bl write_txt
  ldp x29, x30, [sp], #16
  ret
