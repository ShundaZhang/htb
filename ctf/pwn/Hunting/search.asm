
search:     file format elf32-i386


Disassembly of section .interp:

08048194 <.interp>:
 8048194:	2f                   	das    
 8048195:	6c                   	insb   (%dx),%es:(%edi)
 8048196:	69 62 2f 6c 64 2d 6c 	imul   $0x6c2d646c,0x2f(%edx),%esp
 804819d:	69 6e 75 78 2e 73 6f 	imul   $0x6f732e78,0x75(%esi),%ebp
 80481a4:	2e 32 00             	xor    %cs:(%eax),%al

Disassembly of section .note.ABI-tag:

080481a8 <.note.ABI-tag>:
 80481a8:	04 00                	add    $0x0,%al
 80481aa:	00 00                	add    %al,(%eax)
 80481ac:	10 00                	adc    %al,(%eax)
 80481ae:	00 00                	add    %al,(%eax)
 80481b0:	01 00                	add    %eax,(%eax)
 80481b2:	00 00                	add    %al,(%eax)
 80481b4:	47                   	inc    %edi
 80481b5:	4e                   	dec    %esi
 80481b6:	55                   	push   %ebp
 80481b7:	00 00                	add    %al,(%eax)
 80481b9:	00 00                	add    %al,(%eax)
 80481bb:	00 03                	add    %al,(%ebx)
 80481bd:	00 00                	add    %al,(%eax)
 80481bf:	00 02                	add    %al,(%edx)
 80481c1:	00 00                	add    %al,(%eax)
 80481c3:	00 00                	add    %al,(%eax)
 80481c5:	00 00                	add    %al,(%eax)
	...

Disassembly of section .hash:

080481c8 <.hash>:
 80481c8:	03 00                	add    (%eax),%eax
 80481ca:	00 00                	add    %al,(%eax)
 80481cc:	06                   	push   %es
 80481cd:	00 00                	add    %al,(%eax)
 80481cf:	00 03                	add    %al,(%ebx)
 80481d1:	00 00                	add    %al,(%eax)
 80481d3:	00 02                	add    %al,(%edx)
 80481d5:	00 00                	add    %al,(%eax)
 80481d7:	00 04 00             	add    %al,(%eax,%eax,1)
	...
 80481e6:	00 00                	add    %al,(%eax)
 80481e8:	01 00                	add    %eax,(%eax)
 80481ea:	00 00                	add    %al,(%eax)
 80481ec:	05 00 00 00 00       	add    $0x0,%eax
 80481f1:	00 00                	add    %al,(%eax)
	...

Disassembly of section .gnu.hash:

080481f4 <.gnu.hash>:
 80481f4:	02 00                	add    (%eax),%al
 80481f6:	00 00                	add    %al,(%eax)
 80481f8:	05 00 00 00 01       	add    $0x1000000,%eax
 80481fd:	00 00                	add    %al,(%eax)
 80481ff:	00 05 00 00 00 00    	add    %al,0x0
 8048205:	20 00                	and    %al,(%eax)
 8048207:	20 00                	and    %al,(%eax)
 8048209:	00 00                	add    %al,(%eax)
 804820b:	00 05 00 00 00 ad    	add    %al,0xad000000
 8048211:	4b                   	dec    %ebx
 8048212:	e3 c0                	jecxz  80481d4 <_init-0xe2c>

Disassembly of section .dynsym:

08048214 <.dynsym>:
	...
 8048224:	43                   	inc    %ebx
	...
 804822d:	00 00                	add    %al,(%eax)
 804822f:	00 20                	add    %ah,(%eax)
 8048231:	00 00                	add    %al,(%eax)
 8048233:	00 17                	add    %dl,(%edi)
	...
 804823d:	00 00                	add    %al,(%eax)
 804823f:	00 12                	add    %dl,(%edx)
 8048241:	00 00                	add    %al,(%eax)
 8048243:	00 29                	add    %ch,(%ecx)
	...
 804824d:	00 00                	add    %al,(%eax)
 804824f:	00 12                	add    %dl,(%edx)
 8048251:	00 00                	add    %al,(%eax)
 8048253:	00 10                	add    %dl,(%eax)
	...
 804825d:	00 00                	add    %al,(%eax)
 804825f:	00 12                	add    %dl,(%edx)
 8048261:	00 00                	add    %al,(%eax)
 8048263:	00 01                	add    %al,(%ecx)
 8048265:	00 00                	add    %al,(%eax)
 8048267:	00 04 a0             	add    %al,(%eax,%eiz,4)
 804826a:	04 08                	add    $0x8,%al
 804826c:	04 00                	add    $0x0,%al
 804826e:	00 00                	add    %al,(%eax)
 8048270:	11 00                	adc    %eax,(%eax)
 8048272:	10 00                	adc    %al,(%eax)

Disassembly of section .dynstr:

