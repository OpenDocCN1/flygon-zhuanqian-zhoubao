# 搞懂WebAssembly，给AI写代码补上这块关键拼图
作者：龙哥

大家好，我是龙哥。以前在大厂写代码写了六年，现在在SCAI实验室折腾Web出海项目。今天这篇文章的起因，是实验室里有些伙伴做项目时碰上了wasm，但之前完全没接触过。这让我觉得，确实该给零基础的朋友们好好讲讲这块内容。

最近“Web出海”是赚钱圈的热门方向。不少没有技术背景的圈友，靠着AI也做出了像模像样的网站。但随着项目越做越深，有些底层知识还是得补上。WebAssembly如今在Web开发生态里的地位挺关键的，等你开发到一定阶段，总会在某个节点和它碰面。

比方说，你的网站要是涉及视频剪辑、音频处理、图片编辑、语音识别这类功能，那大概率要考虑wasm了。

现在AI能帮你写代码，但很多关键决策得你自己先想明白，再告诉AI怎么做。看完这篇文章你就懂了。市面上讲wasm的教程都太专业，非程序员根本看不进去。我这篇就是个保姆级的入门指南，专门给你补上这块信息差。

这篇教程是写给谁的呢？主要是那些没有程序员背景，但正在靠AI开发网站的朋友。所以呢，一些特别技术化的细节我就不展开了，那些交给AI就行，我会告诉你怎么跟AI提需求。不过，你得先会做个简单网站，比如跟过Web航海或者深海圈那种程度。不需要你懂多深的技术，但至少得知道JavaScript、NPM、Vercel是干嘛的。

这篇文章会聊这些内容：

- 用大白话讲明白wasm是什么
- 什么情况下该用wasm
- 什么情况下不该用wasm
- 具体怎么用wasm
- wasm未来可能的应用场景

#### 另外，我在SCAI实验室分享时的录屏也放在文末了。

# wasm到底是什么？

WebAssembly，简称wasm，你可以把它理解成一种跑在浏览器里的低级编程语言。

## 编程语言也分两类

![](img/336a84ada0d21935d69cb056658983d7.png)

一类是编译型语言，它会提前把高级语言翻译成机器码，所以真正运行的时候直接执行机器码，那速度自然就快。

另一类是解释型语言，它得在运行的时候才一步步翻译执行，所以多了一道编译的工序，速度自然就慢一些。

咱们开发网站用的JavaScript，就是典型的解释型语言。要是遇上计算量特别大的任务，它的速度会比编译型语言慢上整整一个数量级。所以浏览器环境里，太需要一种计算效率远超JS的语言了。

传统的电脑上有汇编语言（Assembly），那是一种低级语言，能直接跟硬件打交道（你看雷军当年写的代码就知道了），所以跑起来特别快。后来Web端也搞出了类似的WebAssembly。

再一个，几乎主流编程语言都能编译成WebAssembly。这里就体现出wasm的另一个优势了——它能直接借用其他语言现成的库。JavaScript再怎么说也就一种语言，很多场景下，它根本找不到好用的库来用。

![](img/0a2c60f9dc3f5f826df6d60faa0151c6.png)

### 哪些任务算“计算密集型”？

下面列一些典型场景，你要是没技术背景，就看第一列，大概了解它擅长干嘛就行。里面有专业名词也不用管。

### 小彩蛋：雷军1994年写的代码（汇编语言）

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
;
; RI.ASM Revision 2.12 [ July 12, 1994 ]
Revision equ 'V2.12 '
;
;
;
;  RAMinit Release 2.0 
;  Copyright (c) 1989-1994 by Yellow Rose Software Co.
;  Written by Mr. Leijun
;
;  Function:
;  Press HotKey to remove all TSR program after this program
;
;

; ..........................................................................
; Removed Softwares by RI:
; SPDOS v6.0F, WPS v3.0F
; Game Busters III, IV
; NETX ( Novell 3.11 )
; PC-CACHE
; Norton Cache
; Microsoft SmartDrv
; SideKick 1.56A
; MOUSE Driver
; Crazy (Monochrome simulate CGA program)
; RAMBIOS v2.0
; 386MAX Version 6.01
; ..........................................................................
; No cancel softwares:
; Windows 3.1 MSD
;
; No removed TSR softwares:
; MS-DOS fastopen
; Buffers, Files ... (QEMM 6.0)
; QCache (386MAX 6.01)
; ..........................................................................
;
COMMENT

V2.04 Use mouse driver software reset function to initiation mouse
2/17/1993 by Mr. Lei and Mr. Feng
V2.05 RI cannot work in Windows DOS prompt
3/9/1993 by Mr. Lei
V2.06 1\. When XMS cannot allocate 1K memory, RI halts.
2\. RI repeat deallocates EMS memory.
V2.07 HotKey Setup Error
4/25/1993 by Mr. Lei
V2.08 KB Buffer
V2.10 1\. Release high memory blocks (EMM386 QEMM386 S-ICE 386MAX)
2\. RI copies flag
V2.12 1\. Exists a critical error in Init 8259 procedure
2\. Save [40:F0--FF] user data area

dosseg
.model tiny
.code
locals @@
org 100h

Start: jmp Main
org 103h

True equ 1
False equ 0
MaxHandles equ 100h

INT3 macro
out 0ffh,al
endm
;
; HotKey Status Test Var
; --------------- ---------------
;
; 7 6 5 4 3 2 1 0 417 418 496
; . . x . x . . . Left Alt is pressed 8 2
; x . . . x . . . Right Alt is pressed 8 8
; . . . x . x . . Left Ctrl is pressed 4 1
; . x . . . x . . Right Ctrl is pressed 4 4
; . . . . . . x . Left Shift is pressed 2
; . . . . . . . x Right Shift is pressed 1
;
LeftAlt equ 00101000b
RightAlt equ 10001000b
LeftCtrl equ 00010100b
RightCtrl equ 01000100b
LeftShift equ 00000010b
RightShift equ 00000001b
HotKey db LeftCtrl or RightCtrl

DataBegin dw 0
NextDataSeg dw 0ffffh
oldInt2F_addr dw 0, 0
XMS_control dw 0, 0
Handle_begin dw 0
cvtOfs dw 0 ; DOS 3.0 equ 0 and above DOS 4.0 is 1
org 104h
db 0dh
db Revision
db ??date
db 26
org 114h
tsrLength dw 0
MachineID db 0FCh ; IBM PC/AT

AuxHotKey db 0 ; 2Dh ; 'X' Scan Code
AuxHotKeyName db 'X$ '
Power db True
Flag db '!'
Kbd102 db 0
NoFlag db 0
StopFlag db 1
DosEnv dw 0
WorkSeg dw 0
PrevDataSeg dw 0
Copies db '1'
old_8259 db 0 ; 21h port
db 0 ; a1h port

Status dw 0
XMSbit equ 00000001b
EMSbit equ 00000010b
SKbit equ 10000000b

GoINT1C: db 0eah
oldInt1C_addr dw 0, 0
newINT1C:
test cs:Status, SKbit
jnz GoINT1C
cmp cs:StopFlag, 0
jz @@0
;
; Mr. Lei 2/8/1993
; Problem: if WPS quit and reenter, old RI cann't control keyboard. ;
push ds
push ax
xor ax, ax
mov ds, ax
mov ax, ds:[94]
cmp ax, offset NewInt9
pop ax
pop ds
jnz GoINT1C
mov cs:StopFlag, 0

@@0: push ax
push ds
push es
xor ax, ax
mov ds, ax
mov es, ds:[94+2]
cmp word ptr es:[101h], 'IE' ; 'LEI'
jz @@1
cli
mov cs:StopFlag, 1
mov ax, ds:[94]
mov cs:oldINT9_addr2, ax
mov ax, ds:[94+2]
mov cs:oldINT9_addr2[2], ax
mov ds:[94], offset newINT9_2
mov ds:[94+2], cs
sti
@@1: pop es
pop ds
pop ax
jmp GoINT1C

; ----------------------------------------------------------------------
; INT2F Func
;
; AX = C0D7h Return RI segment in AX
; AX = C0D8h Removes all TSR programs after RI
; AX = C0D9h Removes all TSR programs include RI
; AX = C0DAh Removes all RI copies
; ----------------------------------------------------------------------

newINT2F:
cmp ax, 0c0d7h ; LEI Hanzi GB Code
jnz @@1
push cs
pop ax
iret
@@1: cmp ax, 0c0d7h+1
jnz @@2
jmp KeepSelf
@@2: cmp ax, 0c0d7h+2
jnz @@3
jmp NoKeepSelf
@@3: cmp ax, 0c0d7h+3
jnz @@9
mov cs:NextDataSeg, -1
mov cs:Copies, '1'
jmp NoKeepSelf
@@9: jmp dword ptr cs:oldInt2F_addr

CallInt9:
ret

newINT9_2:
mov cs:NoFlag, 1
pushf
db 9ah ; call far ptr oldint9_addr
oldInt9_Addr2 dw 0, 0
jmp newINT9_proc

newINT9:
pushf
db 9ah ; call far ptr oldint9_addr
oldInt9_Addr dw 0, 0 cmp cs:NoFlag, 0
jz newINT9_proc
mov cs:NoFlag, 0
iret
newINT9_proc:
cmp cs:Flag, '!' ; busy ?
jnz @@0
iret
@@0:
mov cs:Flag, '!' ; set busy flag
push ax ; cmp hot key
push bx
push es
mov ax,40h
mov es,ax

cmp cs:AuxHotKey, 0
jz @@_1
mov bx, es:[1ah]
cmp bx, es:[1ch]
jz @@10
push bx
mov bl, es:[bx+1]
cmp bl, cs:AuxHotKey
pop bx
jnz @@10
@@_1:
mov ah,es:[17h] ; test CTRL SHIFT ALT
mov al,cs:HotKey
push ax
and ax,0f0fh
cmp al,ah
pop ax
jnz @@10 cmp cs:Kbd102, True
jnz @@1
shr al, 1
shr al, 1
shr al, 1
shr al, 1
push ax
mov ah, es:[18h]
and ax, 303h
cmp al, ah
pop ax
jnz @@10
mov ah, es:[96h]
shr ax, 1
shr ax, 1
and ax, 303h
cmp al, ah
jnz @@10 cmp cs:AuxHotKey, 0
jz @@_3
inc bx
inc bx
cmp bx, 3eh
jb @@_2
mov bx, 1eh
@@_2:
mov es:[1ah], bx
@@_3:
call IsWinDos
or ax, ax
jz @@1
call Beep
@@10:
sti
pop es
pop bx
pop ax
mov cs:Flag, ' ' ; no busy
iret
@@1: ; OK
pop es
pop bx
pop ax

KeepSelf:
call RemoveTSR
push es
mov es,cs:WorkSeg
mov dx,es:tsrLength
mov di,dx
mov al,0h ; Aug 24, 1993
mov cx,100h
rep stosb
pop es
int 27h

NoKeepSelf:
mov ax,0e07h
int 10h
mov cs:clsStr, 47h ; Color (White in Red)
call RemoveTSR
dec cs:Copies
call RestoreSelfIntVec
push es
cmp cs:PrevDataSeg, 0
jz @@1
mov es, cs:PrevDataSeg
mov es:NextDataSeg, -1
@@1: pop es
mov ax, 4c00h
int 21h

; ---------------------------------------------------------------------------

IsWinDOS:
mov ax, 1600h
int 2fh
cmp al, 01h
jz @@9 cmp al, 0ffh
jz @@9 ; Windows/386 Version 2.X
cmp al, 00h
jz @@1 cmp al, 80h
jnz @@9 ; Windows 3 in enhanced mode
; Version number in AL/AH
@@1:
mov ax, 4680h
int 2fh
cmp al, 80h
jnz @@9
xor ax, ax
jmp @@10
@@9: mov ax, 1
@@10: ret

; -----------------------------------------------------------------------
RestoreSelfIntVec:
cmp Copies, '0'
jz @@0
ret
@@0:
cli
push cs
pop ds
xor ax, ax
mov es, ax
mov si, offset oldInt9_Addr
mov di, 94
movsw
movsw
mov si, offset oldInt2F_Addr
mov di, 2Fh4
movsw
movsw
mov si, offset oldInt1C_Addr
mov di, 1Ch4
movsw
movsw
sti
ret

; ------------- KERNEL PROGRAM ----------------------------------------------
RemoveTSR:
pop ax
cli ; Set stack
mov sp, cs
mov ss, sp
mov sp, 100h
sti
push ax

cmp cs:Power, True
jnz @@1
call Init8259
@@1:
push cs
pop ds
@@_0:
mov ax,ds:NextDataSeg
cmp ax, -1
jz @@_1
mov cs:PrevDataSeg, ds
mov ds, ax
jmp @@_0
@@_1: mov si,ds:DataBegin
mov cs:WorkSeg, ds
lodsw
cmp ax, 'XX'
jz @@_2
call Beep
ret
@@_2:
call RestoreEnvStr
call RestoreMCB ; restore current mcb
call CloseFiles
call RestorePort
call RestoreLEDs
call RestoreVecList ; Restore vectors list
call RestoreFloppyParam
cmp cs:Power, True
jnz @@2
call RestoreCVTchain ; Restore cvt chain
call RestoreMemoryManager
@@2:
call RestoreBiosData
call Enable8259
mov ah, 1 int 16h

call RestoreClockSpeed
call CloseSpeaker
call ResetDisk
call UpdateTime

call ClosePRN
mov bx,cs:WorkSeg
mov ah,50h
int 21h ; Set PSP segment
mov ax,3 int 10h ; Set display mode

call InitPRN
call InitMouse
mov al, cs:Copies
cmp al, '1'
ja @@_sh1
mov cs:ShowCopies, ''
jmp @@_sh2
@@_sh1: mov cs:ShowCopies, al
@@_sh2:
mov si, offset clsStr
call ColorPrintStr
mov cs:Flag, ' ' ; no busy
cmp Copies, '1'
jnz @@_end
mov cs:StopFlag, 0
@@_end:
call ClearKB_buffer
ret

Beep:
mov ax,0e07h
int 10h
ret

; #########################################################################

ClearKB_Buffer:
push es
push bx
mov bx, 0040h
mov es, bx
cli
mov bx, es:[1ah]
mov es:[1ch], bx
sti
pop bx
pop es
ret

Init8259:
; cmp cs:Copies, '1'
; jz @@1
; ret
@@1:
cmp cs:MachineID, 0fch
ja @@pc_xt
@@AT:
mov bx,870h ;
mov al,0 ;
out 0F1h,al ;
jcxz $+2
jcxz $+2
mov al,11h ; ICW1
out 0A0h,al
jcxz $+2
jcxz $+2
out 20h,al
jcxz $+2
jcxz $+2
mov al,bl ; ICW2
out 0A1h,al
jcxz $+2
jcxz $+2
mov al,bh
out 21h,al
jcxz $+2
jcxz $+2
mov al,2 ; ICW3
out 0A1h,al
jcxz $+2
jcxz $+2
mov al,4
out 21h,al
jcxz $+2
jcxz $+2
mov al,1 ; ICW4
out 0A1h,al
jcxz $+2
jcxz $+2
out 21h,al
jcxz $+2
jcxz $+2
mov al,0FFh ; OCW1
out 0A1h,al
jcxz $+2
jcxz $+2
out 21h,al
ret
@@PC_XT:
mov al,13h ; ICW1
out 20h,al
jcxz $+2
jcxz $+2
mov al,8 ; ICW2
out 21h,al
jcxz $+2
jcxz $+2
mov al,9 ; ICW4
out 21h,al
jcxz $+2
jcxz $+2
mov al,0FFh ; OCW1
out 21h,al
ret

