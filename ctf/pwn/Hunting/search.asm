
search:     file format elf32-i386


Disassembly of section .text:

00000000 <search>:
   0:	55                   	push   %ebp
   1:	89 e5                	mov    %esp,%ebp
   3:	83 ec 18             	sub    $0x18,%esp
   6:	c7 45 f4 00 00 00 60 	movl   $0x60000000,-0xc(%ebp)
   d:	eb 66                	jmp    75 <search+0x75>
   f:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
  16:	eb 4a                	jmp    62 <search+0x62>
  18:	8b 55 f4             	mov    -0xc(%ebp),%edx
  1b:	8b 45 f0             	mov    -0x10(%ebp),%eax
  1e:	01 d0                	add    %edx,%eax
  20:	83 ec 08             	sub    $0x8,%esp
  23:	6a 00                	push   $0x0
  25:	50                   	push   %eax
  26:	e8 fc ff ff ff       	call   27 <search+0x27>
  2b:	83 c4 10             	add    $0x10,%esp
  2e:	83 f8 f2             	cmp    $0xfffffff2,%eax
  31:	74 3a                	je     6d <search+0x6d>
  33:	8b 55 f4             	mov    -0xc(%ebp),%edx
  36:	8b 45 f0             	mov    -0x10(%ebp),%eax
  39:	01 d0                	add    %edx,%eax
  3b:	8b 00                	mov    (%eax),%eax
  3d:	3d 48 54 42 7b       	cmp    $0x7b425448,%eax
  42:	75 1a                	jne    5e <search+0x5e>
  44:	8b 55 f4             	mov    -0xc(%ebp),%edx
  47:	8b 45 f0             	mov    -0x10(%ebp),%eax
  4a:	01 d0                	add    %edx,%eax
  4c:	83 ec 04             	sub    $0x4,%esp
  4f:	6a 24                	push   $0x24
  51:	50                   	push   %eax
  52:	6a 01                	push   $0x1
  54:	e8 fc ff ff ff       	call   55 <search+0x55>
  59:	83 c4 10             	add    $0x10,%esp
  5c:	eb 20                	jmp    7e <search+0x7e>
  5e:	83 45 f0 04          	addl   $0x4,-0x10(%ebp)
  62:	81 7d f0 ff 0f 00 00 	cmpl   $0xfff,-0x10(%ebp)
  69:	76 ad                	jbe    18 <search+0x18>
  6b:	eb 01                	jmp    6e <search+0x6e>
  6d:	90                   	nop
  6e:	81 45 f4 00 10 00 00 	addl   $0x1000,-0xc(%ebp)
  75:	81 7d f4 00 00 00 f7 	cmpl   $0xf7000000,-0xc(%ebp)
  7c:	76 91                	jbe    f <search+0xf>
  7e:	c9                   	leave  
  7f:	c3                   	ret    

Disassembly of section .comment:

00000000 <.comment>:
   0:	00 47 43             	add    %al,0x43(%edi)
   3:	43                   	inc    %ebx
   4:	3a 20                	cmp    (%eax),%ah
   6:	28 47 4e             	sub    %al,0x4e(%edi)
   9:	55                   	push   %ebp
   a:	29 20                	sub    %esp,(%eax)
   c:	31 32                	xor    %esi,(%edx)
   e:	2e 32 2e             	xor    %cs:(%esi),%ch
  11:	30 00                	xor    %al,(%eax)

Disassembly of section .note.gnu.property:

00000000 <.note.gnu.property>:
   0:	04 00                	add    $0x0,%al
   2:	00 00                	add    %al,(%eax)
   4:	18 00                	sbb    %al,(%eax)
   6:	00 00                	add    %al,(%eax)
   8:	05 00 00 00 47       	add    $0x47000000,%eax
   d:	4e                   	dec    %esi
   e:	55                   	push   %ebp
   f:	00 02                	add    %al,(%edx)
  11:	00 01                	add    %al,(%ecx)
  13:	c0 04 00 00          	rolb   $0x0,(%eax,%eax,1)
  17:	00 00                	add    %al,(%eax)
  19:	00 00                	add    %al,(%eax)
  1b:	00 01                	add    %al,(%ecx)
  1d:	00 01                	add    %al,(%ecx)
  1f:	c0 04 00 00          	rolb   $0x0,(%eax,%eax,1)
  23:	00 01                	add    %al,(%ecx)
  25:	00 00                	add    %al,(%eax)
	...

Disassembly of section .eh_frame:

00000000 <.eh_frame>:
   0:	14 00                	adc    $0x0,%al
   2:	00 00                	add    %al,(%eax)
   4:	00 00                	add    %al,(%eax)
   6:	00 00                	add    %al,(%eax)
   8:	01 7a 52             	add    %edi,0x52(%edx)
   b:	00 01                	add    %al,(%ecx)
   d:	7c 08                	jl     17 <.eh_frame+0x17>
   f:	01 1b                	add    %ebx,(%ebx)
  11:	0c 04                	or     $0x4,%al
  13:	04 88                	add    $0x88,%al
  15:	01 00                	add    %eax,(%eax)
  17:	00 1c 00             	add    %bl,(%eax,%eax,1)
  1a:	00 00                	add    %al,(%eax)
  1c:	1c 00                	sbb    $0x0,%al
  1e:	00 00                	add    %al,(%eax)
  20:	00 00                	add    %al,(%eax)
  22:	00 00                	add    %al,(%eax)
  24:	80 00 00             	addb   $0x0,(%eax)
  27:	00 00                	add    %al,(%eax)
  29:	41                   	inc    %ecx
  2a:	0e                   	push   %cs
  2b:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
  31:	02 7c c5 0c          	add    0xc(%ebp,%eax,8),%bh
  35:	04 04                	add    $0x4,%al
	...