08048274 <.dynstr>:
 8048274:	00 5f 49             	add    %bl,0x49(%edi)
 8048277:	4f                   	dec    %edi
 8048278:	5f                   	pop    %edi
 8048279:	73 74                	jae    80482ef <_init-0xd11>
 804827b:	64 69 6e 5f 75 73 65 	imul   $0x64657375,%fs:0x5f(%esi),%ebp
 8048282:	64 
 8048283:	00 61 63             	add    %ah,0x63(%ecx)
 8048286:	63 65 73             	arpl   %sp,0x73(%ebp)
 8048289:	73 00                	jae    804828b <_init-0xd75>
 804828b:	5f                   	pop    %edi
 804828c:	5f                   	pop    %edi
 804828d:	6c                   	insb   (%dx),%es:(%edi)
 804828e:	69 62 63 5f 73 74 61 	imul   $0x6174735f,0x63(%edx),%esp
 8048295:	72 74                	jb     804830b <_init-0xcf5>
 8048297:	5f                   	pop    %edi
 8048298:	6d                   	insl   (%dx),%es:(%edi)
 8048299:	61                   	popa   
 804829a:	69 6e 00 77 72 69 74 	imul   $0x74697277,0x0(%esi),%ebp
 80482a1:	65 00 6c 69 62       	add    %ch,%gs:0x62(%ecx,%ebp,2)
 80482a6:	63 2e                	arpl   %bp,(%esi)
 80482a8:	73 6f                	jae    8048319 <_init-0xce7>
 80482aa:	2e 36 00 47 4c       	cs add %al,%ss:0x4c(%edi)
 80482af:	49                   	dec    %ecx
 80482b0:	42                   	inc    %edx
 80482b1:	43                   	inc    %ebx
 80482b2:	5f                   	pop    %edi
 80482b3:	32 2e                	xor    (%esi),%ch
 80482b5:	30 00                	xor    %al,(%eax)
 80482b7:	5f                   	pop    %edi
 80482b8:	5f                   	pop    %edi
 80482b9:	67 6d                	insl   (%dx),%es:(%di)
 80482bb:	6f                   	outsl  %ds:(%esi),(%dx)
 80482bc:	6e                   	outsb  %ds:(%esi),(%dx)
 80482bd:	5f                   	pop    %edi
 80482be:	73 74                	jae    8048334 <_init-0xccc>
 80482c0:	61                   	popa   
 80482c1:	72 74                	jb     8048337 <_init-0xcc9>
 80482c3:	5f                   	pop    %edi
 80482c4:	5f                   	pop    %edi
	...

Disassembly of section .gnu.version:

080482c6 <.gnu.version>:
 80482c6:	00 00                	add    %al,(%eax)
 80482c8:	00 00                	add    %al,(%eax)
 80482ca:	02 00                	add    (%eax),%al
 80482cc:	02 00                	add    (%eax),%al
 80482ce:	02 00                	add    (%eax),%al
 80482d0:	01 00                	add    %eax,(%eax)

Disassembly of section .gnu.version_r:

080482d4 <.gnu.version_r>:
 80482d4:	01 00                	add    %eax,(%eax)
 80482d6:	01 00                	add    %eax,(%eax)
 80482d8:	2f                   	das    
 80482d9:	00 00                	add    %al,(%eax)
 80482db:	00 10                	add    %dl,(%eax)
 80482dd:	00 00                	add    %al,(%eax)
 80482df:	00 00                	add    %al,(%eax)
 80482e1:	00 00                	add    %al,(%eax)
 80482e3:	00 10                	add    %dl,(%eax)
 80482e5:	69 69 0d 00 00 02 00 	imul   $0x20000,0xd(%ecx),%ebp
 80482ec:	39 00                	cmp    %eax,(%eax)
 80482ee:	00 00                	add    %al,(%eax)
 80482f0:	00 00                	add    %al,(%eax)
	...

Disassembly of section .rel.dyn:

080482f4 <.rel.dyn>:
 80482f4:	fc                   	cld    
 80482f5:	bf 04 08 06 01       	mov    $0x1060804,%edi
	...

Disassembly of section .rel.plt:

080482fc <.rel.plt>:
 80482fc:	0c c0                	or     $0xc0,%al
 80482fe:	04 08                	add    $0x8,%al
 8048300:	07                   	pop    %es
 8048301:	02 00                	add    (%eax),%al
 8048303:	00 10                	add    %dl,(%eax)
 8048305:	c0 04 08 07          	rolb   $0x7,(%eax,%ecx,1)
 8048309:	03 00                	add    (%eax),%eax
 804830b:	00 14 c0             	add    %dl,(%eax,%eax,8)
 804830e:	04 08                	add    $0x8,%al
 8048310:	07                   	pop    %es
 8048311:	04 00                	add    $0x0,%al
	...

Disassembly of section .init:

08049000 <_init>:
 8049000:	53                   	push   %ebx
 8049001:	83 ec 08             	sub    $0x8,%esp
 8049004:	e8 c7 00 00 00       	call   80490d0 <__x86.get_pc_thunk.bx>
 8049009:	81 c3 f7 2f 00 00    	add    $0x2ff7,%ebx
 804900f:	8b 83 fc ff ff ff    	mov    -0x4(%ebx),%eax
 8049015:	85 c0                	test   %eax,%eax
 8049017:	74 05                	je     804901e <_init+0x1e>
 8049019:	e8 52 00 00 00       	call   8049070 <__gmon_start__@plt>
 804901e:	83 c4 08             	add    $0x8,%esp
 8049021:	5b                   	pop    %ebx
 8049022:	c3                   	ret    