Enable8259:
mov ax, word ptr cs:old_8259
out 021h,al
jcxz $+2
jcxz $+2
mov al,ah
out 0a1h,al ; DEC PC Bus Mouse
ret ; July 1994 by Mr. Lei

; -------------------------------------------------------------------------

RestoreBiosData:
lodsw
cmp ax, '--'
jz @@1
call Beep
ret
@@1: push es
push di
mov di, 40h
mov es, di

mov di, 10h
movsw
mov di, 0a8h ; [40h:a8h]
movsw
movsw
mov di, 49h
mov cx, 1dh
rep movsb

mov di, 0f0h ; User data
mov cx, 8
rep movsw

pop di
pop es
ret

; -------------------------------------------------------------------------

RestoreMCB:
push ds
push es
lodsw ; 'MZ'
@@0: lodsw
cmp ax, 'MM'
jz @@1
mov es,ax
xor di,di
movsb
movsw
movsw
inc ax
mov bx, ds
cmp ax, bx
jz @@10
mov byte ptr es:[8], 0 ; Aug 24, 1993
@@10: cmp byte ptr es:[0], 'Z'
jnz @@0
mov byte ptr es:[10h], 0
jmp @@0
@@1:
pop es
pop ds
ret

; -------------------------------------------------------------------------
CloseFiles:
mov ax, 5 ; Begin handle
push ds
push si
mov cx, 15 ; Max handle
sub cx, ax
inc cx
mov bx, ax
@@1: push bx
push cx
mov ah, 3eh
int 21h
pop cx
pop bx
inc bx
loop @@1
pop si
pop ds
ret

; -------------------------------------------------------------------------
RestorePort:
mov di, 40h ; restore port
mov es, di
xor di, di
mov cx, 8
rep movsw
ret

; -------------------------------------------------------------------------
RestoreLEDs:
lodsb
and al, 11110000b ; LED status
mov ah, es:[17h]
and ah, 00001111b
or ah, al
and ah, 0f0h ; Clear CTRL ALT SHIFT
mov es:[17h], ah
ret

; -------------------------------------------------------------------------
RestoreEnvStr:
lodsw
push si
push di
push ds
push es
mov es, cs:DosEnv
mov ds, ax
xor si, si
mov di, si
@@0: lodsb
or al, al
jnz @@1 cmp byte ptr ds:[si], 0
jz @@2
@@1: stosb
jmp @@0
@@2: stosb
stosb
pop es
pop ds
pop di
pop si
ret

; -----------------------------------------------------------------------
RestoreVecList:
xor ax,ax
mov di,ax
mov es,ax
mov cx,100h
@@0: lodsw
xchg dx, ax
lodsw
cmp dx, 'EL'
jnz @@1 cmp al, 'I'
jnz @@1
sub cl, ah
push cx
mov cl, ah
mov ax, es:[di-4]
mov dx, es:[di-2]
@@a: stosw
xchg ax, dx
stosw
xchg ax, dx
loop @@a
pop cx
or cx, cx
jz @@9
jmp @@0
@@1:
xchg ax, dx
stosw
xchg ax, dx
stosw
loop @@0
@@9:
ret

;----------------------------------------------------------------------------
RestoreFloppyParam: ; Mr. Lei 2/10/1992
push es
push ax
xor ax, ax
mov es, ax
mov byte ptr es:[525h], 2
pop ax
pop es
ret

;---------------------------------------------------------------------------
RestoreCVTchain:
lodsw
cmp ax, 'VC'
jz @@_0
call Beep
ret
@@_0:
push ax
push cx
push es

; -----------------------------------------------------------------
lodsw ; DPB
mov di, ax
lodsw
mov es, ax
@@1: lodsb
inc di
stosb
add di, cs:cvtOfs
add di, 10h
movsw
movsw
les di, es:[di+2]
cmp di, -1
jnz @@1

; -----------------------------------------------------------------
lodsw ; DCB
mov di, ax
lodsw
mov es, ax
xor ax, ax
dec ax
stosw

; -----------------------------------------------------------------
lodsw ; Device Driver Chain
mov di, ax
lodsw
mov es, ax
xor cx, cx
@@9: push di
mov cl, 5
rep movsw
pop di
les di, es:[di]
mov ax, di
inc ax
jnz @@9
pop es
pop cx
pop ax
ret

; ----------------------------------------------------------------------------
RestoreMemoryManager:
test cs:Status, XMSbit
jz @@1
call LoadXMSstatus
@@1:
test cs:Status, EMSbit
jz @@2
call LoadEMSstatus
@@2:
ret

LoadEMSstatus:
lodsw
cmp ax, 'ME'
jz @@_0
call Beep
ret
@@_0:
lodsw
mov cx, ax
xor dx, dx
@@_1: push ds
push si
push dx
push cx

@@0: cmp dx, ds:[si]
jz @@1
add si, 4
loop @@0

push cx
mov cx, 5
@@0: mov ah, 45h ; Deallocate Handle and Memory
int 67h
or ah, ah
jz @@1
loop @@0
@@1: pop cx

@@1:
pop cx
pop dx
pop si
pop ds
inc dx
cmp dx, 100h
jb @@_1
shl cx, 1
shl cx, 1
add si, cx
ret

LoadXMSstatus:
lodsw
cmp ax, 'MX'
jz @@_0
call Beep
ret
@@_0:
lodsw
mov cx, ax
jcxz @@5
@@1:
lodsw
mov dx, ax
@@2: push dx
mov ah, 0ah ; free
call dword ptr cs:xms_control
or ax, ax
pop dx
jnz @@4 cmp bl, 0abh
jnz @@4
push dx
mov ah, 0dh ; unlock
call dword ptr cs:xms_control
or ax, ax
pop dx
jmp @@2
@@4: loop @@1
@@5: ret
endp

; -----------------------------------------------------------------------
CloseSpeaker:
in al, 61h
and al, 0fch
out 61h, al
ret

; -----------------------------------------------------------------------
RestoreClockSpeed:
mov al, 00110110b
out 43h, al
xor ax, ax
out 40h, al
out 40h, al
ret

; -----------------------------------------------------------------------
ResetDisk:
xor ax, ax
xor dx, dx
int 13h ; Restore A
inc dx
int 13h ; Restore B
mov dl, 80h
int 13h ; Restore C
ret

; --------------------------------------------------------------------------
ClosePRN:
mov ah, 51h ; Get PSP seg
int 21h
mov es, bx
mov ax, es:[16h] ; Prev PSP seg
cmp ax, bx
jnz @@9
mov ax, 3e00h ; COMMAND
mov bx, 4 int 21h
@@9:
ret

InitPRN:
mov ax, 3e00h
mov bx, 4 ; PRN
int 21h
mov ax, 3d01h
mov dx, offset PRNname
push cs
pop ds
int 21h
ret
PRNname db 'PRN',0

InitMouse: ; 2/16/1993 by Mr. Lei
push es
xor ax, ax
mov es, ax
cmp word ptr es:[33h4+2], 0
jz @@0 cmp word ptr es:[33h4], 0
jz @@0
mov ax, 21h
int 33h ; Hook Mouse Interrupt
@@0: pop es
ret

; ------------- CMOS CLOCK set to System -----------------------------------
UpdateTime:
call GetRealTime
mov ah, 2dh
int 21h
ret

GetRealTime:
mov ah,2 int 1Ah
mov al,ch
call bcdxchg
mov ch,al
mov al,cl
call bcdxchg
mov cl,al
mov al,dh
call bcdxchg
mov dh,al
mov dl,0
ret

BCDxchg:
push ax
push cx
mov cl,4
shr al,cl
pop cx
mov bl,0Ah
mul bl
pop bx
and bl,0Fh
add al,bl
ret

; -----------------------------------------------------------------------
; Display string
ColorPrintStr:
lodsb
mov bh, al ; color
xor cx, cx
mov dx, 014fh
mov ax, 0600h
int 10h

mov ah, 02 ; GotoXY (0, 0)
xor dx, dx
mov bh, 0 int 10h
PrintStr:
push cs
pop ds
xor bx, bx
@@1: lodsb
cmp al, '$'
jz @@2
or al, al
jz @@2
mov ah, 0eh
int 10h
jmp short @@1
@@2: mov al, cs:clsStrcolor
mov cs:clsStr, al
ret

; -----------------------------------------------------------------------
Self dw 0
clsStrcolor db 17h
clsStr db 17h ; Color (White in Blue)
db ' RAMinit Version 2.12 (c) 1989-1994 by KingSoft Ltd. Mr. Leijun'
db 0dh,0ah
db ' ['
ShowCopies db ''
db '] Activate...',0ah,0dh,'$'

endTSR equ $
mcbList equ offset endTSR + 2 + 2
vecList equ mcbList + 710 + 2 + 10h + 1 + 400h
devLink equ vecList + 4 + 5  26 + 4 + 10  30h + 4
xmsList equ devLink + 2 + MaxHandles  2
emsList equ xmsList + 4 + 1024
crtMode equ emsList + 2 + 1Dh + 4 + 10h
tsrLen equ crtMode + 1
;
; DOS Environment Reserved by RI
; --------------------------------------------------
; Flag 'XX' 2 bytes
; Environment Segment 1 word
; Free MCBs <=710 bytes
; MCB segment 1 word
; MCB 5 bytes
; End flag 'MM' 1 word
; COM LPT ports 10h bytes
; LEDs status 1 bytes
; Packed vectors list <=400h bytes
; Flag 'CV' 2 bytes
; CVT First DPB pointer 4 bytes
; DPBs data <=526 bytes
; First DCB pointer 4 bytes
; Pointer to NUL 4 bytes
; All device driver datas <=30h10 bytes
; Flag 'XM' 2 bytes
; XMS free handle counter 2 bytes
; EMS free handle list <=100h4 bytes
; Flag 'EM' 2 bytes
; EMS free handle counter 2 bytes
; EMS free handle list <=1024 bytes
; EMS handle 1 word
; Number of pages 1 word
; Flag '--' 1 word
; Equipment List 1 word
; CRT 40:49h-66h 1dh bytes
; 40:A8h 1 dword
; BIOS User Data Area 40:F0--FF 10h bytes
; **
;
main: jmp main0

Print Macro Str
Lea dx, Str
call DisplayStr
endm

InstMsg db 'RAMinit Version 2.12 '
db 'Copyright (c) 1989-1994 by KingSoft Ltd. ',0dh,0ah,'$'
Msg0 db 'Already installed !',0dh,0ah,0ah
db 'For Help, type RI /?. ',0dh,0ah,'$'
Msg_0 db 0ah,'Residents a new RAMinit copy [y/n] ? $'
Msg_2 db 'OK, RI No.'
Msg_RI db '2'
db ' residents successful !', 0dh,0ah,'$'
Msg1 db 'Activate with: $'
KeyMsg db 'Right_Shift$'
db 'Left_Shift$ '
KMsg1 db 'Left_Ctrl$ '
db 'Left_Alt$ '
db 'Right_Ctrl$ '
db 'Right_Alt$ '
KMsg2 db 'Ctrl$ '
db 'Alt$ '
db 'Ctrl$ '
db 'Alt$ '
PlusMsg db ' + $'
crlf db 0dh,0ah,'$'

HelpMsg db 'Programmed by Mr. Leijun Dec 1992', 0dh,0ah,0ah
db 'Usage: RI [options]',0dh,0ah,0ah
db '/H,/? Display this screen',0dh,0ah
db '/CLS Removes all TSR programs after current RI',0dh,0ah
db '/RET Removes TSR programs include current RI',0dh,0ah
db '/NEW Residents a new data copy of current environment',0dh,0ah
db '/ALL Removes all RI copies and all other tsr programs',0dh,0ah
db '/Sxyy.. Define Hotkey x=AuxHotkey yy..=shift status',0dh,0ah
db ' x=auxiliary hotkey (default is X) ',0dh,0ah
db ' x equ 1 means need AuxHotkey',0dh,0ah
db ' yy..=shift status [CAScas]',0dh,0ah
db ' C: Left Ctrl A: Left Alt S: Left Shift',0dh,0ah
db ' c: Right Ctrl a: Right Alt s: Right Shift',0dh,0ah,0ah
db 'Example: RI /S1c means Hotkey is Right_Ctrl+X',0dh,0ah
db ' RI /S0Cc means HotKey is Left_Ctrl+Right_Ctrl',0dh,0ah
db ' RI /CLS equals simply press hotkey',0dh,0ah
db ' RI /RET Removes all TSRs after current RI and this RI',0dh,0ah
db 0ah
db 'Contact me for RAMinit problems: (01)2561155 Call 1997',0dh,0ah
db '$'
ErrMsg db 'ERROR: Invalid options !',0dh,0ah,0ah,'$'
WinErr db 7, 'Sorry, I cannot work in Windows DOS environment.',0dh,0ah,'$'
SetMsg db 7, 'Defines new Hotkey successful !',0dh,0ah,0ah,'$'
tsrOK db False

Main0:
cld
Print instMsg
call IsWinDos
or ax, ax
jz @@1
Print WinErr
mov ax, 4c00h
int 21h
@@1:
call HotKeyValid
mov cs:Status, 0
call EMS_test
call CmpDosVer
call CmpSideKick
call GetMachineID
call ModifyHotKeyPrompt

mov ax, 0c0d7h
int 2fh
mov es, ax
cmp word ptr es:[101h], 'IE' ; 'LEI'
jnz @@0
mov cs:Self, ax
@@0:
call CmdLine
call PrintHotKeyPrompt

cmp cs:tsrOK, true
jz @@2
call tsrReplyOK
@@2: cmp cs:tsrOK, true
jnz @@_2
call PrintCopies
@@_2:
mov word ptr cs:[100h], 'EL'
mov byte ptr cs:[102h], 'I'

push cs
pop es
push cs
pop ds
std
mov si, offset eof
mov cx, eof - offset Here
mov di, tsrLen
add di, cx
inc cx
rep movsb
cld
mov bx, tsrLen
jmp bx

Here:
mov ax,cs
mov es,ax
mov di,offset endTSR
mov cs:DataBegin, di
mov cs:NextDataSeg, -1
mov ax, 'XX'
stosw
in al, 0a1h
mov ah, al
in al, 21h
push ax
mov word ptr cs:old_8259, ax
xor ax, ax
out 21h,al ; CLI
call SaveOthers
call SetSelfInt
call BackupVecList
cmp cs:Power, true
jnz @@20
call BackupCVTchain
call BackupMemoryManager
@@20:
call BackupBiosData

sti
mov cs:Flag, ' ' ; no busy
mov cs:StopFlag, 0 ;

mov cs:tsrLength, di
call SetDosEnvSeg
cmp cs:Self, 0
jz @@29
push cs
pop ds
push cs
pop es
cld
mov cx, cs:tsrLength
mov si, cs:DataBegin
sub cx, si
mov di, 120h
mov cs:DataBegin, di
rep movsb
mov cs:tsrLength, di
@@29:
pop ax
out 21h, al ; STI
mov al, ah
out 0a1h, al
mov dx, cs:tsrLength
inc dx
int 27h