Disassembly of section .plt:

08049030 <__libc_start_main@plt-0x10>:
 8049030:	ff 35 04 c0 04 08    	push   0x804c004
 8049036:	ff 25 08 c0 04 08    	jmp    *0x804c008
 804903c:	00 00                	add    %al,(%eax)
	...

08049040 <__libc_start_main@plt>:
 8049040:	ff 25 0c c0 04 08    	jmp    *0x804c00c
 8049046:	68 00 00 00 00       	push   $0x0
 804904b:	e9 e0 ff ff ff       	jmp    8049030 <_init+0x30>

08049050 <write@plt>:
 8049050:	ff 25 10 c0 04 08    	jmp    *0x804c010
 8049056:	68 08 00 00 00       	push   $0x8
 804905b:	e9 d0 ff ff ff       	jmp    8049030 <_init+0x30>

08049060 <access@plt>:
 8049060:	ff 25 14 c0 04 08    	jmp    *0x804c014
 8049066:	68 10 00 00 00       	push   $0x10
 804906b:	e9 c0 ff ff ff       	jmp    8049030 <_init+0x30>

Disassembly of section .plt.got:

08049070 <__gmon_start__@plt>:
 8049070:	ff 25 fc bf 04 08    	jmp    *0x804bffc
 8049076:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

08049080 <_start>:
 8049080:	31 ed                	xor    %ebp,%ebp
 8049082:	5e                   	pop    %esi
 8049083:	89 e1                	mov    %esp,%ecx
 8049085:	83 e4 f0             	and    $0xfffffff0,%esp
 8049088:	50                   	push   %eax
 8049089:	54                   	push   %esp
 804908a:	52                   	push   %edx
 804908b:	e8 23 00 00 00       	call   80490b3 <_start+0x33>
 8049090:	81 c3 70 2f 00 00    	add    $0x2f70,%ebx
 8049096:	8d 83 90 d2 ff ff    	lea    -0x2d70(%ebx),%eax
 804909c:	50                   	push   %eax
 804909d:	8d 83 30 d2 ff ff    	lea    -0x2dd0(%ebx),%eax
 80490a3:	50                   	push   %eax
 80490a4:	51                   	push   %ecx
 80490a5:	56                   	push   %esi
 80490a6:	c7 c0 16 92 04 08    	mov    $0x8049216,%eax
 80490ac:	50                   	push   %eax
 80490ad:	e8 8e ff ff ff       	call   8049040 <__libc_start_main@plt>
 80490b2:	f4                   	hlt    
 80490b3:	8b 1c 24             	mov    (%esp),%ebx
 80490b6:	c3                   	ret    
 80490b7:	66 90                	xchg   %ax,%ax
 80490b9:	66 90                	xchg   %ax,%ax
 80490bb:	66 90                	xchg   %ax,%ax
 80490bd:	66 90                	xchg   %ax,%ax
 80490bf:	90                   	nop

080490c0 <_dl_relocate_static_pie>:
 80490c0:	f3 c3                	repz ret 
 80490c2:	66 90                	xchg   %ax,%ax
 80490c4:	66 90                	xchg   %ax,%ax
 80490c6:	66 90                	xchg   %ax,%ax
 80490c8:	66 90                	xchg   %ax,%ax
 80490ca:	66 90                	xchg   %ax,%ax
 80490cc:	66 90                	xchg   %ax,%ax
 80490ce:	66 90                	xchg   %ax,%ax

080490d0 <__x86.get_pc_thunk.bx>:
 80490d0:	8b 1c 24             	mov    (%esp),%ebx
 80490d3:	c3                   	ret    
 80490d4:	66 90                	xchg   %ax,%ax
 80490d6:	66 90                	xchg   %ax,%ax
 80490d8:	66 90                	xchg   %ax,%ax
 80490da:	66 90                	xchg   %ax,%ax
 80490dc:	66 90                	xchg   %ax,%ax
 80490de:	66 90                	xchg   %ax,%ax

080490e0 <deregister_tm_clones>:
 80490e0:	b8 20 c0 04 08       	mov    $0x804c020,%eax
 80490e5:	3d 20 c0 04 08       	cmp    $0x804c020,%eax
 80490ea:	74 24                	je     8049110 <deregister_tm_clones+0x30>
 80490ec:	b8 00 00 00 00       	mov    $0x0,%eax
 80490f1:	85 c0                	test   %eax,%eax
 80490f3:	74 1b                	je     8049110 <deregister_tm_clones+0x30>
 80490f5:	55                   	push   %ebp
 80490f6:	89 e5                	mov    %esp,%ebp
 80490f8:	83 ec 14             	sub    $0x14,%esp
 80490fb:	68 20 c0 04 08       	push   $0x804c020
 8049100:	ff d0                	call   *%eax
 8049102:	83 c4 10             	add    $0x10,%esp
 8049105:	c9                   	leave  
 8049106:	c3                   	ret    
 8049107:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 804910e:	66 90                	xchg   %ax,%ax
 8049110:	c3                   	ret    
 8049111:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 8049118:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 804911f:	90                   	nop

08049120 <register_tm_clones>:
 8049120:	b8 20 c0 04 08       	mov    $0x804c020,%eax
 8049125:	2d 20 c0 04 08       	sub    $0x804c020,%eax
 804912a:	89 c2                	mov    %eax,%edx
 804912c:	c1 e8 1f             	shr    $0x1f,%eax
 804912f:	c1 fa 02             	sar    $0x2,%edx
 8049132:	01 d0                	add    %edx,%eax
 8049134:	d1 f8                	sar    %eax
 8049136:	74 20                	je     8049158 <register_tm_clones+0x38>
 8049138:	ba 00 00 00 00       	mov    $0x0,%edx
 804913d:	85 d2                	test   %edx,%edx
 804913f:	74 17                	je     8049158 <register_tm_clones+0x38>
 8049141:	55                   	push   %ebp
 8049142:	89 e5                	mov    %esp,%ebp
 8049144:	83 ec 10             	sub    $0x10,%esp
 8049147:	50                   	push   %eax
 8049148:	68 20 c0 04 08       	push   $0x804c020
 804914d:	ff d2                	call   *%edx
 804914f:	83 c4 10             	add    $0x10,%esp
 8049152:	c9                   	leave  
 8049153:	c3                   	ret    
 8049154:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 8049158:	c3                   	ret    
 8049159:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi

08049160 <__do_global_dtors_aux>:
 8049160:	f3 0f 1e fb          	endbr32 
 8049164:	80 3d 20 c0 04 08 00 	cmpb   $0x0,0x804c020
 804916b:	75 1b                	jne    8049188 <__do_global_dtors_aux+0x28>
 804916d:	55                   	push   %ebp
 804916e:	89 e5                	mov    %esp,%ebp
 8049170:	83 ec 08             	sub    $0x8,%esp
 8049173:	e8 68 ff ff ff       	call   80490e0 <deregister_tm_clones>
 8049178:	c6 05 20 c0 04 08 01 	movb   $0x1,0x804c020
 804917f:	c9                   	leave  
 8049180:	c3                   	ret    
 8049181:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 8049188:	c3                   	ret    
 8049189:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi

08049190 <frame_dummy>:
 8049190:	f3 0f 1e fb          	endbr32 
 8049194:	eb 8a                	jmp    8049120 <register_tm_clones>

08049196 <search>:
 8049196:	55                   	push   %ebp
 8049197:	89 e5                	mov    %esp,%ebp
 8049199:	83 ec 18             	sub    $0x18,%esp
 804919c:	c7 45 f4 00 00 00 60 	movl   $0x60000000,-0xc(%ebp)
 80491a3:	eb 66                	jmp    804920b <search+0x75>
 80491a5:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
 80491ac:	eb 4a                	jmp    80491f8 <search+0x62>
 80491ae:	8b 55 f4             	mov    -0xc(%ebp),%edx
 80491b1:	8b 45 f0             	mov    -0x10(%ebp),%eax
 80491b4:	01 d0                	add    %edx,%eax
 80491b6:	83 ec 08             	sub    $0x8,%esp
 80491b9:	6a 00                	push   $0x0
 80491bb:	50                   	push   %eax
 80491bc:	e8 9f fe ff ff       	call   8049060 <access@plt>
 80491c1:	83 c4 10             	add    $0x10,%esp
 80491c4:	83 f8 f2             	cmp    $0xfffffff2,%eax
 80491c7:	74 3a                	je     8049203 <search+0x6d>
 80491c9:	8b 55 f4             	mov    -0xc(%ebp),%edx
 80491cc:	8b 45 f0             	mov    -0x10(%ebp),%eax
 80491cf:	01 d0                	add    %edx,%eax
 80491d1:	8b 00                	mov    (%eax),%eax
 80491d3:	3d 48 54 42 7b       	cmp    $0x7b425448,%eax
 80491d8:	75 1a                	jne    80491f4 <search+0x5e>
 80491da:	8b 55 f4             	mov    -0xc(%ebp),%edx
 80491dd:	8b 45 f0             	mov    -0x10(%ebp),%eax
 80491e0:	01 d0                	add    %edx,%eax
 80491e2:	83 ec 04             	sub    $0x4,%esp
 80491e5:	6a 24                	push   $0x24
 80491e7:	50                   	push   %eax
 80491e8:	6a 01                	push   $0x1
 80491ea:	e8 61 fe ff ff       	call   8049050 <write@plt>
 80491ef:	83 c4 10             	add    $0x10,%esp
 80491f2:	eb 20                	jmp    8049214 <search+0x7e>
 80491f4:	83 45 f0 04          	addl   $0x4,-0x10(%ebp)
 80491f8:	81 7d f0 ff 0f 00 00 	cmpl   $0xfff,-0x10(%ebp)
 80491ff:	76 ad                	jbe    80491ae <search+0x18>
 8049201:	eb 01                	jmp    8049204 <search+0x6e>
 8049203:	90                   	nop
 8049204:	81 45 f4 00 10 00 00 	addl   $0x1000,-0xc(%ebp)
 804920b:	81 7d f4 00 00 00 f7 	cmpl   $0xf7000000,-0xc(%ebp)
 8049212:	76 91                	jbe    80491a5 <search+0xf>
 8049214:	c9                   	leave  
 8049215:	c3                   	ret    