; ----------------------------------------------------------------------------
SetDosEnvSeg:
push ds
push es
mov ax, cs
@@10: mov es, ax
mov ax, es:[16h] ; Get father process psp segment
or ax, ax
jz @@11
mov bx, es
cmp ax, bx
jnz @@10
@@11:
mov es, word ptr es:[2ch] ; Get father process env segment
mov cs:DosEnv, es
pop es
pop ds
ret

; ----------------------------------------------------------------------------

SaveOthers:
mov ax, cs:[2ch] ; Env Seg
stosw
call backupMCB ; Current MCB
mov ax, 40h ; COM LPT Port
mov ds, ax
mov si, 0h
mov cx, 8
rep movsw

mov si, 17h ; LED status
lodsb
stosb
; call OpenLEDs
ret

; --------------------------------------------------------------------------
backupMCB:
mov ax, 'ZM'
stosw
push ds
push es
mov ah, 52h
int 21h ; Get MCB chain head
mov ax, es:[bx-2]
pop es
@@0: mov ds, ax
cmp byte ptr ds:[0], 'Z' ; End ?
jz @@20 cmp byte ptr ds:[0], 'M' ; Memory control block
jnz @@30 cmp word ptr ds:[3], 0 ; Nul mcb
jz @@10 cmp word ptr ds:[1], 0 ; Free MCB
jnz @@10
call SaveFreeMCB
@@10: inc ax
add ax, ds:[3]
jmp @@0
@@20:
call SaveFreeMCB
cmp ax, 0a000h
inc ax
jnb @@30
mov ax, 9fffh ; MS-DOS UMB
jmp @@0

@@30:
cmp ax, 0c000h ; 386MAX
ja @@90
mov ax, 0c020h
jmp @@0

@@90: ; Error ?
pop ds
mov ax, 'MM' ; Set MCB flag
stosw
ret

SaveFreeMCB:
stosw
xor si,si
movsb
movsw
movsw
ret
;
; push ax
; stosw
; xor si,si
; movsb
; movsw
; movsw
; pop ax
; cmp ax, 09fffh
; jnb @@3
; push ax
; push ds
; mov ds,ax
; cmp byte ptr ds:[0], 'M'
; pop ds
; pop ax
; jnz @@4
; mov ax, 09fffh ; MS-DOS UMB
; jmp @@0
; @@4: cmp ax, 0c000h
; ja @@3
; mov ax, 0c020h ; 386MAX
; jmp @@0
;
; --------------------------------------------------------------------------

OpenLEDs: push ax ; Open all LEDs
or al, 070h
mov ds:[17h], al
mov ah, 1 int 16h
mov cx, 4 ; Delay
@@20: push cx
xor cx, cx
@@21: loop @@21
pop cx
loop @@20
pop ax
mov ds:[17h], al
mov ah, 1 int 16h
ret

; --------------------------------------------------------------------------
SetSelfInt:
push es
push di

cmp cs:self, 0
jnz @@1
push cs
pop ds
mov ax,3509h
int 21h
mov word ptr cs:oldInt9_addr,bx
mov word ptr cs:oldInt9_addr[2],es
mov dx,offset NewInt9
mov ax,2509h
int 21h

mov ax,352Fh
int 21h
mov word ptr cs:oldInt2F_addr,bx
mov word ptr cs:oldInt2F_addr[2],es
mov dx,offset newInt2F
mov ax,252Fh
int 21h

mov ax,351Ch
int 21h
mov word ptr cs:oldInt1C_addr,bx
mov word ptr cs:oldInt1C_addr[2],es
mov dx,offset newInt1C
mov ax,251ch
int 21h
cli
jmp @@2
@@1:
mov es, cs:Self
inc es:Copies
@@_0: cmp es:NextDataSeg, -1
jz @@_1
mov es, es:NextDataSeg
jmp @@_0
@@_1: mov es:NextDataSeg, cs
@@2:
pop di
pop es
ret

; -----------------------------------------------------------------------
SaveCounter:
mov word ptr es:[di], 'EL'
mov byte ptr es:[di+2], 'I'
mov byte ptr es:[di+3], bl
xor bx, bx
add di, 4
ret

; -----------------------------------------------------------------------
DisplayStr: push cs
pop ds
mov ah, 9 int 21h
ret

; -----------------------------------------------------------------------
CmdLine:
push cs
pop ds
xor ax, ax
mov si, 80h
lodsb
or al, al
jnz @@1
ret
@@1:
mov cx, ax
dec ax
push ax
push si
@@0: lodsb
cmp al, ' '
jz @@0 cmp al, '/'
jnz @@2
lodsb
cmp al, 'S'
jz @@_2
cmp al, 's'
jnz @@2
@@_2:
call SetHotKey
Print SetMsg
mov ax, 4c00h
int 21h
@@2:
pop si
pop ax
push ax
push si
@@_3: lodsb
cmp al, 'A'
jb @@3 cmp al, 'Z'
ja @@3
add byte ptr ds:[si-1],20h ; DownCase
@@3: loop @@_3
pop si
pop cx

add si, cx
lodsb
cmp al, 's' ; CLS
jnz @@5 cmp word ptr ds:[si-3], 'lc'
jnz @@5 cmp cs:Self, 0
jz @Err
mov ax, 0c0d7h+1 int 2fh

@@5: cmp al, 'h' ; HELP
jz @help
cmp al, '?'
jz @help
cmp al, 't' ; RET
jnz @@6 cmp word ptr ds:[si-3], 'er'
jnz @@6
@@7:
cmp cs:Self, 0
jz @Err
mov ax, 0c0d7h+2 int 2fh
@@6: cmp al, 'w' ; NEW
jnz @@8 cmp word ptr ds:[si-3], 'en'
jnz @@8
mov cs:tsrOK, true
ret
@@8:
cmp al, 'l' ; ALL
jnz @@9 cmp word ptr ds:[si-3], 'la'
jnz @@9
mov ax, 0c0d7h+3 int 2fh
@@9:
cmp al, ' '
jnz @Err
ret

@Err:
Print ErrMsg
@help:
Print HelpMsg
mov ax, 4c00h
int 21h

;---------------------------------------------------------------------------
tsrReplyOK:
cmp cs:Self, 0
jz @@1
Print Msg0

push es
mov ax, cs:Self
@@_10: mov es, ax
mov ax, es:NextDataSeg
cmp ax, -1
jnz @@_10
mov ax, es

@@_0: push ax
dec ax
mov es, ax
mov bx, es:[3]
pop ax

add ax, bx
inc ax
mov es, ax
cmp word ptr es:[0], 'OC'
jz @@_0

mov bx, cs
cmp ax, bx
pop es
jz @@2
Print Msg_0
mov ah, 1 int 21h

push ax
Print crlf
pop ax

cmp al, 'y'
jz @@3 cmp al, 'Y'
jz @@3
@@2: ; Print Msg_1
mov ax, 4c01h
int 21h
@@3:
@@1: mov cs:tsrOK, true
ret

PrintCopies:
cmp cs:Self, 0
jz @@1
push es ; Added -by- Mr. Lei
mov es, cs:Self ; Aug 24, 1993
mov al, es:Copies
inc al ; Total RI copies
push ax ; Set es = current mcb
mov ax, cs
dec ax
mov es, ax
pop ax
mov cx, 5 ; Search end of file name
mov bx, 8
@@10: inc bx
cmp byte ptr es:[bx], 20h
jz @@20 cmp byte ptr es:[bx], 0ffh
jz @@20 cmp byte ptr es:[bx], 00h
jz @@20
loop @@10
@@20: ; Set current RI no
mov byte ptr es:[bx], ':' ; RI:2
mov byte ptr es:[bx+1], al
cmp bx, 8+7
jnb @@30
mov byte ptr es:[bx+2], 0
@@30:
pop es

mov cs:Msg_RI, al
Print Msg_2
@@1: ret

;---------------------------------------------------------------------------
; Backup Interrupt Vector List
;
BackupVecList:
push ds
push cs
pop es
xor si,si ; Vectors
mov ds,si
movsw
movsw
xor bx, bx
mov cx,00ffh
@@0: lodsw
xchg dx, ax
lodsw
cmp ax, es:[di-2]
jnz @@1 cmp dx, es:[di-4]
jz @@2
@@1: or bx, bx
jz @@3
call SaveCounter
@@3: xchg dx, ax
stosw
xchg dx, ax
stosw
loop @@0
jmp @@4
@@2: inc bx
loop @@0
call SaveCounter
@@4:
pop ds
ret
;
;-----------------------------------------------------------------------------
BackupCVTchain:
mov ax, 'VC'
stosw
push ax
push bx
push cx
push ds
push es
mov ah, 52h
int 21h ; ES:BX -- DOS table as described below

; --------------------------------------------------------------------
push es ; DPB chains
push bx
lds si, es:[bx]
push cs
pop es
mov ax, si
stosw
mov ax, ds
stosw
mov bx, cs:cvtOfs
xor cx, cx
@@1: mov al, ds:[si+1]
stosb
mov ax, ds:[si+bx+12h]
stosw
mov ax, ds:[si+bx+14h]
stosw
inc cx
lds si, ds:[si+bx+18h]
cmp si, -1
jnz @@1
; mov ax, 5
; mul cl
; add ax, 4
; add cs:tsrLength, ax
pop bx
pop es

; --------------------------------------------------------------------
push es ; DCB file control blocks
push bx
les bx, es:[bx+4]
@@11: cmp word ptr es:[bx], -1
jz @@10
les bx, es:[bx]
jmp @@11
@@10:
mov ax, es
xchg ax, bx
push cs
pop es
stosw
xchg ax, bx
stosw
pop bx
pop es
; add cs:tsrLength, 4

; ---------------------------------------------------------------------
push es ; Device Driver Chains
pop ds
add bx, 22h
mov si, bx ; NUL

pop es
mov ax, si
stosw
mov ax, ds
stosw
xor cx, cx
xor bx, bx
@@9: push si
mov cl, 5
rep movsw
inc bx
pop si
lds si, ds:[si]
mov ax, si
inc ax
jnz @@9

pop ds
pop cx
pop bx
pop ax
ret

; ----------------------------------------------------------------------------

BackupBiosData:
mov ax, '--'
stosw
push ds
push si
mov si, 40h
mov ds, si
mov si, 10h
movsw
mov si, 0a8h
movsw
movsw
mov si, 49h
mov cx, 1dh
rep movsb

mov si, 0f0h
mov cx, 8
rep movsw
pop si
pop ds
ret

; ---------------------------------------------------------------------------

BackupMemoryManager:
push cs
pop es
push ds
push es
call SaveXMSstatus
call SaveEMSstatus
pop es
pop ds
ret

;---------------------------------------------------------------------

SaveEMSstatus:
test cs:status, EMSbit
jnz @@1
ret
@@1:
mov ax, 'ME'
stosw
inc di
inc di
push di
mov ah, 4dh
int 67h
pop di
mov es:[di-2], bx
shl bx, 1
shl bx, 1
add di, bx
ret
; -------------------------------------------------------------------

SaveXMSstatus:
call XMS_test
test cs:status, XMSbit
jnz @@1
ret
@@1:
mov ax, 'MX'
stosw

mov dx, 1
call XMS_alloc
jnz @@_1
xor cx, cx ; XMS alloc failure
stosw
ret
@@_1:
push dx
sub dx, MaxHandles  10
@@2:
push dx
call XMS_Lock
pop dx
jnz @@3 cmp bl, 0a2h
jnz @@4
add dx, 10
jmp @@2
@@3: push dx
call XMS_unlock
pop dx
@@4:
mov cs:handle_begin, dx
pop dx
push dx
call XMS_bstat
xor cx, cx
mov cl, bl
inc cx
pop dx
call XMS_Free
mov dx, cs:Handle_begin

push cx
push cs
pop es
mov ax, cx
stosw
@@5: push dx
call XMS_Lock
pop dx
jnz @@6 cmp bl, 0a2h ; Handle invalid
jz @@7
@@6: call XMS_unlock
add dx, 10
jmp @@5
@@7: mov ax, dx
stosw
add dx, 10
loop @@5
pop cx
ret
; ------------------------------------------------------------------

XMS_test:
push es
mov ax, 4300h
int 2fh
cmp al, 80h
jnz @@9
mov ax, 4310h
int 2fh
mov cs:XMS_control, bx
mov cs:XMS_control[2], es
or cs:Status, XMSbit
@@9:
pop es
ret

XMS_stat:
mov ah, 0
call dword ptr cs:xms_control
mov hma_exist, dl
ret
hma_exist db 0

XMS_alloc:
mov ah, 9
call dword ptr cs:xms_control
or ax, ax
ret

XMS_lock:
mov ah, 0ch
call dword ptr cs:xms_control
or ax, ax
ret

XMS_unlock:
mov ah, 0dh
call dword ptr cs:xms_control
or ax, ax
ret
XMS_bstat:
mov ah, 0eh
call dword ptr cs:xms_control
or ax, ax
ret

XMS_free:
mov ah, 0ah
call dword ptr cs:xms_control
or ax, ax
ret

; ----------------------------------------------------------------------------
EMS_test:
push cs
pop ds
mov dx, offset EMMname
mov ax, 3d00h
int 21h
jc @@2
mov bx, ax
mov ah, 3eh
int 21h
or cs:Status, EMSbit
@@2:
ret
EMMname db 'EMMXXXX0',0

; -----------------------------------------------------------------------------

SetHotKey:
xor bx, bx
lodsb
push ax

@@1: lodsb
cmp al, 0dh
jz @@9 cmp al, 'C'
jnz @@2
or bl, LeftCtrl
jmp @@1
@@2:
cmp al, 'c'
jnz @@3
or bl, RightCtrl
jmp @@1
@@3:
cmp al, 'A'
jnz @@4
or bl, LeftAlt
jmp @@1
@@4:
cmp al, 'a'
jnz @@5
or bl, RightAlt
jmp @@1
@@5:
cmp al, 'S'
jnz @@6
or bl, LeftShift
jmp @@1
@@6:
cmp al, 's'
jnz @@7
or bl, RightShift
jmp @@1
@@7: pop ax
jmp @Err
@@9:
mov cs:HotKey, bl
pop ax
mov cs:AuxHotKey, 2dh ; 'X' scan key
cmp al, '1'
jz @@29
mov cs:AuxHotKey, 0
@@29:
cmp cs:Self, 0
jz @@30
push es
mov es, cs:Self
mov es:HotKey, bl
mov bl, cs:AuxHotKey
mov es:AuxHotKey, bl
pop es
@@30:
call GetRunFileName
mov ax, 3d02h
int 21h
jc @@10
push cs
pop ds
mov bx, ax
mov cx, 4
mov dx, 100h
mov ah, 40h
int 21h
jc @@10
mov ax, 4200h
xor cx, cx
mov dx, 17h
int 21h
jc @@10
mov cx, 1
mov dx, offset AuxHotKey
mov ah, 40h
int 21h
jc @@10
mov ah, 3eh
int 21h
@@10:
ret

; -----------------------------------------------------------------------
GetRunFileName:
; Return:
; DS:DX Pointer of this run file name ASCIIZ string
push ax
push bx
push cx
push si
push di
push es