08049216 <main>:
 8049216:	55                   	push   %ebp
 8049217:	89 e5                	mov    %esp,%ebp
 8049219:	83 e4 f0             	and    $0xfffffff0,%esp
 804921c:	e8 75 ff ff ff       	call   8049196 <search>
 8049221:	b8 00 00 00 00       	mov    $0x0,%eax
 8049226:	c9                   	leave  
 8049227:	c3                   	ret    
 8049228:	66 90                	xchg   %ax,%ax
 804922a:	66 90                	xchg   %ax,%ax
 804922c:	66 90                	xchg   %ax,%ax
 804922e:	66 90                	xchg   %ax,%ax

08049230 <__libc_csu_init>:
 8049230:	55                   	push   %ebp
 8049231:	57                   	push   %edi
 8049232:	56                   	push   %esi
 8049233:	53                   	push   %ebx
 8049234:	e8 97 fe ff ff       	call   80490d0 <__x86.get_pc_thunk.bx>
 8049239:	81 c3 c7 2d 00 00    	add    $0x2dc7,%ebx
 804923f:	83 ec 0c             	sub    $0xc,%esp
 8049242:	8b 6c 24 28          	mov    0x28(%esp),%ebp
 8049246:	8d b3 08 ff ff ff    	lea    -0xf8(%ebx),%esi
 804924c:	e8 af fd ff ff       	call   8049000 <_init>
 8049251:	8d 83 04 ff ff ff    	lea    -0xfc(%ebx),%eax
 8049257:	29 c6                	sub    %eax,%esi
 8049259:	c1 fe 02             	sar    $0x2,%esi
 804925c:	85 f6                	test   %esi,%esi
 804925e:	74 25                	je     8049285 <__libc_csu_init+0x55>
 8049260:	31 ff                	xor    %edi,%edi
 8049262:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi
 8049268:	83 ec 04             	sub    $0x4,%esp
 804926b:	55                   	push   %ebp
 804926c:	ff 74 24 2c          	push   0x2c(%esp)
 8049270:	ff 74 24 2c          	push   0x2c(%esp)
 8049274:	ff 94 bb 04 ff ff ff 	call   *-0xfc(%ebx,%edi,4)
 804927b:	83 c7 01             	add    $0x1,%edi
 804927e:	83 c4 10             	add    $0x10,%esp
 8049281:	39 fe                	cmp    %edi,%esi
 8049283:	75 e3                	jne    8049268 <__libc_csu_init+0x38>
 8049285:	83 c4 0c             	add    $0xc,%esp
 8049288:	5b                   	pop    %ebx
 8049289:	5e                   	pop    %esi
 804928a:	5f                   	pop    %edi
 804928b:	5d                   	pop    %ebp
 804928c:	c3                   	ret    
 804928d:	8d 76 00             	lea    0x0(%esi),%esi

08049290 <__libc_csu_fini>:
 8049290:	f3 c3                	repz ret 

Disassembly of section .fini:

08049294 <_fini>:
 8049294:	53                   	push   %ebx
 8049295:	83 ec 08             	sub    $0x8,%esp
 8049298:	e8 33 fe ff ff       	call   80490d0 <__x86.get_pc_thunk.bx>
 804929d:	81 c3 63 2d 00 00    	add    $0x2d63,%ebx
 80492a3:	83 c4 08             	add    $0x8,%esp
 80492a6:	5b                   	pop    %ebx
 80492a7:	c3                   	ret    

Disassembly of section .rodata:

0804a000 <_fp_hw>:
 804a000:	03 00                	add    (%eax),%eax
	...

0804a004 <_IO_stdin_used>:
 804a004:	01 00                	add    %eax,(%eax)
 804a006:	02 00                	add    (%eax),%al

Disassembly of section .eh_frame_hdr:

0804a008 <__GNU_EH_FRAME_HDR>:
 804a008:	01 1b                	add    %ebx,(%ebx)
 804a00a:	03 3b                	add    (%ebx),%edi
 804a00c:	40                   	inc    %eax
 804a00d:	00 00                	add    %al,(%eax)
 804a00f:	00 07                	add    %al,(%edi)
 804a011:	00 00                	add    %al,(%eax)
 804a013:	00 28                	add    %ch,(%eax)
 804a015:	f0 ff                	lock (bad) 
 804a017:	ff 70 00             	push   0x0(%eax)
 804a01a:	00 00                	add    %al,(%eax)
 804a01c:	68 f0 ff ff 94       	push   $0x94fffff0
 804a021:	00 00                	add    %al,(%eax)
 804a023:	00 b8 f0 ff ff 5c    	add    %bh,0x5cfffff0(%eax)
 804a029:	00 00                	add    %al,(%eax)
 804a02b:	00 8e f1 ff ff a8    	add    %cl,-0x5700000f(%esi)
 804a031:	00 00                	add    %al,(%eax)
 804a033:	00 0e                	add    %cl,(%esi)
 804a035:	f2 ff                	repnz (bad) 
 804a037:	ff c8                	dec    %eax
 804a039:	00 00                	add    %al,(%eax)
 804a03b:	00 28                	add    %ch,(%eax)
 804a03d:	f2 ff                	repnz (bad) 
 804a03f:	ff                   	(bad)  
 804a040:	e8 00 00 00 88       	call   9004a045 <_end+0x87ffe021>
 804a045:	f2 ff                	repnz (bad) 
 804a047:	ff 34 01             	push   (%ecx,%eax,1)
	...