push cs
pop es
mov ax, es:[2ch]
mov es, ax
xor di, di
mov cx, 1000h
xor al, al
@@1: repnz scasb
cmp es:[di], al
loopnz @@1
mov dx, di
add dx, 3
push es
pop ds

pop es
pop di
pop si
pop cx
pop bx
pop ax
ret

; ---------------------------------------------------------------------------
GetMachineID:
push es
mov KBD102,True
mov ax,40h
mov es,ax
test byte ptr es:[96h], 00010000b
jnz @@1
mov Kbd102,False
@@1:
xor ax,ax
dec ax
mov es,ax
mov al,es:[0eh]
mov cs:MachineID, al
pop es
ret

; ---------------------------------------------------------------------------
ModifyHotKeyPrompt:
cmp cs:Kbd102, True
jz @@9
push cs
pop es
push cs
pop ds
mov cx, 124
mov si, offset KMsg2
mov di, offset KMsg1
rep movsb
@@9: cmp cs:MachineID, 0fch
jna @@10
mov cs:clsStrcolor, 70h ; Mono
mov cs:clsStr, 70h
@@10:
ret

; ---------------------------------------------------------------------------
PrintHotKeyPrompt:
Print Msg1
mov al, cs:HotKey
mov ah, al
shr al, 1
shr al, 1
and ax, 33ch
or al, ah
mov dx, offset KeyMsg
@@40:
or ax, ax ; Mr. Lei 4/25/1993
jz @@_42
shr al, 1
push ax
jnc @@41

push ax
call ColorDisplayStr
; mov ah, 9
; int 21h
pop ax

or al, al
jz @@42

push dx
mov dx, offset PlusMsg
call ColorDisplayStr
; Print PlusMsg
pop dx

@@41: add dx, 12
pop ax
jmp @@40
@@42: pop ax
@@_42: cmp cs:AuxHotKey, 0
jz @@43 cmp cs:HotKey, 0 ; Mr. Lei
jz @@_43
mov dx, offset PlusMsg
call ColorDisplayStr
; Print PlusMsg
@@_43: mov dx, offset AuxHotKeyName
call ColorDisplayStr
; Print AuxHotKeyName
@@43:
Print crlf
ret

ColorDisplayStr:
push bx
push cx
push dx
push si
mov bl, 0fh
mov si, dx
xor bh, bh
mov cx, 1
@@1: lodsb
cmp al, '$'
jz @@2
or al, al
jz @@2
push cx
mov ah, 09h
int 10h
mov ah, 3 int 10h
inc dl
mov ah, 2 int 10h
pop cx
jmp short @@1
@@2:
pop si
pop dx
pop cx
pop bx
ret

; ---------------------------------------------------------------------------
CmpSideKick:
xor ax, ax
mov es, ax
les bx, es:[20h]
cmp word ptr es:[bx-4], 4b53h
jnz @@1 cmp word ptr es:[bx-2], 4942h
jz @@2
@@1: mov es, ax
les bx, es:[94h]
cmp word ptr es:[bx-2], 4b53h
jz @@2
ret
@@2: or cs:Status, SKbit
ret

; ---------------------------------------------------------------------------
CmpDosVer: mov ah, 30h
int 21h
cmp al, 3
jb @@1 cmp al, 3
jna @@2
mov cs:cvtOfs, 1
ret
@@2: mov cs:cvtOfs, 0
ret
@@1: Print DosVerErr
mov ax, 4cffh
int 21h

DosVerErr db 'Sorry, DOS version too lower !',0dh,0ah,'$'

HotKeyValid:
cmp cs:HotKey, 0
jnz @@_1
cmp cs:AuxHotKey, 0
jnz @@_1
Print HotKeyErr
mov ax, 4cfeh
int 21h
@@_1: ret

HotKeyErr db 'Sorry, please setup hotkey again. ',0dh,0ah,'$'

eof:
ends
end Start

; ------------- The End ! ---------------------------------------------------
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
;
; RI.ASM Revision 2.12 [ July 12, 1994 ]
Revision equ 'V2.12 '
;
;
;
;  RAMinit Release 2.0 
;  Copyright (c) 1989-1994 by Yellow Rose Software Co.
;  Written by Mr. Leijun
;
;  Function:
;  Press HotKey to remove all TSR program after this program
;
;

; ..........................................................................
; Removed Softwares by RI:
; SPDOS v6.0F, WPS v3.0F
; Game Busters III, IV
; NETX ( Novell 3.11 )
; PC-CACHE
; Norton Cache
; Microsoft SmartDrv
; SideKick 1.56A
; MOUSE Driver
; Crazy (Monochrome simulate CGA program)
; RAMBIOS v2.0
; 386MAX Version 6.01
; ..........................................................................
; No cancel softwares:
; Windows 3.1 MSD
;
; No removed TSR softwares:
; MS-DOS fastopen
; Buffers, Files ... (QEMM 6.0)
; QCache (386MAX 6.01)
; ..........................................................................
;
COMMENT

V2.04 Use mouse driver software reset function to initiation mouse
2/17/1993 by Mr. Lei and Mr. Feng
V2.05 RI cannot work in Windows DOS prompt
3/9/1993 by Mr. Lei
V2.06 1\. When XMS cannot allocate 1K memory, RI halts.
2\. RI repeat deallocates EMS memory.
V2.07 HotKey Setup Error
4/25/1993 by Mr. Lei
V2.08 KB Buffer
V2.10 1\. Release high memory blocks (EMM386 QEMM386 S-ICE 386MAX)
2\. RI copies flag
V2.12 1\. Exists a critical error in Init 8259 procedure
2\. Save [40:F0--FF] user data area

dosseg
.model tiny
.code
locals @@
org 100h

Start: jmp Main
org 103h

True equ 1
False equ 0
MaxHandles equ 100h

INT3 macro
out 0ffh,al
endm
;
; HotKey Status Test Var
; --------------- ---------------
;
; 7 6 5 4 3 2 1 0 417 418 496
; . . x . x . . . Left Alt is pressed 8 2
; x . . . x . . . Right Alt is pressed 8 8
; . . . x . x . . Left Ctrl is pressed 4 1
; . x . . . x . . Right Ctrl is pressed 4 4
; . . . . . . x . Left Shift is pressed 2
; . . . . . . . x Right Shift is pressed 1
;
LeftAlt equ 00101000b
RightAlt equ 10001000b
LeftCtrl equ 00010100b
RightCtrl equ 01000100b
LeftShift equ 00000010b
RightShift equ 00000001b
HotKey db LeftCtrl or RightCtrl

DataBegin dw 0
NextDataSeg dw 0ffffh
oldInt2F_addr dw 0, 0
XMS_control dw 0, 0
Handle_begin dw 0
cvtOfs dw 0 ; DOS 3.0 equ 0 and above DOS 4.0 is 1
org 104h
db 0dh
db Revision
db ??date
db 26
org 114h
tsrLength dw 0
MachineID db 0FCh ; IBM PC/AT

AuxHotKey db 0 ; 2Dh ; 'X' Scan Code
AuxHotKeyName db 'X$ '
Power db True
Flag db '!'
Kbd102 db 0
NoFlag db 0
StopFlag db 1
DosEnv dw 0
WorkSeg dw 0
PrevDataSeg dw 0
Copies db '1'
old_8259 db 0 ; 21h port
db 0 ; a1h port

Status dw 0
XMSbit equ 00000001b
EMSbit equ 00000010b
SKbit equ 10000000b

GoINT1C: db 0eah
oldInt1C_addr dw 0, 0
newINT1C:
test cs:Status, SKbit
jnz GoINT1C
cmp cs:StopFlag, 0
jz @@0
;
; Mr. Lei 2/8/1993
; Problem: if WPS quit and reenter, old RI cann't control keyboard. ;
push ds
push ax
xor ax, ax
mov ds, ax
mov ax, ds:[94]
cmp ax, offset NewInt9
pop ax
pop ds
jnz GoINT1C
mov cs:StopFlag, 0

@@0: push ax
push ds
push es
xor ax, ax
mov ds, ax
mov es, ds:[94+2]
cmp word ptr es:[101h], 'IE' ; 'LEI'
jz @@1
cli
mov cs:StopFlag, 1
mov ax, ds:[94]
mov cs:oldINT9_addr2, ax
mov ax, ds:[94+2]
mov cs:oldINT9_addr2[2], ax
mov ds:[94], offset newINT9_2
mov ds:[94+2], cs
sti
@@1: pop es
pop ds
pop ax
jmp GoINT1C

; ----------------------------------------------------------------------
; INT2F Func
;
; AX = C0D7h Return RI segment in AX
; AX = C0D8h Removes all TSR programs after RI
; AX = C0D9h Removes all TSR programs include RI
; AX = C0DAh Removes all RI copies
; ----------------------------------------------------------------------

newINT2F:
cmp ax, 0c0d7h ; LEI Hanzi GB Code
jnz @@1
push cs
pop ax
iret
@@1: cmp ax, 0c0d7h+1
jnz @@2
jmp KeepSelf
@@2: cmp ax, 0c0d7h+2
jnz @@3
jmp NoKeepSelf
@@3: cmp ax, 0c0d7h+3
jnz @@9
mov cs:NextDataSeg, -1
mov cs:Copies, '1'
jmp NoKeepSelf
@@9: jmp dword ptr cs:oldInt2F_addr

CallInt9:
ret

newINT9_2:
mov cs:NoFlag, 1
pushf
db 9ah ; call far ptr oldint9_addr
oldInt9_Addr2 dw 0, 0
jmp newINT9_proc

newINT9:
pushf
db 9ah ; call far ptr oldint9_addr
oldInt9_Addr dw 0, 0 cmp cs:NoFlag, 0
jz newINT9_proc
mov cs:NoFlag, 0
iret
newINT9_proc:
cmp cs:Flag, '!' ; busy ?
jnz @@0
iret
@@0:
mov cs:Flag, '!' ; set busy flag
push ax ; cmp hot key
push bx
push es
mov ax,40h
mov es,ax

cmp cs:AuxHotKey, 0
jz @@_1
mov bx, es:[1ah]
cmp bx, es:[1ch]
jz @@10
push bx
mov bl, es:[bx+1]
cmp bl, cs:AuxHotKey
pop bx
jnz @@10
@@_1:
mov ah,es:[17h] ; test CTRL SHIFT ALT
mov al,cs:HotKey
push ax
and ax,0f0fh
cmp al,ah
pop ax
jnz @@10 cmp cs:Kbd102, True
jnz @@1
shr al, 1
shr al, 1
shr al, 1
shr al, 1
push ax
mov ah, es:[18h]
and ax, 303h
cmp al, ah
pop ax
jnz @@10
mov ah, es:[96h]
shr ax, 1
shr ax, 1
and ax, 303h
cmp al, ah
jnz @@10 cmp cs:AuxHotKey, 0
jz @@_3
inc bx
inc bx
cmp bx, 3eh
jb @@_2
mov bx, 1eh
@@_2:
mov es:[1ah], bx
@@_3:
call IsWinDos
or ax, ax
jz @@1
call Beep
@@10:
sti
pop es
pop bx
pop ax
mov cs:Flag, ' ' ; no busy
iret
@@1: ; OK
pop es
pop bx
pop ax

KeepSelf:
call RemoveTSR
push es
mov es,cs:WorkSeg
mov dx,es:tsrLength
mov di,dx
mov al,0h ; Aug 24, 1993
mov cx,100h
rep stosb
pop es
int 27h

NoKeepSelf:
mov ax,0e07h
int 10h
mov cs:clsStr, 47h ; Color (White in Red)
call RemoveTSR
dec cs:Copies
call RestoreSelfIntVec
push es
cmp cs:PrevDataSeg, 0
jz @@1
mov es, cs:PrevDataSeg
mov es:NextDataSeg, -1
@@1: pop es
mov ax, 4c00h
int 21h

; ---------------------------------------------------------------------------

IsWinDOS:
mov ax, 1600h
int 2fh
cmp al, 01h
jz @@9 cmp al, 0ffh
jz @@9 ; Windows/386 Version 2.X
cmp al, 00h
jz @@1 cmp al, 80h
jnz @@9 ; Windows 3 in enhanced mode
; Version number in AL/AH
@@1:
mov ax, 4680h
int 2fh
cmp al, 80h
jnz @@9
xor ax, ax
jmp @@10
@@9: mov ax, 1
@@10: ret

; -----------------------------------------------------------------------
RestoreSelfIntVec:
cmp Copies, '0'
jz @@0
ret
@@0:
cli
push cs
pop ds
xor ax, ax
mov es, ax
mov si, offset oldInt9_Addr
mov di, 94
movsw
movsw
mov si, offset oldInt2F_Addr
mov di, 2Fh4
movsw
movsw
mov si, offset oldInt1C_Addr
mov di, 1Ch4
movsw
movsw
sti
ret

; ------------- KERNEL PROGRAM ----------------------------------------------
RemoveTSR:
pop ax
cli ; Set stack
mov sp, cs
mov ss, sp
mov sp, 100h
sti
push ax

cmp cs:Power, True
jnz @@1
call Init8259
@@1:
push cs
pop ds
@@_0:
mov ax,ds:NextDataSeg
cmp ax, -1
jz @@_1
mov cs:PrevDataSeg, ds
mov ds, ax
jmp @@_0
@@_1: mov si,ds:DataBegin
mov cs:WorkSeg, ds
lodsw
cmp ax, 'XX'
jz @@_2
call Beep
ret
@@_2:
call RestoreEnvStr
call RestoreMCB ; restore current mcb
call CloseFiles
call RestorePort
call RestoreLEDs
call RestoreVecList ; Restore vectors list
call RestoreFloppyParam
cmp cs:Power, True
jnz @@2
call RestoreCVTchain ; Restore cvt chain
call RestoreMemoryManager
@@2:
call RestoreBiosData
call Enable8259
mov ah, 1 int 16h

call RestoreClockSpeed
call CloseSpeaker
call ResetDisk
call UpdateTime

call ClosePRN
mov bx,cs:WorkSeg
mov ah,50h
int 21h ; Set PSP segment
mov ax,3 int 10h ; Set display mode

call InitPRN
call InitMouse
mov al, cs:Copies
cmp al, '1'
ja @@_sh1
mov cs:ShowCopies, ''
jmp @@_sh2
@@_sh1: mov cs:ShowCopies, al
@@_sh2:
mov si, offset clsStr
call ColorPrintStr
mov cs:Flag, ' ' ; no busy
cmp Copies, '1'
jnz @@_end
mov cs:StopFlag, 0
@@_end:
call ClearKB_buffer
ret

Beep:
mov ax,0e07h
int 10h
ret

; #########################################################################

ClearKB_Buffer:
push es
push bx
mov bx, 0040h
mov es, bx
cli
mov bx, es:[1ah]
mov es:[1ch], bx
sti
pop bx
pop es
ret

Init8259:
; cmp cs:Copies, '1'
; jz @@1
; ret
@@1:
cmp cs:MachineID, 0fch
ja @@pc_xt
@@AT:
mov bx,870h ;
mov al,0 ;
out 0F1h,al ;
jcxz $+2
jcxz $+2
mov al,11h ; ICW1
out 0A0h,al
jcxz $+2
jcxz $+2
out 20h,al
jcxz $+2
jcxz $+2
mov al,bl ; ICW2
out 0A1h,al
jcxz $+2
jcxz $+2
mov al,bh
out 21h,al
jcxz $+2
jcxz $+2
mov al,2 ; ICW3
out 0A1h,al
jcxz $+2
jcxz $+2
mov al,4
out 21h,al
jcxz $+2
jcxz $+2
mov al,1 ; ICW4
out 0A1h,al
jcxz $+2
jcxz $+2
out 21h,al
jcxz $+2
jcxz $+2
mov al,0FFh ; OCW1
out 0A1h,al
jcxz $+2
jcxz $+2
out 21h,al
ret
@@PC_XT:
mov al,13h ; ICW1
out 20h,al
jcxz $+2
jcxz $+2
mov al,8 ; ICW2
out 21h,al
jcxz $+2
jcxz $+2
mov al,9 ; ICW4
out 21h,al
jcxz $+2
jcxz $+2
mov al,0FFh ; OCW1
out 21h,al
ret

Enable8259:
mov ax, word ptr cs:old_8259
out 021h,al
jcxz $+2
jcxz $+2
mov al,ah
out 0a1h,al ; DEC PC Bus Mouse
ret ; July 1994 by Mr. Lei

; -------------------------------------------------------------------------

RestoreBiosData:
lodsw
cmp ax, '--'
jz @@1
call Beep
ret
@@1: push es
push di
mov di, 40h
mov es, di

mov di, 10h
movsw
mov di, 0a8h ; [40h:a8h]
movsw
movsw
mov di, 49h
mov cx, 1dh
rep movsb

mov di, 0f0h ; User data
mov cx, 8
rep movsw

pop di
pop es
ret

; -------------------------------------------------------------------------

RestoreMCB:
push ds
push es
lodsw ; 'MZ'
@@0: lodsw
cmp ax, 'MM'
jz @@1
mov es,ax
xor di,di
movsb
movsw
movsw
inc ax
mov bx, ds
cmp ax, bx
jz @@10
mov byte ptr es:[8], 0 ; Aug 24, 1993
@@10: cmp byte ptr es:[0], 'Z'
jnz @@0
mov byte ptr es:[10h], 0
jmp @@0
@@1:
pop es
pop ds
ret

; -------------------------------------------------------------------------
CloseFiles:
mov ax, 5 ; Begin handle
push ds
push si
mov cx, 15 ; Max handle
sub cx, ax
inc cx
mov bx, ax
@@1: push bx
push cx
mov ah, 3eh
int 21h
pop cx
pop bx
inc bx
loop @@1
pop si
pop ds
ret

; -------------------------------------------------------------------------
RestorePort:
mov di, 40h ; restore port
mov es, di
xor di, di
mov cx, 8
rep movsw
ret

; -------------------------------------------------------------------------
RestoreLEDs:
lodsb
and al, 11110000b ; LED status
mov ah, es:[17h]
and ah, 00001111b
or ah, al
and ah, 0f0h ; Clear CTRL ALT SHIFT
mov es:[17h], ah
ret

; -------------------------------------------------------------------------
RestoreEnvStr:
lodsw
push si
push di
push ds
push es
mov es, cs:DosEnv
mov ds, ax
xor si, si
mov di, si
@@0: lodsb
or al, al
jnz @@1 cmp byte ptr ds:[si], 0
jz @@2
@@1: stosb
jmp @@0
@@2: stosb
stosb
pop es
pop ds
pop di
pop si
ret

; -----------------------------------------------------------------------
RestoreVecList:
xor ax,ax
mov di,ax
mov es,ax
mov cx,100h
@@0: lodsw
xchg dx, ax
lodsw
cmp dx, 'EL'
jnz @@1 cmp al, 'I'
jnz @@1
sub cl, ah
push cx
mov cl, ah
mov ax, es:[di-4]
mov dx, es:[di-2]
@@a: stosw
xchg ax, dx
stosw
xchg ax, dx
loop @@a
pop cx
or cx, cx
jz @@9
jmp @@0
@@1:
xchg ax, dx
stosw
xchg ax, dx
stosw
loop @@0
@@9:
ret

;----------------------------------------------------------------------------
RestoreFloppyParam: ; Mr. Lei 2/10/1992
push es
push ax
xor ax, ax
mov es, ax
mov byte ptr es:[525h], 2
pop ax
pop es
ret

;---------------------------------------------------------------------------
RestoreCVTchain:
lodsw
cmp ax, 'VC'
jz @@_0
call Beep
ret
@@_0:
push ax
push cx
push es

; -----------------------------------------------------------------
lodsw ; DPB
mov di, ax
lodsw
mov es, ax
@@1: lodsb
inc di
stosb
add di, cs:cvtOfs
add di, 10h
movsw
movsw
les di, es:[di+2]
cmp di, -1
jnz @@1

; -----------------------------------------------------------------
lodsw ; DCB
mov di, ax
lodsw
mov es, ax
xor ax, ax
dec ax
stosw

; -----------------------------------------------------------------
lodsw ; Device Driver Chain
mov di, ax
lodsw
mov es, ax
xor cx, cx
@@9: push di
mov cl, 5
rep movsw
pop di
les di, es:[di]
mov ax, di
inc ax
jnz @@9
pop es
pop cx
pop ax
ret

; ----------------------------------------------------------------------------
RestoreMemoryManager:
test cs:Status, XMSbit
jz @@1
call LoadXMSstatus
@@1:
test cs:Status, EMSbit
jz @@2
call LoadEMSstatus
@@2:
ret

LoadEMSstatus:
lodsw
cmp ax, 'ME'
jz @@_0
call Beep
ret
@@_0:
lodsw
mov cx, ax
xor dx, dx
@@_1: push ds
push si
push dx
push cx

@@0: cmp dx, ds:[si]
jz @@1
add si, 4
loop @@0

push cx
mov cx, 5
@@0: mov ah, 45h ; Deallocate Handle and Memory
int 67h
or ah, ah
jz @@1
loop @@0
@@1: pop cx

@@1:
pop cx
pop dx
pop si
pop ds
inc dx
cmp dx, 100h
jb @@_1
shl cx, 1
shl cx, 1
add si, cx
ret

LoadXMSstatus:
lodsw
cmp ax, 'MX'
jz @@_0
call Beep
ret
@@_0:
lodsw
mov cx, ax
jcxz @@5
@@1:
lodsw
mov dx, ax
@@2: push dx
mov ah, 0ah ; free
call dword ptr cs:xms_control
or ax, ax
pop dx
jnz @@4 cmp bl, 0abh
jnz @@4
push dx
mov ah, 0dh ; unlock
call dword ptr cs:xms_control
or ax, ax
pop dx
jmp @@2
@@4: loop @@1
@@5: ret
endp

; -----------------------------------------------------------------------
CloseSpeaker:
in al, 61h
and al, 0fch
out 61h, al
ret

; -----------------------------------------------------------------------
RestoreClockSpeed:
mov al, 00110110b
out 43h, al
xor ax, ax
out 40h, al
out 40h, al
ret

; -----------------------------------------------------------------------
ResetDisk:
xor ax, ax
xor dx, dx
int 13h ; Restore A
inc dx
int 13h ; Restore B
mov dl, 80h
int 13h ; Restore C
ret

; --------------------------------------------------------------------------
ClosePRN:
mov ah, 51h ; Get PSP seg
int 21h
mov es, bx
mov ax, es:[16h] ; Prev PSP seg
cmp ax, bx
jnz @@9
mov ax, 3e00h ; COMMAND
mov bx, 4 int 21h
@@9:
ret

InitPRN:
mov ax, 3e00h
mov bx, 4 ; PRN
int 21h
mov ax, 3d01h
mov dx, offset PRNname
push cs
pop ds
int 21h
ret
PRNname db 'PRN',0

InitMouse: ; 2/16/1993 by Mr. Lei
push es
xor ax, ax
mov es, ax
cmp word ptr es:[33h4+2], 0
jz @@0 cmp word ptr es:[33h4], 0
jz @@0
mov ax, 21h
int 33h ; Hook Mouse Interrupt
@@0: pop es
ret

; ------------- CMOS CLOCK set to System -----------------------------------
UpdateTime:
call GetRealTime
mov ah, 2dh
int 21h
ret

GetRealTime:
mov ah,2 int 1Ah
mov al,ch
call bcdxchg
mov ch,al
mov al,cl
call bcdxchg
mov cl,al
mov al,dh
call bcdxchg
mov dh,al
mov dl,0
ret

BCDxchg:
push ax
push cx
mov cl,4
shr al,cl
pop cx
mov bl,0Ah
mul bl
pop bx
and bl,0Fh
add al,bl
ret

; -----------------------------------------------------------------------
; Display string
ColorPrintStr:
lodsb
mov bh, al ; color
xor cx, cx
mov dx, 014fh
mov ax, 0600h
int 10h

mov ah, 02 ; GotoXY (0, 0)
xor dx, dx
mov bh, 0 int 10h
PrintStr:
push cs
pop ds
xor bx, bx
@@1: lodsb
cmp al, '$'
jz @@2
or al, al
jz @@2
mov ah, 0eh
int 10h
jmp short @@1
@@2: mov al, cs:clsStrcolor
mov cs:clsStr, al
ret

; -----------------------------------------------------------------------
Self dw 0
clsStrcolor db 17h
clsStr db 17h ; Color (White in Blue)
db ' RAMinit Version 2.12 (c) 1989-1994 by KingSoft Ltd. Mr. Leijun'
db 0dh,0ah
db ' ['
ShowCopies db ''
db '] Activate...',0ah,0dh,'$'

endTSR equ $
mcbList equ offset endTSR + 2 + 2
vecList equ mcbList + 710 + 2 + 10h + 1 + 400h
devLink equ vecList + 4 + 5  26 + 4 + 10  30h + 4
xmsList equ devLink + 2 + MaxHandles  2
emsList equ xmsList + 4 + 1024
crtMode equ emsList + 2 + 1Dh + 4 + 10h
tsrLen equ crtMode + 1
;
; DOS Environment Reserved by RI
; --------------------------------------------------
; Flag 'XX' 2 bytes
; Environment Segment 1 word
; Free MCBs <=710 bytes
; MCB segment 1 word
; MCB 5 bytes
; End flag 'MM' 1 word
; COM LPT ports 10h bytes
; LEDs status 1 bytes
; Packed vectors list <=400h bytes
; Flag 'CV' 2 bytes
; CVT First DPB pointer 4 bytes
; DPBs data <=526 bytes
; First DCB pointer 4 bytes
; Pointer to NUL 4 bytes
; All device driver datas <=30h10 bytes
; Flag 'XM' 2 bytes
; XMS free handle counter 2 bytes
; EMS free handle list <=100h4 bytes
; Flag 'EM' 2 bytes
; EMS free handle counter 2 bytes
; EMS free handle list <=1024 bytes
; EMS handle 1 word
; Number of pages 1 word
; Flag '--' 1 word
; Equipment List 1 word
; CRT 40:49h-66h 1dh bytes
; 40:A8h 1 dword
; BIOS User Data Area 40:F0--FF 10h bytes
; **
;
main: jmp main0

Print Macro Str
Lea dx, Str
call DisplayStr
endm

InstMsg db 'RAMinit Version 2.12 '
db 'Copyright (c) 1989-1994 by KingSoft Ltd. ',0dh,0ah,'$'
Msg0 db 'Already installed !',0dh,0ah,0ah
db 'For Help, type RI /?. ',0dh,0ah,'$'
Msg_0 db 0ah,'Residents a new RAMinit copy [y/n] ? $'
Msg_2 db 'OK, RI No.'
Msg_RI db '2'
db ' residents successful !', 0dh,0ah,'$'
Msg1 db 'Activate with: $'
KeyMsg db 'Right_Shift$'
db 'Left_Shift$ '
KMsg1 db 'Left_Ctrl$ '
db 'Left_Alt$ '
db 'Right_Ctrl$ '
db 'Right_Alt$ '
KMsg2 db 'Ctrl$ '
db 'Alt$ '
db 'Ctrl$ '
db 'Alt$ '
PlusMsg db ' + $'
crlf db 0dh,0ah,'$'

HelpMsg db 'Programmed by Mr. Leijun Dec 1992', 0dh,0ah,0ah
db 'Usage: RI [options]',0dh,0ah,0ah
db '/H,/? Display this screen',0dh,0ah
db '/CLS Removes all TSR programs after current RI',0dh,0ah
db '/RET Removes TSR programs include current RI',0dh,0ah
db '/NEW Residents a new data copy of current environment',0dh,0ah
db '/ALL Removes all RI copies and all other tsr programs',0dh,0ah
db '/Sxyy.. Define Hotkey x=AuxHotkey yy..=shift status',0dh,0ah
db ' x=auxiliary hotkey (default is X) ',0dh,0ah
db ' x equ 1 means need AuxHotkey',0dh,0ah
db ' yy..=shift status [CAScas]',0dh,0ah
db ' C: Left Ctrl A: Left Alt S: Left Shift',0dh,0ah
db ' c: Right Ctrl a: Right Alt s: Right Shift',0dh,0ah,0ah
db 'Example: RI /S1c means Hotkey is Right_Ctrl+X',0dh,0ah
db ' RI /S0Cc means HotKey is Left_Ctrl+Right_Ctrl',0dh,0ah
db ' RI /CLS equals simply press hotkey',0dh,0ah
db ' RI /RET Removes all TSRs after current RI and this RI',0dh,0ah
db 0ah
db 'Contact me for RAMinit problems: (01)2561155 Call 1997',0dh,0ah
db '$'
ErrMsg db 'ERROR: Invalid options !',0dh,0ah,0ah,'$'
WinErr db 7, 'Sorry, I cannot work in Windows DOS environment.',0dh,0ah,'$'
SetMsg db 7, 'Defines new Hotkey successful !',0dh,0ah,0ah,'$'
tsrOK db False

Main0:
cld
Print instMsg
call IsWinDos
or ax, ax
jz @@1
Print WinErr
mov ax, 4c00h
int 21h
@@1:
call HotKeyValid
mov cs:Status, 0
call EMS_test
call CmpDosVer
call CmpSideKick
call GetMachineID
call ModifyHotKeyPrompt

mov ax, 0c0d7h
int 2fh
mov es, ax
cmp word ptr es:[101h], 'IE' ; 'LEI'
jnz @@0
mov cs:Self, ax
@@0:
call CmdLine
call PrintHotKeyPrompt

cmp cs:tsrOK, true
jz @@2
call tsrReplyOK
@@2: cmp cs:tsrOK, true
jnz @@_2
call PrintCopies
@@_2:
mov word ptr cs:[100h], 'EL'
mov byte ptr cs:[102h], 'I'

push cs
pop es
push cs
pop ds
std
mov si, offset eof
mov cx, eof - offset Here
mov di, tsrLen
add di, cx
inc cx
rep movsb
cld
mov bx, tsrLen
jmp bx

Here:
mov ax,cs
mov es,ax
mov di,offset endTSR
mov cs:DataBegin, di
mov cs:NextDataSeg, -1
mov ax, 'XX'
stosw
in al, 0a1h
mov ah, al
in al, 21h
push ax
mov word ptr cs:old_8259, ax
xor ax, ax
out 21h,al ; CLI
call SaveOthers
call SetSelfInt
call BackupVecList
cmp cs:Power, true
jnz @@20
call BackupCVTchain
call BackupMemoryManager
@@20:
call BackupBiosData