Disassembly of section .eh_frame:

0804a04c <__FRAME_END__-0x104>:
 804a04c:	14 00                	adc    $0x0,%al
 804a04e:	00 00                	add    %al,(%eax)
 804a050:	00 00                	add    %al,(%eax)
 804a052:	00 00                	add    %al,(%eax)
 804a054:	01 7a 52             	add    %edi,0x52(%edx)
 804a057:	00 01                	add    %al,(%ecx)
 804a059:	7c 08                	jl     804a063 <__GNU_EH_FRAME_HDR+0x5b>
 804a05b:	01 1b                	add    %ebx,(%ebx)
 804a05d:	0c 04                	or     $0x4,%al
 804a05f:	04 88                	add    $0x88,%al
 804a061:	01 00                	add    %eax,(%eax)
 804a063:	00 10                	add    %dl,(%eax)
 804a065:	00 00                	add    %al,(%eax)
 804a067:	00 1c 00             	add    %bl,(%eax,%eax,1)
 804a06a:	00 00                	add    %al,(%eax)
 804a06c:	54                   	push   %esp
 804a06d:	f0 ff                	lock (bad) 
 804a06f:	ff 02                	incl   (%edx)
 804a071:	00 00                	add    %al,(%eax)
 804a073:	00 00                	add    %al,(%eax)
 804a075:	00 00                	add    %al,(%eax)
 804a077:	00 20                	add    %ah,(%eax)
 804a079:	00 00                	add    %al,(%eax)
 804a07b:	00 30                	add    %dh,(%eax)
 804a07d:	00 00                	add    %al,(%eax)
 804a07f:	00 b0 ef ff ff 40    	add    %dh,0x40ffffef(%eax)
 804a085:	00 00                	add    %al,(%eax)
 804a087:	00 00                	add    %al,(%eax)
 804a089:	0e                   	push   %cs
 804a08a:	08 46 0e             	or     %al,0xe(%esi)
 804a08d:	0c 4a                	or     $0x4a,%al
 804a08f:	0f 0b                	ud2    
 804a091:	74 04                	je     804a097 <__GNU_EH_FRAME_HDR+0x8f>
 804a093:	78 00                	js     804a095 <__GNU_EH_FRAME_HDR+0x8d>
 804a095:	3f                   	aas    
 804a096:	1a 3b                	sbb    (%ebx),%bh
 804a098:	2a 32                	sub    (%edx),%dh
 804a09a:	24 22                	and    $0x22,%al
 804a09c:	10 00                	adc    %al,(%eax)
 804a09e:	00 00                	add    %al,(%eax)
 804a0a0:	54                   	push   %esp
 804a0a1:	00 00                	add    %al,(%eax)
 804a0a3:	00 cc                	add    %cl,%ah
 804a0a5:	ef                   	out    %eax,(%dx)
 804a0a6:	ff                   	(bad)  
 804a0a7:	ff 08                	decl   (%eax)
 804a0a9:	00 00                	add    %al,(%eax)
 804a0ab:	00 00                	add    %al,(%eax)
 804a0ad:	00 00                	add    %al,(%eax)
 804a0af:	00 1c 00             	add    %bl,(%eax,%eax,1)
 804a0b2:	00 00                	add    %al,(%eax)
 804a0b4:	68 00 00 00 de       	push   $0xde000000
 804a0b9:	f0 ff                	lock (bad) 
 804a0bb:	ff 80 00 00 00 00    	incl   0x0(%eax)
 804a0c1:	41                   	inc    %ecx
 804a0c2:	0e                   	push   %cs
 804a0c3:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
 804a0c9:	02 7c c5 0c          	add    0xc(%ebp,%eax,8),%bh
 804a0cd:	04 04                	add    $0x4,%al
 804a0cf:	00 1c 00             	add    %bl,(%eax,%eax,1)
 804a0d2:	00 00                	add    %al,(%eax)
 804a0d4:	88 00                	mov    %al,(%eax)
 804a0d6:	00 00                	add    %al,(%eax)
 804a0d8:	3e f1                	ds icebp 
 804a0da:	ff                   	(bad)  
 804a0db:	ff 12                	call   *(%edx)
 804a0dd:	00 00                	add    %al,(%eax)
 804a0df:	00 00                	add    %al,(%eax)
 804a0e1:	41                   	inc    %ecx
 804a0e2:	0e                   	push   %cs
 804a0e3:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
 804a0e9:	4e                   	dec    %esi
 804a0ea:	c5 0c 04             	lds    (%esp,%eax,1),%ecx
 804a0ed:	04 00                	add    $0x0,%al
 804a0ef:	00 48 00             	add    %cl,0x0(%eax)
 804a0f2:	00 00                	add    %al,(%eax)
 804a0f4:	a8 00                	test   $0x0,%al
 804a0f6:	00 00                	add    %al,(%eax)
 804a0f8:	38 f1                	cmp    %dh,%cl
 804a0fa:	ff                   	(bad)  
 804a0fb:	ff 5d 00             	lcall  *0x0(%ebp)
 804a0fe:	00 00                	add    %al,(%eax)
 804a100:	00 41 0e             	add    %al,0xe(%ecx)
 804a103:	08 85 02 41 0e 0c    	or     %al,0xc0e4102(%ebp)
 804a109:	87 03                	xchg   %eax,(%ebx)
 804a10b:	41                   	inc    %ecx
 804a10c:	0e                   	push   %cs
 804a10d:	10 86 04 41 0e 14    	adc    %al,0x140e4104(%esi)
 804a113:	83 05 4e 0e 20 69 0e 	addl   $0xe,0x69200e4e
 804a11a:	24 41                	and    $0x41,%al
 804a11c:	0e                   	push   %cs
 804a11d:	28 44 0e 2c          	sub    %al,0x2c(%esi,%ecx,1)
 804a121:	44                   	inc    %esp
 804a122:	0e                   	push   %cs
 804a123:	30 4d 0e             	xor    %cl,0xe(%ebp)
 804a126:	20 47 0e             	and    %al,0xe(%edi)
 804a129:	14 41                	adc    $0x41,%al
 804a12b:	c3                   	ret    
 804a12c:	0e                   	push   %cs
 804a12d:	10 41 c6             	adc    %al,-0x3a(%ecx)
 804a130:	0e                   	push   %cs
 804a131:	0c 41                	or     $0x41,%al
 804a133:	c7                   	(bad)  
 804a134:	0e                   	push   %cs
 804a135:	08 41 c5             	or     %al,-0x3b(%ecx)
 804a138:	0e                   	push   %cs
 804a139:	04 00                	add    $0x0,%al
 804a13b:	00 10                	add    %dl,(%eax)
 804a13d:	00 00                	add    %al,(%eax)
 804a13f:	00 f4                	add    %dh,%ah
 804a141:	00 00                	add    %al,(%eax)
 804a143:	00 4c f1 ff          	add    %cl,-0x1(%ecx,%esi,8)
 804a147:	ff 02                	incl   (%edx)
 804a149:	00 00                	add    %al,(%eax)
 804a14b:	00 00                	add    %al,(%eax)
 804a14d:	00 00                	add    %al,(%eax)
	...

0804a150 <__FRAME_END__>:
 804a150:	00 00                	add    %al,(%eax)
	...

Disassembly of section .init_array:

0804bf04 <__frame_dummy_init_array_entry>:
 804bf04:	90                   	nop
 804bf05:	91                   	xchg   %eax,%ecx
 804bf06:	04 08                	add    $0x8,%al

Disassembly of section .fini_array:

0804bf08 <__do_global_dtors_aux_fini_array_entry>:
 804bf08:	60                   	pusha  
 804bf09:	91                   	xchg   %eax,%ecx
 804bf0a:	04 08                	add    $0x8,%al

Disassembly of section .dynamic:

0804bf0c <_DYNAMIC>:
 804bf0c:	01 00                	add    %eax,(%eax)
 804bf0e:	00 00                	add    %al,(%eax)
 804bf10:	2f                   	das    
 804bf11:	00 00                	add    %al,(%eax)
 804bf13:	00 0c 00             	add    %cl,(%eax,%eax,1)
 804bf16:	00 00                	add    %al,(%eax)
 804bf18:	00 90 04 08 0d 00    	add    %dl,0xd0804(%eax)
 804bf1e:	00 00                	add    %al,(%eax)
 804bf20:	94                   	xchg   %eax,%esp
 804bf21:	92                   	xchg   %eax,%edx
 804bf22:	04 08                	add    $0x8,%al
 804bf24:	19 00                	sbb    %eax,(%eax)
 804bf26:	00 00                	add    %al,(%eax)
 804bf28:	04 bf                	add    $0xbf,%al
 804bf2a:	04 08                	add    $0x8,%al
 804bf2c:	1b 00                	sbb    (%eax),%eax
 804bf2e:	00 00                	add    %al,(%eax)
 804bf30:	04 00                	add    $0x0,%al
 804bf32:	00 00                	add    %al,(%eax)
 804bf34:	1a 00                	sbb    (%eax),%al
 804bf36:	00 00                	add    %al,(%eax)
 804bf38:	08 bf 04 08 1c 00    	or     %bh,0x1c0804(%edi)
 804bf3e:	00 00                	add    %al,(%eax)
 804bf40:	04 00                	add    $0x0,%al
 804bf42:	00 00                	add    %al,(%eax)
 804bf44:	04 00                	add    $0x0,%al
 804bf46:	00 00                	add    %al,(%eax)
 804bf48:	c8 81 04 08          	enter  $0x481,$0x8
 804bf4c:	f5                   	cmc    
 804bf4d:	fe                   	(bad)  
 804bf4e:	ff 6f f4             	ljmp   *-0xc(%edi)
 804bf51:	81 04 08 05 00 00 00 	addl   $0x5,(%eax,%ecx,1)
 804bf58:	74 82                	je     804bedc <__FRAME_END__+0x1d8c>
 804bf5a:	04 08                	add    $0x8,%al
 804bf5c:	06                   	push   %es
 804bf5d:	00 00                	add    %al,(%eax)
 804bf5f:	00 14 82             	add    %dl,(%edx,%eax,4)
 804bf62:	04 08                	add    $0x8,%al
 804bf64:	0a 00                	or     (%eax),%al
 804bf66:	00 00                	add    %al,(%eax)
 804bf68:	52                   	push   %edx
 804bf69:	00 00                	add    %al,(%eax)
 804bf6b:	00 0b                	add    %cl,(%ebx)
 804bf6d:	00 00                	add    %al,(%eax)
 804bf6f:	00 10                	add    %dl,(%eax)
 804bf71:	00 00                	add    %al,(%eax)
 804bf73:	00 15 00 00 00 00    	add    %dl,0x0
 804bf79:	00 00                	add    %al,(%eax)
 804bf7b:	00 03                	add    %al,(%ebx)
 804bf7d:	00 00                	add    %al,(%eax)
 804bf7f:	00 00                	add    %al,(%eax)
 804bf81:	c0 04 08 02          	rolb   $0x2,(%eax,%ecx,1)
 804bf85:	00 00                	add    %al,(%eax)
 804bf87:	00 18                	add    %bl,(%eax)
 804bf89:	00 00                	add    %al,(%eax)
 804bf8b:	00 14 00             	add    %dl,(%eax,%eax,1)
 804bf8e:	00 00                	add    %al,(%eax)
 804bf90:	11 00                	adc    %eax,(%eax)
 804bf92:	00 00                	add    %al,(%eax)
 804bf94:	17                   	pop    %ss
 804bf95:	00 00                	add    %al,(%eax)
 804bf97:	00 fc                	add    %bh,%ah
 804bf99:	82 04 08 11          	addb   $0x11,(%eax,%ecx,1)
 804bf9d:	00 00                	add    %al,(%eax)
 804bf9f:	00 f4                	add    %dh,%ah
 804bfa1:	82 04 08 12          	addb   $0x12,(%eax,%ecx,1)
 804bfa5:	00 00                	add    %al,(%eax)
 804bfa7:	00 08                	add    %cl,(%eax)
 804bfa9:	00 00                	add    %al,(%eax)
 804bfab:	00 13                	add    %dl,(%ebx)
 804bfad:	00 00                	add    %al,(%eax)
 804bfaf:	00 08                	add    %cl,(%eax)
 804bfb1:	00 00                	add    %al,(%eax)
 804bfb3:	00 fe                	add    %bh,%dh
 804bfb5:	ff                   	(bad)  
 804bfb6:	ff 6f d4             	ljmp   *-0x2c(%edi)
 804bfb9:	82 04 08 ff          	addb   $0xff,(%eax,%ecx,1)
 804bfbd:	ff                   	(bad)  
 804bfbe:	ff 6f 01             	ljmp   *0x1(%edi)
 804bfc1:	00 00                	add    %al,(%eax)
 804bfc3:	00 f0                	add    %dh,%al
 804bfc5:	ff                   	(bad)  
 804bfc6:	ff 6f c6             	ljmp   *-0x3a(%edi)
 804bfc9:	82 04 08 00          	addb   $0x0,(%eax,%ecx,1)
	...