sti
mov cs:Flag, ' ' ; no busy
mov cs:StopFlag, 0 ;

mov cs:tsrLength, di
call SetDosEnvSeg
cmp cs:Self, 0
jz @@29
push cs
pop ds
push cs
pop es
cld
mov cx, cs:tsrLength
mov si, cs:DataBegin
sub cx, si
mov di, 120h
mov cs:DataBegin, di
rep movsb
mov cs:tsrLength, di
@@29:
pop ax
out 21h, al ; STI
mov al, ah
out 0a1h, al
mov dx, cs:tsrLength
inc dx
int 27h

; ----------------------------------------------------------------------------
SetDosEnvSeg:
push ds
push es
mov ax, cs
@@10: mov es, ax
mov ax, es:[16h] ; Get father process psp segment
or ax, ax
jz @@11
mov bx, es
cmp ax, bx
jnz @@10
@@11:
mov es, word ptr es:[2ch] ; Get father process env segment
mov cs:DosEnv, es
pop es
pop ds
ret

; ----------------------------------------------------------------------------

SaveOthers:
mov ax, cs:[2ch] ; Env Seg
stosw
call backupMCB ; Current MCB
mov ax, 40h ; COM LPT Port
mov ds, ax
mov si, 0h
mov cx, 8
rep movsw

mov si, 17h ; LED status
lodsb
stosb
; call OpenLEDs
ret

; --------------------------------------------------------------------------
backupMCB:
mov ax, 'ZM'
stosw
push ds
push es
mov ah, 52h
int 21h ; Get MCB chain head
mov ax, es:[bx-2]
pop es
@@0: mov ds, ax
cmp byte ptr ds:[0], 'Z' ; End ?
jz @@20 cmp byte ptr ds:[0], 'M' ; Memory control block
jnz @@30 cmp word ptr ds:[3], 0 ; Nul mcb
jz @@10 cmp word ptr ds:[1], 0 ; Free MCB
jnz @@10
call SaveFreeMCB
@@10: inc ax
add ax, ds:[3]
jmp @@0
@@20:
call SaveFreeMCB
cmp ax, 0a000h
inc ax
jnb @@30
mov ax, 9fffh ; MS-DOS UMB
jmp @@0

@@30:
cmp ax, 0c000h ; 386MAX
ja @@90
mov ax, 0c020h
jmp @@0

@@90: ; Error ?
pop ds
mov ax, 'MM' ; Set MCB flag
stosw
ret

SaveFreeMCB:
stosw
xor si,si
movsb
movsw
movsw
ret
;
; push ax
; stosw
; xor si,si
; movsb
; movsw
; movsw
; pop ax
; cmp ax, 09fffh
; jnb @@3
; push ax
; push ds
; mov ds,ax
; cmp byte ptr ds:[0], 'M'
; pop ds
; pop ax
; jnz @@4
; mov ax, 09fffh ; MS-DOS UMB
; jmp @@0
; @@4: cmp ax, 0c000h
; ja @@3
; mov ax, 0c020h ; 386MAX
; jmp @@0
;
; --------------------------------------------------------------------------

OpenLEDs: push ax ; Open all LEDs
or al, 070h
mov ds:[17h], al
mov ah, 1 int 16h
mov cx, 4 ; Delay
@@20: push cx
xor cx, cx
@@21: loop @@21
pop cx
loop @@20
pop ax
mov ds:[17h], al
mov ah, 1 int 16h
ret

; --------------------------------------------------------------------------
SetSelfInt:
push es
push di

cmp cs:self, 0
jnz @@1
push cs
pop ds
mov ax,3509h
int 21h
mov word ptr cs:oldInt9_addr,bx
mov word ptr cs:oldInt9_addr[2],es
mov dx,offset NewInt9
mov ax,2509h
int 21h

mov ax,352Fh
int 21h
mov word ptr cs:oldInt2F_addr,bx
mov word ptr cs:oldInt2F_addr[2],es
mov dx,offset newInt2F
mov ax,252Fh
int 21h

mov ax,351Ch
int 21h
mov word ptr cs:oldInt1C_addr,bx
mov word ptr cs:oldInt1C_addr[2],es
mov dx,offset newInt1C
mov ax,251ch
int 21h
cli
jmp @@2
@@1:
mov es, cs:Self
inc es:Copies
@@_0: cmp es:NextDataSeg, -1
jz @@_1
mov es, es:NextDataSeg
jmp @@_0
@@_1: mov es:NextDataSeg, cs
@@2:
pop di
pop es
ret

; -----------------------------------------------------------------------
SaveCounter:
mov word ptr es:[di], 'EL'
mov byte ptr es:[di+2], 'I'
mov byte ptr es:[di+3], bl
xor bx, bx
add di, 4
ret

; -----------------------------------------------------------------------
DisplayStr: push cs
pop ds
mov ah, 9 int 21h
ret

; -----------------------------------------------------------------------
CmdLine:
push cs
pop ds
xor ax, ax
mov si, 80h
lodsb
or al, al
jnz @@1
ret
@@1:
mov cx, ax
dec ax
push ax
push si
@@0: lodsb
cmp al, ' '
jz @@0 cmp al, '/'
jnz @@2
lodsb
cmp al, 'S'
jz @@_2
cmp al, 's'
jnz @@2
@@_2:
call SetHotKey
Print SetMsg
mov ax, 4c00h
int 21h
@@2:
pop si
pop ax
push ax
push si
@@_3: lodsb
cmp al, 'A'
jb @@3 cmp al, 'Z'
ja @@3
add byte ptr ds:[si-1],20h ; DownCase
@@3: loop @@_3
pop si
pop cx

add si, cx
lodsb
cmp al, 's' ; CLS
jnz @@5 cmp word ptr ds:[si-3], 'lc'
jnz @@5 cmp cs:Self, 0
jz @Err
mov ax, 0c0d7h+1 int 2fh

@@5: cmp al, 'h' ; HELP
jz @help
cmp al, '?'
jz @help
cmp al, 't' ; RET
jnz @@6 cmp word ptr ds:[si-3], 'er'
jnz @@6
@@7:
cmp cs:Self, 0
jz @Err
mov ax, 0c0d7h+2 int 2fh
@@6: cmp al, 'w' ; NEW
jnz @@8 cmp word ptr ds:[si-3], 'en'
jnz @@8
mov cs:tsrOK, true
ret
@@8:
cmp al, 'l' ; ALL
jnz @@9 cmp word ptr ds:[si-3], 'la'
jnz @@9
mov ax, 0c0d7h+3 int 2fh
@@9:
cmp al, ' '
jnz @Err
ret

@Err:
Print ErrMsg
@help:
Print HelpMsg
mov ax, 4c00h
int 21h

;---------------------------------------------------------------------------
tsrReplyOK:
cmp cs:Self, 0
jz @@1
Print Msg0

push es
mov ax, cs:Self
@@_10: mov es, ax
mov ax, es:NextDataSeg
cmp ax, -1
jnz @@_10
mov ax, es

@@_0: push ax
dec ax
mov es, ax
mov bx, es:[3]
pop ax

add ax, bx
inc ax
mov es, ax
cmp word ptr es:[0], 'OC'
jz @@_0

mov bx, cs
cmp ax, bx
pop es
jz @@2
Print Msg_0
mov ah, 1 int 21h

push ax
Print crlf
pop ax

cmp al, 'y'
jz @@3 cmp al, 'Y'
jz @@3
@@2: ; Print Msg_1
mov ax, 4c01h
int 21h
@@3:
@@1: mov cs:tsrOK, true
ret

PrintCopies:
cmp cs:Self, 0
jz @@1
push es ; Added -by- Mr. Lei
mov es, cs:Self ; Aug 24, 1993
mov al, es:Copies
inc al ; Total RI copies
push ax ; Set es = current mcb
mov ax, cs
dec ax
mov es, ax
pop ax
mov cx, 5 ; Search end of file name
mov bx, 8
@@10: inc bx
cmp byte ptr es:[bx], 20h
jz @@20 cmp byte ptr es:[bx], 0ffh
jz @@20 cmp byte ptr es:[bx], 00h
jz @@20
loop @@10
@@20: ; Set current RI no
mov byte ptr es:[bx], ':' ; RI:2
mov byte ptr es:[bx+1], al
cmp bx, 8+7
jnb @@30
mov byte ptr es:[bx+2], 0
@@30:
pop es

mov cs:Msg_RI, al
Print Msg_2
@@1: ret

;---------------------------------------------------------------------------
; Backup Interrupt Vector List
;
BackupVecList:
push ds
push cs
pop es
xor si,si ; Vectors
mov ds,si
movsw
movsw
xor bx, bx
mov cx,00ffh
@@0: lodsw
xchg dx, ax
lodsw
cmp ax, es:[di-2]
jnz @@1 cmp dx, es:[di-4]
jz @@2
@@1: or bx, bx
jz @@3
call SaveCounter
@@3: xchg dx, ax
stosw
xchg dx, ax
stosw
loop @@0
jmp @@4
@@2: inc bx
loop @@0
call SaveCounter
@@4:
pop ds
ret
;
;-----------------------------------------------------------------------------
BackupCVTchain:
mov ax, 'VC'
stosw
push ax
push bx
push cx
push ds
push es
mov ah, 52h
int 21h ; ES:BX -- DOS table as described below

; --------------------------------------------------------------------
push es ; DPB chains
push bx
lds si, es:[bx]
push cs
pop es
mov ax, si
stosw
mov ax, ds
stosw
mov bx, cs:cvtOfs
xor cx, cx
@@1: mov al, ds:[si+1]
stosb
mov ax, ds:[si+bx+12h]
stosw
mov ax, ds:[si+bx+14h]
stosw
inc cx
lds si, ds:[si+bx+18h]
cmp si, -1
jnz @@1
; mov ax, 5
; mul cl
; add ax, 4
; add cs:tsrLength, ax
pop bx
pop es

; --------------------------------------------------------------------
push es ; DCB file control blocks
push bx
les bx, es:[bx+4]
@@11: cmp word ptr es:[bx], -1
jz @@10
les bx, es:[bx]
jmp @@11
@@10:
mov ax, es
xchg ax, bx
push cs
pop es
stosw
xchg ax, bx
stosw
pop bx
pop es
; add cs:tsrLength, 4

; ---------------------------------------------------------------------
push es ; Device Driver Chains
pop ds
add bx, 22h
mov si, bx ; NUL

pop es
mov ax, si
stosw
mov ax, ds
stosw
xor cx, cx
xor bx, bx
@@9: push si
mov cl, 5
rep movsw
inc bx
pop si
lds si, ds:[si]
mov ax, si
inc ax
jnz @@9

pop ds
pop cx
pop bx
pop ax
ret

; ----------------------------------------------------------------------------

BackupBiosData:
mov ax, '--'
stosw
push ds
push si
mov si, 40h
mov ds, si
mov si, 10h
movsw
mov si, 0a8h
movsw
movsw
mov si, 49h
mov cx, 1dh
rep movsb

mov si, 0f0h
mov cx, 8
rep movsw
pop si
pop ds
ret

; ---------------------------------------------------------------------------

BackupMemoryManager:
push cs
pop es
push ds
push es
call SaveXMSstatus
call SaveEMSstatus
pop es
pop ds
ret

;---------------------------------------------------------------------

SaveEMSstatus:
test cs:status, EMSbit
jnz @@1
ret
@@1:
mov ax, 'ME'
stosw
inc di
inc di
push di
mov ah, 4dh
int 67h
pop di
mov es:[di-2], bx
shl bx, 1
shl bx, 1
add di, bx
ret
; -------------------------------------------------------------------

SaveXMSstatus:
call XMS_test
test cs:status, XMSbit
jnz @@1
ret
@@1:
mov ax, 'MX'
stosw

mov dx, 1
call XMS_alloc
jnz @@_1
xor cx, cx ; XMS alloc failure
stosw
ret
@@_1:
push dx
sub dx, MaxHandles  10
@@2:
push dx
call XMS_Lock
pop dx
jnz @@3 cmp bl, 0a2h
jnz @@4
add dx, 10
jmp @@2
@@3: push dx
call XMS_unlock
pop dx
@@4:
mov cs:handle_begin, dx
pop dx
push dx
call XMS_bstat
xor cx, cx
mov cl, bl
inc cx
pop dx
call XMS_Free
mov dx, cs:Handle_begin

push cx
push cs
pop es
mov ax, cx
stosw
@@5: push dx
call XMS_Lock
pop dx
jnz @@6 cmp bl, 0a2h ; Handle invalid
jz @@7
@@6: call XMS_unlock
add dx, 10
jmp @@5
@@7: mov ax, dx
stosw
add dx, 10
loop @@5
pop cx
ret
; ------------------------------------------------------------------

XMS_test:
push es
mov ax, 4300h
int 2fh
cmp al, 80h
jnz @@9
mov ax, 4310h
int 2fh
mov cs:XMS_control, bx
mov cs:XMS_control[2], es
or cs:Status, XMSbit
@@9:
pop es
ret

XMS_stat:
mov ah, 0
call dword ptr cs:xms_control
mov hma_exist, dl
ret
hma_exist db 0

XMS_alloc:
mov ah, 9
call dword ptr cs:xms_control
or ax, ax
ret

XMS_lock:
mov ah, 0ch
call dword ptr cs:xms_control
or ax, ax
ret

XMS_unlock:
mov ah, 0dh
call dword ptr cs:xms_control
or ax, ax
ret
XMS_bstat:
mov ah, 0eh
call dword ptr cs:xms_control
or ax, ax
ret

XMS_free:
mov ah, 0ah
call dword ptr cs:xms_control
or ax, ax
ret

; ----------------------------------------------------------------------------
EMS_test:
push cs
pop ds
mov dx, offset EMMname
mov ax, 3d00h
int 21h
jc @@2
mov bx, ax
mov ah, 3eh
int 21h
or cs:Status, EMSbit
@@2:
ret
EMMname db 'EMMXXXX0',0

; -----------------------------------------------------------------------------

SetHotKey:
xor bx, bx
lodsb
push ax

@@1: lodsb
cmp al, 0dh
jz @@9 cmp al, 'C'
jnz @@2
or bl, LeftCtrl
jmp @@1
@@2:
cmp al, 'c'
jnz @@3
or bl, RightCtrl
jmp @@1
@@3:
cmp al, 'A'
jnz @@4
or bl, LeftAlt
jmp @@1
@@4:
cmp al, 'a'
jnz @@5
or bl, RightAlt
jmp @@1
@@5:
cmp al, 'S'
jnz @@6
or bl, LeftShift
jmp @@1
@@6:
cmp al, 's'
jnz @@7
or bl, RightShift
jmp @@1
@@7: pop ax
jmp @Err
@@9:
mov cs:HotKey, bl
pop ax
mov cs:AuxHotKey, 2dh ; 'X' scan key
cmp al, '1'
jz @@29
mov cs:AuxHotKey, 0
@@29:
cmp cs:Self, 0
jz @@30
push es
mov es, cs:Self
mov es:HotKey, bl
mov bl, cs:AuxHotKey
mov es:AuxHotKey, bl
pop es
@@30:
call GetRunFileName
mov ax, 3d02h
int 21h
jc @@10
push cs
pop ds
mov bx, ax
mov cx, 4
mov dx, 100h
mov ah, 40h
int 21h
jc @@10
mov ax, 4200h
xor cx, cx
mov dx, 17h
int 21h
jc @@10
mov cx, 1
mov dx, offset AuxHotKey
mov ah, 40h
int 21h
jc @@10
mov ah, 3eh
int 21h
@@10:
ret