Disassembly of section .got:

0804bffc <.got>:
 804bffc:	00 00                	add    %al,(%eax)
	...

Disassembly of section .got.plt:

0804c000 <_GLOBAL_OFFSET_TABLE_>:
 804c000:	0c bf                	or     $0xbf,%al
 804c002:	04 08                	add    $0x8,%al
	...
 804c00c:	46                   	inc    %esi
 804c00d:	90                   	nop
 804c00e:	04 08                	add    $0x8,%al
 804c010:	56                   	push   %esi
 804c011:	90                   	nop
 804c012:	04 08                	add    $0x8,%al
 804c014:	66 90                	xchg   %ax,%ax
 804c016:	04 08                	add    $0x8,%al

Disassembly of section .data:

0804c018 <__data_start>:
 804c018:	00 00                	add    %al,(%eax)
	...

0804c01c <__dso_handle>:
 804c01c:	00 00                	add    %al,(%eax)
	...

Disassembly of section .bss:

0804c020 <completed.0>:
 804c020:	00 00                	add    %al,(%eax)
	...

Disassembly of section .comment:

00000000 <.comment>:
   0:	47                   	inc    %edi
   1:	43                   	inc    %ebx
   2:	43                   	inc    %ebx
   3:	3a 20                	cmp    (%eax),%ah
   5:	28 47 4e             	sub    %al,0x4e(%edi)
   8:	55                   	push   %ebp
   9:	29 20                	sub    %esp,(%eax)
   b:	31 32                	xor    %esi,(%edx)
   d:	2e 32 2e             	xor    %cs:(%esi),%ch
  10:	30 00                	xor    %al,(%eax)