; -----------------------------------------------------------------------
GetRunFileName:
; Return:
; DS:DX Pointer of this run file name ASCIIZ string
push ax
push bx
push cx
push si
push di
push es

push cs
pop es
mov ax, es:[2ch]
mov es, ax
xor di, di
mov cx, 1000h
xor al, al
@@1: repnz scasb
cmp es:[di], al
loopnz @@1
mov dx, di
add dx, 3
push es
pop ds

pop es
pop di
pop si
pop cx
pop bx
pop ax
ret

; ---------------------------------------------------------------------------
GetMachineID:
push es
mov KBD102,True
mov ax,40h
mov es,ax
test byte ptr es:[96h], 00010000b
jnz @@1
mov Kbd102,False
@@1:
xor ax,ax
dec ax
mov es,ax
mov al,es:[0eh]
mov cs:MachineID, al
pop es
ret

; ---------------------------------------------------------------------------
ModifyHotKeyPrompt:
cmp cs:Kbd102, True
jz @@9
push cs
pop es
push cs
pop ds
mov cx, 124
mov si, offset KMsg2
mov di, offset KMsg1
rep movsb
@@9: cmp cs:MachineID, 0fch
jna @@10
mov cs:clsStrcolor, 70h ; Mono
mov cs:clsStr, 70h
@@10:
ret

; ---------------------------------------------------------------------------
PrintHotKeyPrompt:
Print Msg1
mov al, cs:HotKey
mov ah, al
shr al, 1
shr al, 1
and ax, 33ch
or al, ah
mov dx, offset KeyMsg
@@40:
or ax, ax ; Mr. Lei 4/25/1993
jz @@_42
shr al, 1
push ax
jnc @@41

push ax
call ColorDisplayStr
; mov ah, 9
; int 21h
pop ax

or al, al
jz @@42

push dx
mov dx, offset PlusMsg
call ColorDisplayStr
; Print PlusMsg
pop dx

@@41: add dx, 12
pop ax
jmp @@40
@@42: pop ax
@@_42: cmp cs:AuxHotKey, 0
jz @@43 cmp cs:HotKey, 0 ; Mr. Lei
jz @@_43
mov dx, offset PlusMsg
call ColorDisplayStr
; Print PlusMsg
@@_43: mov dx, offset AuxHotKeyName
call ColorDisplayStr
; Print AuxHotKeyName
@@43:
Print crlf
ret

ColorDisplayStr:
push bx
push cx
push dx
push si
mov bl, 0fh
mov si, dx
xor bh, bh
mov cx, 1
@@1: lodsb
cmp al, '$'
jz @@2
or al, al
jz @@2
push cx
mov ah, 09h
int 10h
mov ah, 3 int 10h
inc dl
mov ah, 2 int 10h
pop cx
jmp short @@1
@@2:
pop si
pop dx
pop cx
pop bx
ret

; ---------------------------------------------------------------------------
CmpSideKick:
xor ax, ax
mov es, ax
les bx, es:[20h]
cmp word ptr es:[bx-4], 4b53h
jnz @@1 cmp word ptr es:[bx-2], 4942h
jz @@2
@@1: mov es, ax
les bx, es:[94h]
cmp word ptr es:[bx-2], 4b53h
jz @@2
ret
@@2: or cs:Status, SKbit
ret

; ---------------------------------------------------------------------------
CmpDosVer: mov ah, 30h
int 21h
cmp al, 3
jb @@1 cmp al, 3
jna @@2
mov cs:cvtOfs, 1
ret
@@2: mov cs:cvtOfs, 0
ret
@@1: Print DosVerErr
mov ax, 4cffh
int 21h

DosVerErr db 'Sorry, DOS version too lower !',0dh,0ah,'$'

HotKeyValid:
cmp cs:HotKey, 0
jnz @@_1
cmp cs:AuxHotKey, 0
jnz @@_1
Print HotKeyErr
mov ax, 4cfeh
int 21h
@@_1: ret

HotKeyErr db 'Sorry, please setup hotkey again. ',0dh,0ah,'$'

eof:
ends
end Start

; ------------- The End ! ---------------------------------------------------
```。

接下来要做的，就是接住它，然后，把故事讲下去。

# WebAssembly（Wasm）到底适合做什么？一篇文章带你判断、选择与实战

如果你还不太熟悉 Wasm，可以先通过几个实际项目感受一下它的能力：

- 3D 游戏：https://files.dl.it.unity3d.com/jonas/AngryBots/
- 图片压缩：https://squoosh.app/
- 图片背景移除：https://github.com/imgly/background-removal-js
- Wasm 项目合集：https://github.com/mbasso/awesome-wasm

Wasm 并不是“什么都应该用”的万能方案。它更像是一件特殊工具：用对地方，能显著提升性能；用错地方，反而会增加项目复杂度、加载时间和维护成本。

# 哪些情况下适合使用 Wasm？

## 你具备一定技术基础时，可以从这几个角度判断

### 1. 项目属于计算密集型任务

如果某项功能需要进行大量计算，Wasm 往往比单纯使用 JavaScript 更有优势。常见场景包括：

- 音视频编码与解码、视频滤镜、分块渲染
- 加密算法、文件压缩与解压
- 在浏览器端运行 AI 模型
- 图像处理、复杂数据转换等高负载任务

举个例子：如果你的 MVP 使用 Vercel 加 Supabase 搭建，但产品里又需要完成视频剪辑，那么可以考虑使用 `ffmpeg.wasm`。这样，视频处理逻辑能够直接运行在浏览器中，不必额外部署一台服务器去执行 FFmpeg。

### 2. 需要复用成熟的 C/C++/Rust 代码

有些能力已经在其他语言生态中发展得非常成熟，性能也经过长期验证。这时，与其重新用 JavaScript 实现一遍，不如直接把现有代码编译成 Wasm。

现在，Rust、Go、Kotlin 等语言都已经具备较完善的 Wasm 支持，迁移和编译的门槛比过去低了很多。

### 3. 对代码隔离和安全性要求较高

Wasm 的一个重要特性，就是运行环境天然具备沙盒属性。默认情况下，它不能随意访问宿主机的文件系统或网络资源。

因此，如果你的 SaaS 产品允许用户上传并执行自定义脚本，但又不希望搭建复杂的容器隔离体系，Wasm 会是一个值得考虑的方案。

对于特别关注用户隐私和数据安全的场景，尤其是欧美市场中的部分应用，Wasm 也有较明显的优势。

## 如果你不懂技术，可以这样判断

不懂底层原理，也不代表无法判断是否适合使用 Wasm。你可以直接借助 AI 进行分析。

如果你已经做完了一些复杂功能，而且这些功能与页面布局、交互逻辑没有太大关系，可以向 AI 提问：

> 我当前的项目中，有哪些部分适合通过 Wasm 提升性能？如果使用 Wasm 的收益不明显，请不要强行推荐。

如果你还没有开始开发某个功能，也可以这样问：

> 我准备实现 xxx 功能，这个功能比较复杂，是否适合使用 Wasm？如果没有明显必要，请不要为了使用 Wasm 而使用它。

重点是，最好在问题中强调“没有必要就不要使用”，避免 AI 把 Wasm 当作默认答案。

# 哪些情况下不建议使用 Wasm？

### 1. 页面展示和交互逻辑

与页面结构、样式、表单、交互相关的代码，通常直接使用 JavaScript 更合适。

如果为了处理 DOM 和页面逻辑，反而让 Wasm 参与其中，那么它原本的性能优势很可能会被通信和数据转换开销抵消。

### 2. 首页加载路径中的重型功能

Wasm 文件往往不小，几十 MB 并不罕见。用户访问首页时如果必须先下载 Wasm，首屏速度、用户体验以及 SEO 都可能受到影响。

如果项目确实离不开 Wasm，可以考虑延迟加载、按需加载等方式。你也可以询问 AI：

> 我的项目使用了 Wasm，但我不希望它影响页面加载速度，请帮我设计一套优化方案。

### 3. 处理规模超过浏览器限制的数据

在浏览器环境中，Wasm 通常最多可使用约 4GB 内存。如果你的任务需要处理超过这一规模的数据，就不适合继续依赖浏览器端 Wasm。

总之，Wasm 只是技术选项之一。不要因为手里有一把“锤子”，就把所有问题都当成“钉子”。只有在收益明确时，才值得引入它。

# Wasm 应该怎么使用？

通常有三条路线：

1. 直接使用别人已经编译好的 Wasm 库
2. 通过 NPM 安装并集成
3. 自己编写代码，再编译成 Wasm

## 第一种方式：直接使用现成库

许多成熟能力已经有现成的 Wasm 实现，比如前面提到的图像处理、音视频处理等。

想确认某个功能是否已有可用方案，最简单的方式就是让 AI 帮你搜索和判断。

使用第三方 Wasm 库时，常见的接入方式主要有两种。

### 方案一：通过 CDN 引入

部分 Wasm 项目会提供官方 CDN，也有一些由第三方提供 CDN 资源。你可以先询问 AI：

> 帮我查一下 xxx 的 Wasm 是否有可以直接使用的 CDN。

确定地址后，再告诉 AI：

> 我希望通过 CDN 引入这个 Wasm，地址是 xxx，请帮我完成项目配置。

#### 使用 CDN 的好处

1. **降低打包体积**：Wasm 文件通常比较大，不放进项目产物可以明显减小应用体积。
2. **支持按需下载**：只有用户真正使用某项功能时，才加载对应文件，例如导出视频时再下载。
3. **便于缓存**：CDN 资源可以被浏览器长期缓存，不同项目也可能共享同一份文件。
4. **减少构建配置问题**：部分构建工具处理 Wasm 时存在兼容性差异，使用外部资源可以绕开一部分问题。

#### CDN 的潜在问题

1. **依赖外部服务**：CDN 出现故障时，相关功能可能无法使用。
2. **版本可能不同步**：项目依赖中的版本与代码里写死的 CDN 版本，可能出现不一致。
3. **无法保证离线使用**：没有网络连接时，浏览器无法获取 CDN 文件。

#### CDN 到底是什么？

可以把 CDN 理解成“分布在世界各地的静态文件仓库”。

假设你的服务器在美国，而用户位于杭州。如果每次访问都要跨越太平洋下载图片、JS、CSS 或 Wasm，速度自然会受到影响。

CDN 会把这些文件复制到全球多个加速节点。用户访问时，系统会优先从距离较近的节点获取资源，从而减少网络延迟。

你可以将自己的文件上传到 CDN，也可以直接使用其他服务提供的公共 CDN 文件。

### 实战：用 ffmpeg.wasm 做一个视频剪辑页面

接下来可以用 `ffmpeg.wasm` 制作一个简单的视频编辑工具。

最终效果示例：

https://video-editor-wasm-nine.vercel.app/

![](img/38adee99faefe3336e51398c2e279a73.png)

实现方式并不复杂。打开 V0、Bolt.new、same.new、Cursor 或 Claude Code 等 AI 开发工具，新建项目，然后输入下面的提示词：

```
# 开发一个基于 WebAssembly 的在线视频编辑器

## 项目概述
请开发一个单页 Web 应用，让用户可以在浏览器中编辑视频，无需上传到服务器。所有视频处理都在客户端通过 ffmpeg.wasm 完成。

## 核心功能要求
1\. **视频导入**
   - 支持拖拽上传和点击选择
   - 支持多个视频文件（每个最大 100MB）
   - 显示视频缩略图和时长

2\. **视频编辑**
   - 时间轴上可视化显示所有视频片段
   - 支持拖拽调整视频顺序
   - 支持拖拽两端手柄裁剪视频（调整起始和结束时间）
   - 实时显示裁剪时间

3\. **音频功能**
   - 支持添加一个背景音乐轨道
   - 可以调整音频的起始偏移时间
   - 音频轨道可视化显示在时间轴上

4\. **预览播放**
   - 实时预览编辑后的效果
   - 播放/暂停控制
   - 进度条拖动
   - 支持空格键快捷键

5\. **视频导出**
   - 使用 ffmpeg.wasm 在浏览器端处理
   - 支持选择输出分辨率（源视频/720p/1080p）
   - 显示导出进度条
   - 自动下载生成的 MP4 文件

## 技术栈要求
- **框架**: React 18 + TypeScript
- **构建工具**: Vite
- **状态管理**: Zustand
- **样式**: Tailwind CSS
- **拖拽**: @dnd-kit/core + @dnd-kit/sortable
- **视频处理**: @ffmpeg/ffmpeg (WebAssembly)
- **路由**: React Router DOM

## UI 布局

┌─ 工具栏 ─────────────────────┐
│ [导入] [导出] [撤销] [重做] │ 
└──────────────────────────┘ 
┌─ 资源面板(25%) ─┬─ 预览区(75%) ─────────┐ 
│ 视频列表 │ 视频预览画面 │ │ 音频轨道 │ 播放控制条 │ 
└─────────────────┴───────────┘ 
┌─ 时间轴 ───────────────────────────┐ 
│ 视频轨道: [片段1][片段2][片段3] │ │ 音频轨道: [背景音乐] │ 
└────────────────────────────────┘

## 实现细节
1\. **文件处理**
   - 使用 File API 读取视频文件
   - 生成视频缩略图
   - 获取视频元数据（时长等）

2\. **时间轴交互**
   - 视频片段中间区域：拖拽排序
   - 视频片段两端：拖拽裁剪
   - 音频轨道：拖拽调整偏移

3\. **ffmpeg.wasm 集成**
   - 从 CDN 加载（unpkg.com）
   - 处理视频裁剪、拼接、音频混合
   - 使用 Web Worker 避免阻塞主线程（可选）

4\. **响应式设计**
   - 支持桌面和移动设备
   - 触摸手势支持
   - 自适应布局

5\. **性能优化**
   - 视频文件保存在内存中
   - 使用 blob URL 管理
   - 及时释放不用的资源

## 错误处理
- 文件大小限制提示
- 不支持的格式提示
- 导出失败的友好提示
- 加载状态显示

## 部署配置
- 配置 CORS 头支持 SharedArrayBuffer
- 添加 netlify.toml 配置文件
- 确保 ffmpeg.wasm 可以正常加载

请使用现代的 React Hooks 和函数组件开发，确保代码类型安全，并提供良好的用户体验。

## 开发顺序建议
1\. 先搭建基础项目结构和 UI 布局
2\. 实现视频导入和预览功能
3\. 添加时间轴和拖拽功能
4\. 实现视频裁剪功能
5\. 添加音频轨道支持
6\. 最后实现 ffmpeg.wasm 导出功能

## 常见问题解决
- 如果 ffmpeg Worker 加载失败，可以改用直接加载方式
- 视频裁剪和拖拽冲突时，需要分离交互区域
- 音频导出时注意 itsoffset 参数的位置

## 测试要点
- 测试多个视频的拼接
- 测试视频裁剪的准确性
- 测试音频同步
- 测试不同格式的兼容性
```

接下来让 AI 继续完成代码即可。

需要注意的是，AI 生成的第一版往往会存在不少问题。遇到报错或功能异常时，把具体问题逐项反馈给 AI，让它逐步修复即可。整个过程与开发普通网页应用没有本质区别。

项目部署到 Vercel 的流程，也基本和一般前端项目一致。

## 第二种方式：通过 NPM 安装（更推荐）

如果某个 Wasm 库提供 NPM 包，通常可以像安装普通依赖一样将它加入项目。

具体配置不必全部手写，直接让 AI 生成即可。

需要特别提醒的是：如果一个库同时提供 NPM 和 CDN 两种版本，一定要明确告诉 AI 你希望使用哪一种，否则它可能自行选择，导致项目配置和你的预期不一致。

### NPM 方式的优点

1. **支持离线运行**：不依赖外部网络，应用可以在离线环境中工作。
2. **版本更可控**：版本由 `package.json` 管理，不容易出现 CDN 与项目依赖不一致的问题。
3. **构建阶段更容易发现问题**：Wasm 文件缺失或配置错误，通常能在构建时暴露出来。
4. **减少外部服务依赖**：不受 CDN 故障影响。
5. **适合企业内网环境**：即使存在网络限制，也可以正常部署和使用。

### NPM 方式的不足

1. **最终产物可能非常大**：Wasm 文件常见体积在 20-50MB 左右。
2. **首次访问速度较慢**：用户可能需要先下载完整资源才能使用功能。
3. **内存占用更高**：加载 Wasm 后会占用额外内存。
4. **构建配置更复杂**：需要正确处理 Vite、Webpack 等工具对 Wasm 的支持。
5. **更新后的缓存利用率可能较低**：应用重新发布后，用户可能需要重新下载相关文件。

### 实战：使用本地 Wasm 运行语音识别

这次我们不调用远程 API，而是在浏览器本地运行开源 Whisper 模型，将语音转换成文字。

示例项目：

https://whisper-webgpu-demo.vercel.app/

创建一个新文件夹，打开 Cursor，然后输入下面的提示词：

```
Whisper WebGPU 语音识别应用开发 Prompt

  请帮我开发一个基于 WebGPU 的浏览器端中文语音识别应用，具体要求如下：

  核心功能需求

  1\. 语音识别功能：使用 Xenova/whisper-small 模型进行中文语音识别
  2\. WebGPU 加速：优先使用 WebGPU，不支持时自动降级到 WASM
  3\. 录音功能：支持浏览器内录音，自动重采样到 16kHz
  4\. 流式输出：转写过程中实时显示识别结果
  5\. 模型缓存：使用浏览器 Cache API 缓存模型文件（约244MB），避免重复下载

  技术栈要求

  - 框架：使用 Webpack 5 作为构建工具
  - 语言：TypeScript（严格模式）
  - 样式：Tailwind CSS
  - 依赖：@xenova/transformers 库
  - 目标环境：现代浏览器，ES2020

  项目结构

  src/
  ├── index.ts        # 主入口，UI交互和流程控制
  ├── whisper.ts      # Whisper模型封装
  ├── recorder.ts     # 音频录制和处理
  ├── cache-utils.ts  # 缓存管理工具
  └── styles.css      # Tailwind CSS样式

  详细实现要求

  1\. WhisperModel 类 (whisper.ts)

  - 封装 @xenova/transformers 的 pipeline API
  - 检测 WebGPU 支持（navigator.gpu）
  - 初始化时显示下载进度
  - transcribe 方法支持流式回调输出
  - 配置：language='zh', task='transcribe', chunk_length_s=30

  2\. AudioRecorder 类 (recorder.ts)

  - 使用 MediaRecorder API 录音
  - 配置：48kHz采样率，单声道，开启降噪和回声消除
  - stop 方法返回 Blob 并停止所有音轨
  - resampleTo16kHz 方法：使用 Web Audio API 重采样到 16kHz

  3\. 缓存管理 (cache-utils.ts)

  - checkModelCacheExists：检查 'transformers-cache' 是否存在
  - clearModelCache：清理缓存并刷新页面

  4\. UI 界面 (index.html)

  - 简洁的单页应用布局
  - 顶部：标题 + 清理缓存按钮
  - 中间：文字输出区域（带滚动）
  - 底部：下载模型/开始录音/停止录音按钮
  - 进度条：模型下载进度
  - 警告提示：WebGPU 不可用时显示

  5\. 主逻辑 (index.ts)

  - 页面加载时检查缓存，存在则自动加载模型
  - 下载模型：显示进度条，完成后隐藏
  - 录音流程：开始录音 → 停止录音 → 重采样 → 转写 → 显示结果
  - 错误处理：友好的错误提示

  特殊配置

  Webpack 配置重点：

  devServer: {
    headers: {
      'Cross-Origin-Embedder-Policy': 'require-corp',
      'Cross-Origin-Opener-Policy': 'same-origin',
    }
  }

  复制 WASM 文件：

  new CopyPlugin({
    patterns: [{
      from: 'node_modules/onnxruntime-web/dist/*.wasm',
      to: '[name][ext]'
    }]
  })

  开发命令

  - npm run dev - 启动开发服务器（端口8080）
  - npm run build - 构建生产版本
  - npm run clean - 清理构建目录

  用户体验要求

  1\. 首次使用需下载模型，显示进度
  2\. 模型加载后自动缓存，下次无需下载
  3\. 录音时显示"正在录音..."
  4\. 转写时实时显示识别文字
  5\. 无语音时提示"未检测到语音内容"
  6\. WebGPU不可用时显示降级提示

  请按照以上要求，一步步实现这个语音识别应用。先创建项目结构，再逐个实现各个模块。
```

为了减少兼容性问题，这个项目采用相对传统的 Webpack 进行构建，而不是 Vite。

Vite 同样可以实现，但可能需要花费更多时间处理相关兼容配置。后续开发流程与普通 Web 项目类似。

由于该项目使用的并不是 Next.js，可以额外询问 AI：

> 这个项目是否可以直接部署到 Vercel？如果不能，请帮我补充必要配置。

## 第三种方式：自己编写并编译 Wasm

如果你希望自己实现某些计算逻辑，就需要编写源代码，再将其编译为 Wasm。

以前，选择开发语言时，通常会优先考虑自己最熟悉的语言。但在 AI 辅助开发越来越普及的今天，非资深程序员不一定需要把大量精力放在语法细节上，更重要的是把需求、数据流和业务逻辑讲清楚。

目前常用于开发 Wasm 的语言主要包括：

- C++
- Rust
- TypeScript / JavaScript

TypeScript 和 JavaScript 受欢迎，主要是因为前端开发者对它们最熟悉。

C++ 的优势在于性能强、历史悠久、开发者数量多，但它的工程复杂度较高，也更容易出现内存相关问题。

Rust 则是凭借自身实力获得广泛认可：它拥有很强的性能、相对优雅的语法，并且能够在编译阶段避免许多常见错误。

如果你使用 AI 辅助编写代码，同时又不把“是否熟悉语法”作为首要条件，那么 Rust 往往是一个非常值得优先考虑的选择。

### 小知识：Stack Overflow 的语言偏好调查

在相关统计图中，蓝色通常代表“未来计划使用”，红色标记则表示“过去一年使用过，并且仍然愿意继续使用”。

从图表可以看出，Rust 的认可度非常高。

![](img/ec90fe412512ddd6143487a7569d3379.png)

### 实战：用 Rust 编写图像处理 Wasm 工具

下面以 Rust 为例，其他语言的整体思路也类似。

我们要制作的是一个运行在浏览器中的图像处理工具，不依赖远程 API，就可以完成多种图片操作。

示例项目：

https://wasm-image-demo.vercel.app/

这里先展示其中三项功能，实际上，基于 Wasm 还能扩展出更多图像处理能力。

![](img/b45e0cc1500f0c70a8b70b8c3c76b1c2.png)

接下来，我们从零开始创建一个属于自己的 Wasm 项目。

#### 第一步：建立 Web 项目

使用 V0、Bolt.new、same.new、Cursor 或 Claude Code 等 AI 开发工具创建新项目。

先把上面的功能示意图上传给 AI，再输入以下提示词：

```
帮我开发一个简单的页面，页面的功能如图所示。使用next.js作为框架。你当前只需要参考截图，实现这个页面的布局，不需要实现具体的功能。
```

#### 把项目先拉到本地

如果你现在用的是 V0、Bolt.new 或者 same.new 这类在线编辑器，第一步先把工程同步到 git 仓库，然后在本地执行 git clone 把代码拿下来。

用 Cursor、VS Code 等编辑器打开本地项目后，在项目根目录下新建一个文件夹，名字随意，常见的叫法是「rust-wasm」。

![](img/16c8b05d121f6c7709bea6c4bf0c6b2f.png)

#### 让 AI 来写核心的 Wasm 逻辑

直接把下面这段需求提示丢给 AI，让它帮你生成对应的 Rust Wasm 代码：

```
请你帮我在`rust-wasm`路径下，使用rust语言和photon-rs库，开发一下wasm功能，主要的功能包括灰度滤镜、高斯模糊、边缘检测。
参考代码：
```

use wasm_bindgen::prelude::*;

use photon_rs::{PhotonImage, monochrome, conv};

#[wasm_bindgen]

pub fn apply_grayscale(raw_pixels: Vec, width: u32, height: u32) -> Vec <u8>{

    let mut photon_image = PhotonImage::new(raw_pixels, width, height);

    monochrome::grayscale(&mut photon_image);

    photon_image.get_raw_pixels()

}

#[wasm_bindgen]

pub fn apply_blur(raw_pixels: Vec<u8>, width: u32, height: u32) -> Vec <u8>{

    let mut photon_image = PhotonImage::new(raw_pixels, width, height);

    conv::gaussian_blur(&mut photon_image, 5);

    photon_image.get_raw_pixels()

}

#[wasm_bindgen]

pub fn apply_edge_detection(raw_pixels: Vec<u8>, width: u32, height: u32) -> Vec <u8>{

    let mut photon_image = PhotonImage::new(raw_pixels, width, height);

    conv::edge_detection(&mut photon_image);

    photon_image.get_raw_pixels()

}

```
开发完成后，需要增加一个`rust-wasm/build.sh`脚本，来编译成wasm并放置到合适的路径下。这个脚本文件请你设置成可执行。
参考代码：
```

#!/bin/bash

wasm-pack build --target bundler --out-dir ../lib/wasm

```
注意，我本地可能没有安装rustc和wasm-pack，如果你发现我没有安装，请你使用rustup帮我安装一下。</u8></u8></u8></u8></u8>
```

注意，上面附带的代码只是参考，实际让 AI 开发时完全可以不依赖这些示例，它自己也能搞定。加上示例主要是为了提升生成的准确率。

#### 编译 Rust 为 Wasm

完成代码编写后，通常会多出一个 `build.sh` 脚本。打开终端，进入项目目录执行：

```
cd rust-wasm && ./build.sh
```

稍等片刻即可完成编译。如果编译过程中报错，把错误日志直接丢给 AI 让它修复，循环直至编译成功。

#### 在本地调试 Wasm

本地调试的方式和普通前端项目一致，执行 `npm run dev` 启动服务后打开页面即可。

Wasm 的日志输出同样会打印到浏览器控制台里。如果你想在 Rust 里使用 console.log，需要做一点小配置。可以把下面这段提示发给 AI：

```
我需要在浏览器中打印日志来调试问题，请你增加可以在浏览器中打印日志的方法。

示例代码：
```

use wasm_bindgen::prelude::*;

  // 绑定console.log

  #[wasm_bindgen]

  extern "C" {

      #[wasm_bindgen(js_namespace = console)]

      fn log(s: &str);

  }

  // 创建宏简化使用

  macro_rules! console_log {

      ($($t:tt)*) => (log(&format_args!($($t)*).to_string()))

  }

  #[wasm_bindgen]

  pub fn process_image() {

      console_log!("开始处理图像...");

      // 你的代码

      console_log!("图像处理完成");

  }

```
```

在定位问题时可以告诉 AI：

```
我发现了xxx问题。你可以增加一些日志来调试这个问题，日志打印到浏览器的方法我之前已经写好了，你按那个方式来添加日志。
```

每次改完 Rust 代码并不会立刻生效，必须重新执行一遍构建，也就是再跑一次上面的 build.sh。若不想手动重复操作，可以让 AI 帮你加上自动编译。这个需求可以直接用下面提示词：

```
我希望每次修改完rust代码，都可以自动重新编译。请你帮我配置一下吧。

参考代码（package.json）：
  {
    "scripts": {
      "dev:wasm": "chokidar 'rust-wasm/src/**/*.rs' -c 'npm run build:wasm'",
      "dev:next": "next dev",
      "dev": "concurrently 'npm run dev:wasm' 'npm run dev:next'"
    },
    "devDependencies": {
      "chokidar-cli": "^3.0.0",
      "concurrently": "^7.6.0"
    }
  }
```

#### 提交代码并部署到 Vercel

想在 Vercel 上使用自己写的 Wasm，一般有两种思路：

1.  把已经编译好的 Wasm 文件直接塞进 public 目录一起提交到 git。优点是部署零配置，缺点是 Wasm 包体积偏大，会拖慢仓库历史记录。
2.  只上传源码，不上传编译产物，让 Vercel 在部署时自动编译。推荐使用第二种方式。

下面是第二种方式的配置方法。把下面提示词发给 AI，让它帮你完成部署脚本的编写：

```
我的项目准备部署在vercel上面。我当前的项目包含rust的wasm，因此在npm编译的时候需要特殊设置一下，确保在vercel编译的时候能够连同wasm一起编译。
参考代码：
增加一个build-wasm.sh:
```

#!/bin/bash

set -e

echo "Building WASM module..."

# Install Rust if not already installed

if ! command -v rustc &> /dev/null; then

    echo "Installing Rust..."

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

    source ~/.cargo/env

fi

# Install wasm-pack if not already installed

if ! command -v wasm-pack &> /dev/null; then

    echo "Installing wasm-pack..."

    curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh

fi

# Add wasm32 target if not already added

rustup target add wasm32-unknown-unknown

# Build WASM module

cd rust-wasm

chmod +x build.sh

./build.sh

cd ..

echo "WASM module built successfully!"

```
然后修改package.json:
```

  "scripts": {

    "dev": "next dev --turbopack",

    "prebuild": "./build-wasm.sh",

    "build": "next build",

    "start": "next start",

    "lint": "next lint"

  },

```
```

#### 恭喜你，第一个自研的 Wasm 工具就这样做出来了！

# 使用 Wasm 时常见的坑

*   部分 Wasm 包与 Vite 存在兼容性问题。
    解决办法：让 AI 帮你安装对应的适配插件即可。
*   文件体积过大导致加载缓慢。
    解决办法：让 AI 帮你加上懒加载逻辑，避免首屏加载。
*   Safari 上偶现不兼容。
    这并不是 Wasm 本身的缺陷，Safari 的行为本就和 Chrome 有差异，属于浏览器特性问题。

# 最后说两句

非常感谢龙哥盟这个社区，给了我很多宝贵的思路和灵感。希望能把这些经验也分享出来，帮助更多人。

AI 的浪潮已经来临，能不能抓住机会，就看谁动作更快。祝大家都能在这一波里龙哥盟！