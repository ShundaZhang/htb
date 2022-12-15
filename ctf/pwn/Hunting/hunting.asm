
hunting:     file format elf32-i386


Disassembly of section .interp:

000001b4 <.interp>:
 1b4:	2f                   	das    
 1b5:	6c                   	insb   (%dx),%es:(%edi)
 1b6:	69 62 2f 6c 64 2d 6c 	imul   $0x6c2d646c,0x2f(%edx),%esp
 1bd:	69 6e 75 78 2e 73 6f 	imul   $0x6f732e78,0x75(%esi),%ebp
 1c4:	2e 32 00             	xor    %cs:(%eax),%al

Disassembly of section .note.gnu.build-id:

000001c8 <.note.gnu.build-id>:
 1c8:	04 00                	add    $0x0,%al
 1ca:	00 00                	add    %al,(%eax)
 1cc:	14 00                	adc    $0x0,%al
 1ce:	00 00                	add    %al,(%eax)
 1d0:	03 00                	add    (%eax),%eax
 1d2:	00 00                	add    %al,(%eax)
 1d4:	47                   	inc    %edi
 1d5:	4e                   	dec    %esi
 1d6:	55                   	push   %ebp
 1d7:	00 80 1f 10 40 74    	add    %al,0x7440101f(%eax)
 1dd:	44                   	inc    %esp
 1de:	c1 39 0c             	sarl   $0xc,(%ecx)
 1e1:	ae                   	scas   %es:(%edi),%al
 1e2:	57                   	push   %edi
 1e3:	55                   	push   %ebp
 1e4:	d9 e9                	fldl2t 
 1e6:	52                   	push   %edx
 1e7:	f3 fe                	repz (bad) 
 1e9:	ad                   	lods   %ds:(%esi),%eax
 1ea:	f3                   	repz
 1eb:	eb                   	.byte 0xeb

Disassembly of section .note.gnu.property:

000001ec <.note.gnu.property>:
 1ec:	04 00                	add    $0x0,%al
 1ee:	00 00                	add    %al,(%eax)
 1f0:	0c 00                	or     $0x0,%al
 1f2:	00 00                	add    %al,(%eax)
 1f4:	05 00 00 00 47       	add    $0x47000000,%eax
 1f9:	4e                   	dec    %esi
 1fa:	55                   	push   %ebp
 1fb:	00 02                	add    %al,(%edx)
 1fd:	00 00                	add    %al,(%eax)
 1ff:	c0 04 00 00          	rolb   $0x0,(%eax,%eax,1)
 203:	00 03                	add    %al,(%ebx)
 205:	00 00                	add    %al,(%eax)
	...

Disassembly of section .note.ABI-tag:

00000208 <.note.ABI-tag>:
 208:	04 00                	add    $0x0,%al
 20a:	00 00                	add    %al,(%eax)
 20c:	10 00                	adc    %al,(%eax)
 20e:	00 00                	add    %al,(%eax)
 210:	01 00                	add    %eax,(%eax)
 212:	00 00                	add    %al,(%eax)
 214:	47                   	inc    %edi
 215:	4e                   	dec    %esi
 216:	55                   	push   %ebp
 217:	00 00                	add    %al,(%eax)
 219:	00 00                	add    %al,(%eax)
 21b:	00 03                	add    %al,(%ebx)
 21d:	00 00                	add    %al,(%eax)
 21f:	00 02                	add    %al,(%edx)
 221:	00 00                	add    %al,(%eax)
 223:	00 00                	add    %al,(%eax)
 225:	00 00                	add    %al,(%eax)
	...

Disassembly of section .gnu.hash:

00000228 <.gnu.hash>:
 228:	02 00                	add    (%eax),%al
 22a:	00 00                	add    %al,(%eax)
 22c:	13 00                	adc    (%eax),%eax
 22e:	00 00                	add    %al,(%eax)
 230:	01 00                	add    %eax,(%eax)
 232:	00 00                	add    %al,(%eax)
 234:	05 00 00 00 00       	add    $0x0,%eax
 239:	20 00                	and    %al,(%eax)
 23b:	20 00                	and    %al,(%eax)
 23d:	00 00                	add    %al,(%eax)
 23f:	00 13                	add    %dl,(%ebx)
 241:	00 00                	add    %al,(%eax)
 243:	00                   	.byte 0x0
 244:	ad                   	lods   %ds:(%esi),%eax
 245:	4b                   	dec    %ebx
 246:	e3 c0                	jecxz  208 <__cxa_finalize@plt-0xf08>

Disassembly of section .dynsym:

00000248 <.dynsym>:
	...
 258:	4c                   	dec    %esp
	...
 261:	00 00                	add    %al,(%eax)
 263:	00 12                	add    %dl,(%edx)
 265:	00 00                	add    %al,(%eax)
 267:	00 99 00 00 00 00    	add    %bl,0x0(%ecx)
 26d:	00 00                	add    %al,(%eax)
 26f:	00 00                	add    %al,(%eax)
 271:	00 00                	add    %al,(%eax)
 273:	00 20                	add    %ah,(%eax)
 275:	00 00                	add    %al,(%eax)
 277:	00 33                	add    %dh,(%ebx)
	...
 281:	00 00                	add    %al,(%eax)
 283:	00 12                	add    %dl,(%edx)
 285:	00 00                	add    %al,(%eax)
 287:	00 51 00             	add    %dl,0x0(%ecx)
	...
 292:	00 00                	add    %al,(%eax)
 294:	12 00                	adc    (%eax),%al
 296:	00 00                	add    %al,(%eax)
 298:	62 00                	bound  %eax,(%eax)
	...
 2a2:	00 00                	add    %al,(%eax)
 2a4:	22 00                	and    (%eax),%al
 2a6:	00 00                	add    %al,(%eax)
 2a8:	2c 00                	sub    $0x0,%al
	...
 2b2:	00 00                	add    %al,(%eax)
 2b4:	12 00                	adc    (%eax),%al
 2b6:	00 00                	add    %al,(%eax)
 2b8:	1a 00                	sbb    (%eax),%al
	...
 2c2:	00 00                	add    %al,(%eax)
 2c4:	12 00                	adc    (%eax),%al
 2c6:	00 00                	add    %al,(%eax)
 2c8:	b5 00                	mov    $0x0,%ch
	...
 2d2:	00 00                	add    %al,(%eax)
 2d4:	20 00                	and    %al,(%eax)
 2d6:	00 00                	add    %al,(%eax)
 2d8:	21 00                	and    %eax,(%eax)
	...
 2e2:	00 00                	add    %al,(%eax)
 2e4:	12 00                	adc    (%eax),%al
 2e6:	00 00                	add    %al,(%eax)
 2e8:	5d                   	pop    %ebp
	...
 2f1:	00 00                	add    %al,(%eax)
 2f3:	00 12                	add    %dl,(%edx)
 2f5:	00 00                	add    %al,(%eax)
 2f7:	00 26                	add    %ah,(%esi)
	...
 301:	00 00                	add    %al,(%eax)
 303:	00 12                	add    %dl,(%edx)
 305:	00 00                	add    %al,(%eax)
 307:	00 3a                	add    %bh,(%edx)
	...
 311:	00 00                	add    %al,(%eax)
 313:	00 12                	add    %dl,(%edx)
 315:	00 00                	add    %al,(%eax)
 317:	00 71 00             	add    %dh,0x0(%ecx)
	...
 322:	00 00                	add    %al,(%eax)
 324:	12 00                	adc    (%eax),%al
 326:	00 00                	add    %al,(%eax)
 328:	45                   	inc    %ebp
	...
 331:	00 00                	add    %al,(%eax)
 333:	00 12                	add    %dl,(%edx)
 335:	00 00                	add    %al,(%eax)
 337:	00 3f                	add    %bh,(%edi)
	...
 341:	00 00                	add    %al,(%eax)
 343:	00 12                	add    %dl,(%edx)
 345:	00 00                	add    %al,(%eax)
 347:	00 27                	add    %ah,(%edi)
	...
 351:	00 00                	add    %al,(%eax)
 353:	00 12                	add    %dl,(%edx)
 355:	00 00                	add    %al,(%eax)
 357:	00 c4                	add    %al,%ah
	...
 361:	00 00                	add    %al,(%eax)
 363:	00 20                	add    %ah,(%eax)
 365:	00 00                	add    %al,(%eax)
 367:	00 57 00             	add    %dl,0x0(%edi)
	...
 372:	00 00                	add    %al,(%eax)
 374:	12 00                	adc    (%eax),%al
 376:	00 00                	add    %al,(%eax)
 378:	0b 00                	or     (%eax),%eax
 37a:	00 00                	add    %al,(%eax)
 37c:	04 20                	add    $0x20,%al
 37e:	00 00                	add    %al,(%eax)
 380:	04 00                	add    $0x0,%al
 382:	00 00                	add    %al,(%eax)
 384:	11 00                	adc    %eax,(%eax)
 386:	12 00                	adc    (%eax),%al

Disassembly of section .dynstr:

00000388 <.dynstr>:
 388:	00 6c 69 62          	add    %ch,0x62(%ecx,%ebp,2)
 38c:	63 2e                	arpl   %bp,(%esi)
 38e:	73 6f                	jae    3ff <__cxa_finalize@plt-0xd11>
 390:	2e 36 00 5f 49       	cs add %bl,%ss:0x49(%edi)
 395:	4f                   	dec    %edi
 396:	5f                   	pop    %edi
 397:	73 74                	jae    40d <__cxa_finalize@plt-0xd03>
 399:	64 69 6e 5f 75 73 65 	imul   $0x64657375,%fs:0x5f(%esi),%ebp
 3a0:	64 
 3a1:	00 73 74             	add    %dh,0x74(%ebx)
 3a4:	72 63                	jb     409 <__cxa_finalize@plt-0xd07>
 3a6:	70 79                	jo     421 <__cxa_finalize@plt-0xcef>
 3a8:	00 65 78             	add    %ah,0x78(%ebp)
 3ab:	69 74 00 73 72 61 6e 	imul   $0x646e6172,0x73(%eax,%eax,1),%esi
 3b2:	64 
 3b3:	00 70 65             	add    %dh,0x65(%eax)
 3b6:	72 72                	jb     42a <__cxa_finalize@plt-0xce6>
 3b8:	6f                   	outsl  %ds:(%esi),(%dx)
 3b9:	72 00                	jb     3bb <__cxa_finalize@plt-0xd55>
 3bb:	73 69                	jae    426 <__cxa_finalize@plt-0xcea>
 3bd:	67 6e                	outsb  %ds:(%si),(%dx)
 3bf:	61                   	popa   
 3c0:	6c                   	insb   (%dx),%es:(%edi)
 3c1:	00 6d 6d             	add    %ch,0x6d(%ebp)
 3c4:	61                   	popa   
 3c5:	70 00                	jo     3c7 <__cxa_finalize@plt-0xd49>
 3c7:	70 72                	jo     43b <__cxa_finalize@plt-0xcd5>
 3c9:	63 74 6c 00          	arpl   %si,0x0(%esp,%ebp,2)
 3cd:	6d                   	insl   (%dx),%es:(%edi)
 3ce:	65 6d                	gs insl (%dx),%es:(%edi)
 3d0:	73 65                	jae    437 <__cxa_finalize@plt-0xcd9>
 3d2:	74 00                	je     3d4 <__cxa_finalize@plt-0xd3c>
 3d4:	72 65                	jb     43b <__cxa_finalize@plt-0xcd5>
 3d6:	61                   	popa   
 3d7:	64 00 61 6c          	add    %ah,%fs:0x6c(%ecx)
 3db:	61                   	popa   
 3dc:	72 6d                	jb     44b <__cxa_finalize@plt-0xcc5>
 3de:	00 63 6c             	add    %ah,0x6c(%ebx)
 3e1:	6f                   	outsl  %ds:(%esi),(%dx)
 3e2:	73 65                	jae    449 <__cxa_finalize@plt-0xcc7>
 3e4:	00 6f 70             	add    %ch,0x70(%edi)
 3e7:	65 6e                	outsb  %gs:(%esi),(%dx)
 3e9:	00 5f 5f             	add    %bl,0x5f(%edi)
 3ec:	63 78 61             	arpl   %di,0x61(%eax)
 3ef:	5f                   	pop    %edi
 3f0:	66 69 6e 61 6c 69    	imul   $0x696c,0x61(%esi),%bp
 3f6:	7a 65                	jp     45d <__cxa_finalize@plt-0xcb3>
 3f8:	00 5f 5f             	add    %bl,0x5f(%edi)
 3fb:	6c                   	insb   (%dx),%es:(%edi)
 3fc:	69 62 63 5f 73 74 61 	imul   $0x6174735f,0x63(%edx),%esp
 403:	72 74                	jb     479 <__cxa_finalize@plt-0xc97>
 405:	5f                   	pop    %edi
 406:	6d                   	insl   (%dx),%es:(%edi)
 407:	61                   	popa   
 408:	69 6e 00 47 4c 49 42 	imul   $0x42494c47,0x0(%esi),%ebp
 40f:	43                   	inc    %ebx
 410:	5f                   	pop    %edi
 411:	32 2e                	xor    (%esi),%ch
 413:	31 2e                	xor    %ebp,(%esi)
 415:	33 00                	xor    (%eax),%eax
 417:	47                   	inc    %edi
 418:	4c                   	dec    %esp
 419:	49                   	dec    %ecx
 41a:	42                   	inc    %edx
 41b:	43                   	inc    %ebx
 41c:	5f                   	pop    %edi
 41d:	32 2e                	xor    (%esi),%ch
 41f:	30 00                	xor    %al,(%eax)
 421:	5f                   	pop    %edi
 422:	49                   	dec    %ecx
 423:	54                   	push   %esp
 424:	4d                   	dec    %ebp
 425:	5f                   	pop    %edi
 426:	64 65 72 65          	fs gs jb 48f <__cxa_finalize@plt-0xc81>
 42a:	67 69 73 74 65 72 54 	imul   $0x4d547265,0x74(%bp,%di),%esi
 431:	4d 
 432:	43                   	inc    %ebx
 433:	6c                   	insb   (%dx),%es:(%edi)
 434:	6f                   	outsl  %ds:(%esi),(%dx)
 435:	6e                   	outsb  %ds:(%esi),(%dx)
 436:	65 54                	gs push %esp
 438:	61                   	popa   
 439:	62 6c 65 00          	bound  %ebp,0x0(%ebp,%eiz,2)
 43d:	5f                   	pop    %edi
 43e:	5f                   	pop    %edi
 43f:	67 6d                	insl   (%dx),%es:(%di)
 441:	6f                   	outsl  %ds:(%esi),(%dx)
 442:	6e                   	outsb  %ds:(%esi),(%dx)
 443:	5f                   	pop    %edi
 444:	73 74                	jae    4ba <__cxa_finalize@plt-0xc56>
 446:	61                   	popa   
 447:	72 74                	jb     4bd <__cxa_finalize@plt-0xc53>
 449:	5f                   	pop    %edi
 44a:	5f                   	pop    %edi
 44b:	00 5f 49             	add    %bl,0x49(%edi)
 44e:	54                   	push   %esp
 44f:	4d                   	dec    %ebp
 450:	5f                   	pop    %edi
 451:	72 65                	jb     4b8 <__cxa_finalize@plt-0xc58>
 453:	67 69 73 74 65 72 54 	imul   $0x4d547265,0x74(%bp,%di),%esi
 45a:	4d 
 45b:	43                   	inc    %ebx
 45c:	6c                   	insb   (%dx),%es:(%edi)
 45d:	6f                   	outsl  %ds:(%esi),(%dx)
 45e:	6e                   	outsb  %ds:(%esi),(%dx)
 45f:	65 54                	gs push %esp
 461:	61                   	popa   
 462:	62 6c 65 00          	bound  %ebp,0x0(%ebp,%eiz,2)

Disassembly of section .gnu.version:

00000466 <.gnu.version>:
 466:	00 00                	add    %al,(%eax)
 468:	02 00                	add    (%eax),%al
 46a:	00 00                	add    %al,(%eax)
 46c:	02 00                	add    (%eax),%al
 46e:	02 00                	add    (%eax),%al
 470:	03 00                	add    (%eax),%eax
 472:	02 00                	add    (%eax),%al
 474:	02 00                	add    (%eax),%al
 476:	00 00                	add    %al,(%eax)
 478:	02 00                	add    (%eax),%al
 47a:	02 00                	add    (%eax),%al
 47c:	02 00                	add    (%eax),%al
 47e:	02 00                	add    (%eax),%al
 480:	02 00                	add    (%eax),%al
 482:	02 00                	add    (%eax),%al
 484:	02 00                	add    (%eax),%al
 486:	02 00                	add    (%eax),%al
 488:	00 00                	add    %al,(%eax)
 48a:	02 00                	add    (%eax),%al
 48c:	01 00                	add    %eax,(%eax)

Disassembly of section .gnu.version_r:

00000490 <.gnu.version_r>:
 490:	01 00                	add    %eax,(%eax)
 492:	02 00                	add    (%eax),%al
 494:	01 00                	add    %eax,(%eax)
 496:	00 00                	add    %al,(%eax)
 498:	10 00                	adc    %al,(%eax)
 49a:	00 00                	add    %al,(%eax)
 49c:	00 00                	add    %al,(%eax)
 49e:	00 00                	add    %al,(%eax)
 4a0:	73 1f                	jae    4c1 <__cxa_finalize@plt-0xc4f>
 4a2:	69 09 00 00 03 00    	imul   $0x30000,(%ecx),%ecx
 4a8:	83 00 00             	addl   $0x0,(%eax)
 4ab:	00 10                	add    %dl,(%eax)
 4ad:	00 00                	add    %al,(%eax)
 4af:	00 10                	add    %dl,(%eax)
 4b1:	69 69 0d 00 00 02 00 	imul   $0x20000,0xd(%ecx),%ebp
 4b8:	8f 00                	pop    (%eax)
 4ba:	00 00                	add    %al,(%eax)
 4bc:	00 00                	add    %al,(%eax)
	...

Disassembly of section .rel.dyn:

000004c0 <.rel.dyn>:
 4c0:	a8 3e                	test   $0x3e,%al
 4c2:	00 00                	add    %al,(%eax)
 4c4:	08 00                	or     %al,(%eax)
 4c6:	00 00                	add    %al,(%eax)
 4c8:	ac                   	lods   %ds:(%esi),%al
 4c9:	3e 00 00             	add    %al,%ds:(%eax)
 4cc:	08 00                	or     %al,(%eax)
 4ce:	00 00                	add    %al,(%eax)
 4d0:	f8                   	clc    
 4d1:	3f                   	aas    
 4d2:	00 00                	add    %al,(%eax)
 4d4:	08 00                	or     %al,(%eax)
 4d6:	00 00                	add    %al,(%eax)
 4d8:	04 40                	add    $0x40,%al
 4da:	00 00                	add    %al,(%eax)
 4dc:	08 00                	or     %al,(%eax)
 4de:	00 00                	add    %al,(%eax)
 4e0:	e8 3f 00 00 06       	call   6000524 <_IO_stdin_used@@Base+0x5ffe520>
 4e5:	02 00                	add    (%eax),%al
 4e7:	00 ec                	add    %ch,%ah
 4e9:	3f                   	aas    
 4ea:	00 00                	add    %al,(%eax)
 4ec:	06                   	push   %es
 4ed:	05 00 00 f0 3f       	add    $0x3ff00000,%eax
 4f2:	00 00                	add    %al,(%eax)
 4f4:	06                   	push   %es
 4f5:	08 00                	or     %al,(%eax)
 4f7:	00 f4                	add    %dh,%ah
 4f9:	3f                   	aas    
 4fa:	00 00                	add    %al,(%eax)
 4fc:	06                   	push   %es
 4fd:	09 00                	or     %eax,(%eax)
 4ff:	00 fc                	add    %bh,%ah
 501:	3f                   	aas    
 502:	00 00                	add    %al,(%eax)
 504:	06                   	push   %es
 505:	11 00                	adc    %eax,(%eax)
	...

Disassembly of section .rel.plt:

00000508 <.rel.plt>:
 508:	b4 3f                	mov    $0x3f,%ah
 50a:	00 00                	add    %al,(%eax)
 50c:	07                   	pop    %es
 50d:	01 00                	add    %eax,(%eax)
 50f:	00 b8 3f 00 00 07    	add    %bh,0x700003f(%eax)
 515:	03 00                	add    (%eax),%eax
 517:	00 bc 3f 00 00 07 04 	add    %bh,0x4070000(%edi,%edi,1)
 51e:	00 00                	add    %al,(%eax)
 520:	c0 3f 00             	sarb   $0x0,(%edi)
 523:	00 07                	add    %al,(%edi)
 525:	06                   	push   %es
 526:	00 00                	add    %al,(%eax)
 528:	c4 3f                	les    (%edi),%edi
 52a:	00 00                	add    %al,(%eax)
 52c:	07                   	pop    %es
 52d:	07                   	pop    %es
 52e:	00 00                	add    %al,(%eax)
 530:	c8 3f 00 00          	enter  $0x3f,$0x0
 534:	07                   	pop    %es
 535:	0a 00                	or     (%eax),%al
 537:	00 cc                	add    %cl,%ah
 539:	3f                   	aas    
 53a:	00 00                	add    %al,(%eax)
 53c:	07                   	pop    %es
 53d:	0b 00                	or     (%eax),%eax
 53f:	00 d0                	add    %dl,%al
 541:	3f                   	aas    
 542:	00 00                	add    %al,(%eax)
 544:	07                   	pop    %es
 545:	0c 00                	or     $0x0,%al
 547:	00 d4                	add    %dl,%ah
 549:	3f                   	aas    
 54a:	00 00                	add    %al,(%eax)
 54c:	07                   	pop    %es
 54d:	0d 00 00 d8 3f       	or     $0x3fd80000,%eax
 552:	00 00                	add    %al,(%eax)
 554:	07                   	pop    %es
 555:	0e                   	push   %cs
 556:	00 00                	add    %al,(%eax)
 558:	dc 3f                	fdivrl (%edi)
 55a:	00 00                	add    %al,(%eax)
 55c:	07                   	pop    %es
 55d:	0f 00 00             	sldt   (%eax)
 560:	e0 3f                	loopne 5a1 <__cxa_finalize@plt-0xb6f>
 562:	00 00                	add    %al,(%eax)
 564:	07                   	pop    %es
 565:	10 00                	adc    %al,(%eax)
 567:	00 e4                	add    %ah,%ah
 569:	3f                   	aas    
 56a:	00 00                	add    %al,(%eax)
 56c:	07                   	pop    %es
 56d:	12 00                	adc    (%eax),%al
	...

Disassembly of section .init:

00001000 <.init>:
    1000:	f3 0f 1e fb          	endbr32 
    1004:	53                   	push   %ebx
    1005:	83 ec 08             	sub    $0x8,%esp
    1008:	e8 33 02 00 00       	call   1240 <close@plt+0x50>
    100d:	81 c3 9b 2f 00 00    	add    $0x2f9b,%ebx
    1013:	8b 83 48 00 00 00    	mov    0x48(%ebx),%eax
    1019:	85 c0                	test   %eax,%eax
    101b:	74 02                	je     101f <__cxa_finalize@plt-0xf1>
    101d:	ff d0                	call   *%eax
    101f:	83 c4 08             	add    $0x8,%esp
    1022:	5b                   	pop    %ebx
    1023:	c3                   	ret    

Disassembly of section .plt:

00001030 <.plt>:
    1030:	ff b3 04 00 00 00    	push   0x4(%ebx)
    1036:	ff a3 08 00 00 00    	jmp    *0x8(%ebx)
    103c:	0f 1f 40 00          	nopl   0x0(%eax)
    1040:	f3 0f 1e fb          	endbr32 
    1044:	68 00 00 00 00       	push   $0x0
    1049:	e9 e2 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    104e:	66 90                	xchg   %ax,%ax
    1050:	f3 0f 1e fb          	endbr32 
    1054:	68 08 00 00 00       	push   $0x8
    1059:	e9 d2 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    105e:	66 90                	xchg   %ax,%ax
    1060:	f3 0f 1e fb          	endbr32 
    1064:	68 10 00 00 00       	push   $0x10
    1069:	e9 c2 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    106e:	66 90                	xchg   %ax,%ax
    1070:	f3 0f 1e fb          	endbr32 
    1074:	68 18 00 00 00       	push   $0x18
    1079:	e9 b2 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    107e:	66 90                	xchg   %ax,%ax
    1080:	f3 0f 1e fb          	endbr32 
    1084:	68 20 00 00 00       	push   $0x20
    1089:	e9 a2 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    108e:	66 90                	xchg   %ax,%ax
    1090:	f3 0f 1e fb          	endbr32 
    1094:	68 28 00 00 00       	push   $0x28
    1099:	e9 92 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    109e:	66 90                	xchg   %ax,%ax
    10a0:	f3 0f 1e fb          	endbr32 
    10a4:	68 30 00 00 00       	push   $0x30
    10a9:	e9 82 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10ae:	66 90                	xchg   %ax,%ax
    10b0:	f3 0f 1e fb          	endbr32 
    10b4:	68 38 00 00 00       	push   $0x38
    10b9:	e9 72 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10be:	66 90                	xchg   %ax,%ax
    10c0:	f3 0f 1e fb          	endbr32 
    10c4:	68 40 00 00 00       	push   $0x40
    10c9:	e9 62 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10ce:	66 90                	xchg   %ax,%ax
    10d0:	f3 0f 1e fb          	endbr32 
    10d4:	68 48 00 00 00       	push   $0x48
    10d9:	e9 52 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10de:	66 90                	xchg   %ax,%ax
    10e0:	f3 0f 1e fb          	endbr32 
    10e4:	68 50 00 00 00       	push   $0x50
    10e9:	e9 42 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10ee:	66 90                	xchg   %ax,%ax
    10f0:	f3 0f 1e fb          	endbr32 
    10f4:	68 58 00 00 00       	push   $0x58
    10f9:	e9 32 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    10fe:	66 90                	xchg   %ax,%ax
    1100:	f3 0f 1e fb          	endbr32 
    1104:	68 60 00 00 00       	push   $0x60
    1109:	e9 22 ff ff ff       	jmp    1030 <__cxa_finalize@plt-0xe0>
    110e:	66 90                	xchg   %ax,%ax

Disassembly of section .plt.got:

00001110 <__cxa_finalize@plt>:
    1110:	f3 0f 1e fb          	endbr32 
    1114:	ff a3 44 00 00 00    	jmp    *0x44(%ebx)
    111a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001120 <exit@plt>:
    1120:	f3 0f 1e fb          	endbr32 
    1124:	ff a3 4c 00 00 00    	jmp    *0x4c(%ebx)
    112a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

Disassembly of section .plt.sec:

00001130 <read@plt>:
    1130:	f3 0f 1e fb          	endbr32 
    1134:	ff a3 0c 00 00 00    	jmp    *0xc(%ebx)
    113a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001140 <signal@plt>:
    1140:	f3 0f 1e fb          	endbr32 
    1144:	ff a3 10 00 00 00    	jmp    *0x10(%ebx)
    114a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001150 <alarm@plt>:
    1150:	f3 0f 1e fb          	endbr32 
    1154:	ff a3 14 00 00 00    	jmp    *0x14(%ebx)
    115a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001160 <perror@plt>:
    1160:	f3 0f 1e fb          	endbr32 
    1164:	ff a3 18 00 00 00    	jmp    *0x18(%ebx)
    116a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001170 <strcpy@plt>:
    1170:	f3 0f 1e fb          	endbr32 
    1174:	ff a3 1c 00 00 00    	jmp    *0x1c(%ebx)
    117a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001180 <open@plt>:
    1180:	f3 0f 1e fb          	endbr32 
    1184:	ff a3 20 00 00 00    	jmp    *0x20(%ebx)
    118a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

00001190 <srand@plt>:
    1190:	f3 0f 1e fb          	endbr32 
    1194:	ff a3 24 00 00 00    	jmp    *0x24(%ebx)
    119a:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011a0 <mmap@plt>:
    11a0:	f3 0f 1e fb          	endbr32 
    11a4:	ff a3 28 00 00 00    	jmp    *0x28(%ebx)
    11aa:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011b0 <__libc_start_main@plt>:
    11b0:	f3 0f 1e fb          	endbr32 
    11b4:	ff a3 2c 00 00 00    	jmp    *0x2c(%ebx)
    11ba:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011c0 <memset@plt>:
    11c0:	f3 0f 1e fb          	endbr32 
    11c4:	ff a3 30 00 00 00    	jmp    *0x30(%ebx)
    11ca:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011d0 <prctl@plt>:
    11d0:	f3 0f 1e fb          	endbr32 
    11d4:	ff a3 34 00 00 00    	jmp    *0x34(%ebx)
    11da:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011e0 <rand@plt>:
    11e0:	f3 0f 1e fb          	endbr32 
    11e4:	ff a3 38 00 00 00    	jmp    *0x38(%ebx)
    11ea:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

000011f0 <close@plt>:
    11f0:	f3 0f 1e fb          	endbr32 
    11f4:	ff a3 3c 00 00 00    	jmp    *0x3c(%ebx)
    11fa:	66 0f 1f 44 00 00    	nopw   0x0(%eax,%eax,1)

Disassembly of section .text:

00001200 <.text>:
    1200:	f3 0f 1e fb          	endbr32 
    1204:	31 ed                	xor    %ebp,%ebp
    1206:	5e                   	pop    %esi
    1207:	89 e1                	mov    %esp,%ecx
    1209:	83 e4 f0             	and    $0xfffffff0,%esp
    120c:	50                   	push   %eax
    120d:	54                   	push   %esp
    120e:	52                   	push   %edx
    120f:	e8 22 00 00 00       	call   1236 <close@plt+0x46>
    1214:	81 c3 94 2d 00 00    	add    $0x2d94,%ebx
    121a:	8d 83 28 d6 ff ff    	lea    -0x29d8(%ebx),%eax
    1220:	50                   	push   %eax
    1221:	8d 83 b8 d5 ff ff    	lea    -0x2a48(%ebx),%eax
    1227:	50                   	push   %eax
    1228:	51                   	push   %ecx
    1229:	56                   	push   %esi
    122a:	ff b3 50 00 00 00    	push   0x50(%ebx)
    1230:	e8 7b ff ff ff       	call   11b0 <__libc_start_main@plt>
    1235:	f4                   	hlt    
    1236:	8b 1c 24             	mov    (%esp),%ebx
    1239:	c3                   	ret    
    123a:	66 90                	xchg   %ax,%ax
    123c:	66 90                	xchg   %ax,%ax
    123e:	66 90                	xchg   %ax,%ax
    1240:	8b 1c 24             	mov    (%esp),%ebx
    1243:	c3                   	ret    
    1244:	66 90                	xchg   %ax,%ax
    1246:	66 90                	xchg   %ax,%ax
    1248:	66 90                	xchg   %ax,%ax
    124a:	66 90                	xchg   %ax,%ax
    124c:	66 90                	xchg   %ax,%ax
    124e:	66 90                	xchg   %ax,%ax
    1250:	e8 e4 00 00 00       	call   1339 <close@plt+0x149>
    1255:	81 c2 53 2d 00 00    	add    $0x2d53,%edx
    125b:	8d 8a 28 01 00 00    	lea    0x128(%edx),%ecx
    1261:	8d 82 28 01 00 00    	lea    0x128(%edx),%eax
    1267:	39 c8                	cmp    %ecx,%eax
    1269:	74 1d                	je     1288 <close@plt+0x98>
    126b:	8b 82 40 00 00 00    	mov    0x40(%edx),%eax
    1271:	85 c0                	test   %eax,%eax
    1273:	74 13                	je     1288 <close@plt+0x98>
    1275:	55                   	push   %ebp
    1276:	89 e5                	mov    %esp,%ebp
    1278:	83 ec 14             	sub    $0x14,%esp
    127b:	51                   	push   %ecx
    127c:	ff d0                	call   *%eax
    127e:	83 c4 10             	add    $0x10,%esp
    1281:	c9                   	leave  
    1282:	c3                   	ret    
    1283:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
    1287:	90                   	nop
    1288:	c3                   	ret    
    1289:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
    1290:	e8 a4 00 00 00       	call   1339 <close@plt+0x149>
    1295:	81 c2 13 2d 00 00    	add    $0x2d13,%edx
    129b:	55                   	push   %ebp
    129c:	89 e5                	mov    %esp,%ebp
    129e:	53                   	push   %ebx
    129f:	8d 8a 28 01 00 00    	lea    0x128(%edx),%ecx
    12a5:	8d 82 28 01 00 00    	lea    0x128(%edx),%eax
    12ab:	83 ec 04             	sub    $0x4,%esp
    12ae:	29 c8                	sub    %ecx,%eax
    12b0:	89 c3                	mov    %eax,%ebx
    12b2:	c1 e8 1f             	shr    $0x1f,%eax
    12b5:	c1 fb 02             	sar    $0x2,%ebx
    12b8:	01 d8                	add    %ebx,%eax
    12ba:	d1 f8                	sar    %eax
    12bc:	74 14                	je     12d2 <close@plt+0xe2>
    12be:	8b 92 54 00 00 00    	mov    0x54(%edx),%edx
    12c4:	85 d2                	test   %edx,%edx
    12c6:	74 0a                	je     12d2 <close@plt+0xe2>
    12c8:	83 ec 08             	sub    $0x8,%esp
    12cb:	50                   	push   %eax
    12cc:	51                   	push   %ecx
    12cd:	ff d2                	call   *%edx
    12cf:	83 c4 10             	add    $0x10,%esp
    12d2:	8b 5d fc             	mov    -0x4(%ebp),%ebx
    12d5:	c9                   	leave  
    12d6:	c3                   	ret    
    12d7:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
    12de:	66 90                	xchg   %ax,%ax
    12e0:	f3 0f 1e fb          	endbr32 
    12e4:	55                   	push   %ebp
    12e5:	89 e5                	mov    %esp,%ebp
    12e7:	53                   	push   %ebx
    12e8:	e8 53 ff ff ff       	call   1240 <close@plt+0x50>
    12ed:	81 c3 bb 2c 00 00    	add    $0x2cbb,%ebx
    12f3:	83 ec 04             	sub    $0x4,%esp
    12f6:	80 bb 28 01 00 00 00 	cmpb   $0x0,0x128(%ebx)
    12fd:	75 27                	jne    1326 <close@plt+0x136>
    12ff:	8b 83 44 00 00 00    	mov    0x44(%ebx),%eax
    1305:	85 c0                	test   %eax,%eax
    1307:	74 11                	je     131a <close@plt+0x12a>
    1309:	83 ec 0c             	sub    $0xc,%esp
    130c:	ff b3 5c 00 00 00    	push   0x5c(%ebx)
    1312:	e8 f9 fd ff ff       	call   1110 <__cxa_finalize@plt>
    1317:	83 c4 10             	add    $0x10,%esp
    131a:	e8 31 ff ff ff       	call   1250 <close@plt+0x60>
    131f:	c6 83 28 01 00 00 01 	movb   $0x1,0x128(%ebx)
    1326:	8b 5d fc             	mov    -0x4(%ebp),%ebx
    1329:	c9                   	leave  
    132a:	c3                   	ret    
    132b:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
    132f:	90                   	nop
    1330:	f3 0f 1e fb          	endbr32 
    1334:	e9 57 ff ff ff       	jmp    1290 <close@plt+0xa0>
    1339:	8b 14 24             	mov    (%esp),%edx
    133c:	c3                   	ret    
    133d:	f3 0f 1e fb          	endbr32 
    1341:	55                   	push   %ebp
    1342:	89 e5                	mov    %esp,%ebp
    1344:	53                   	push   %ebx
    1345:	83 ec 14             	sub    $0x14,%esp
    1348:	e8 f3 fe ff ff       	call   1240 <close@plt+0x50>
    134d:	81 c3 5b 2c 00 00    	add    $0x2c5b,%ebx
    1353:	66 c7 45 f0 0e 00    	movw   $0xe,-0x10(%ebp)
    1359:	8d 83 b8 00 00 00    	lea    0xb8(%ebx),%eax
    135f:	89 45 f4             	mov    %eax,-0xc(%ebp)
    1362:	83 ec 0c             	sub    $0xc,%esp
    1365:	6a 00                	push   $0x0
    1367:	6a 00                	push   $0x0
    1369:	6a 00                	push   $0x0
    136b:	6a 01                	push   $0x1
    136d:	6a 26                	push   $0x26
    136f:	e8 5c fe ff ff       	call   11d0 <prctl@plt>
    1374:	83 c4 20             	add    $0x20,%esp
    1377:	85 c0                	test   %eax,%eax
    1379:	79 1c                	jns    1397 <close@plt+0x1a7>
    137b:	83 ec 0c             	sub    $0xc,%esp
    137e:	8d 83 60 e0 ff ff    	lea    -0x1fa0(%ebx),%eax
    1384:	50                   	push   %eax
    1385:	e8 d6 fd ff ff       	call   1160 <perror@plt>
    138a:	83 c4 10             	add    $0x10,%esp
    138d:	83 ec 0c             	sub    $0xc,%esp
    1390:	6a 02                	push   $0x2
    1392:	e8 89 fd ff ff       	call   1120 <exit@plt>
    1397:	83 ec 04             	sub    $0x4,%esp
    139a:	8d 45 f0             	lea    -0x10(%ebp),%eax
    139d:	50                   	push   %eax
    139e:	6a 02                	push   $0x2
    13a0:	6a 16                	push   $0x16
    13a2:	e8 29 fe ff ff       	call   11d0 <prctl@plt>
    13a7:	83 c4 10             	add    $0x10,%esp
    13aa:	85 c0                	test   %eax,%eax
    13ac:	79 1c                	jns    13ca <close@plt+0x1da>
    13ae:	83 ec 0c             	sub    $0xc,%esp
    13b1:	8d 83 7b e0 ff ff    	lea    -0x1f85(%ebx),%eax
    13b7:	50                   	push   %eax
    13b8:	e8 a3 fd ff ff       	call   1160 <perror@plt>
    13bd:	83 c4 10             	add    $0x10,%esp
    13c0:	83 ec 0c             	sub    $0xc,%esp
    13c3:	6a 02                	push   $0x2
    13c5:	e8 56 fd ff ff       	call   1120 <exit@plt>
    13ca:	90                   	nop
    13cb:	8b 5d fc             	mov    -0x4(%ebp),%ebx
    13ce:	c9                   	leave  
    13cf:	c3                   	ret    
    13d0:	f3 0f 1e fb          	endbr32 
    13d4:	55                   	push   %ebp
    13d5:	89 e5                	mov    %esp,%ebp
    13d7:	53                   	push   %ebx
    13d8:	83 ec 14             	sub    $0x14,%esp
    13db:	e8 60 fe ff ff       	call   1240 <close@plt+0x50>
    13e0:	81 c3 c8 2b 00 00    	add    $0x2bc8,%ebx
    13e6:	83 ec 08             	sub    $0x8,%esp
    13e9:	6a 00                	push   $0x0
    13eb:	8d 83 91 e0 ff ff    	lea    -0x1f6f(%ebx),%eax
    13f1:	50                   	push   %eax
    13f2:	e8 89 fd ff ff       	call   1180 <open@plt>
    13f7:	83 c4 10             	add    $0x10,%esp
    13fa:	89 45 f0             	mov    %eax,-0x10(%ebp)
    13fd:	83 ec 04             	sub    $0x4,%esp
    1400:	6a 08                	push   $0x8
    1402:	8d 45 e8             	lea    -0x18(%ebp),%eax
    1405:	50                   	push   %eax
    1406:	ff 75 f0             	push   -0x10(%ebp)
    1409:	e8 22 fd ff ff       	call   1130 <read@plt>
    140e:	83 c4 10             	add    $0x10,%esp
    1411:	83 ec 0c             	sub    $0xc,%esp
    1414:	ff 75 f0             	push   -0x10(%ebp)
    1417:	e8 d4 fd ff ff       	call   11f0 <close@plt>
    141c:	83 c4 10             	add    $0x10,%esp
    141f:	8b 45 e8             	mov    -0x18(%ebp),%eax
    1422:	8b 55 ec             	mov    -0x14(%ebp),%edx
    1425:	83 ec 0c             	sub    $0xc,%esp
    1428:	50                   	push   %eax
    1429:	e8 62 fd ff ff       	call   1190 <srand@plt>
    142e:	83 c4 10             	add    $0x10,%esp
    1431:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
    1438:	eb 0b                	jmp    1445 <close@plt+0x255>
    143a:	e8 a1 fd ff ff       	call   11e0 <rand@plt>
    143f:	c1 e0 10             	shl    $0x10,%eax
    1442:	89 45 f4             	mov    %eax,-0xc(%ebp)
    1445:	81 7d f4 ff ff ff 5f 	cmpl   $0x5fffffff,-0xc(%ebp)
    144c:	7e ec                	jle    143a <close@plt+0x24a>
    144e:	8b 45 f4             	mov    -0xc(%ebp),%eax
    1451:	3d 00 00 00 f7       	cmp    $0xf7000000,%eax
    1456:	77 e2                	ja     143a <close@plt+0x24a>
    1458:	8b 45 f4             	mov    -0xc(%ebp),%eax
    145b:	8b 5d fc             	mov    -0x4(%ebp),%ebx
    145e:	c9                   	leave  
    145f:	c3                   	ret    
    1460:	f3 0f 1e fb          	endbr32 
    1464:	8d 4c 24 04          	lea    0x4(%esp),%ecx
    1468:	83 e4 f0             	and    $0xfffffff0,%esp
    146b:	ff 71 fc             	push   -0x4(%ecx)
    146e:	55                   	push   %ebp
    146f:	89 e5                	mov    %esp,%ebp
    1471:	53                   	push   %ebx
    1472:	51                   	push   %ecx
    1473:	83 ec 10             	sub    $0x10,%esp
    1476:	e8 c5 fd ff ff       	call   1240 <close@plt+0x50>
    147b:	81 c3 2d 2b 00 00    	add    $0x2b2d,%ebx
    1481:	e8 4a ff ff ff       	call   13d0 <close@plt+0x1e0>
    1486:	89 45 f4             	mov    %eax,-0xc(%ebp)
    1489:	83 ec 08             	sub    $0x8,%esp
    148c:	8b 83 4c 00 00 00    	mov    0x4c(%ebx),%eax
    1492:	50                   	push   %eax
    1493:	6a 0e                	push   $0xe
    1495:	e8 a6 fc ff ff       	call   1140 <signal@plt>
    149a:	83 c4 10             	add    $0x10,%esp
    149d:	83 ec 0c             	sub    $0xc,%esp
    14a0:	6a 0a                	push   $0xa
    14a2:	e8 a9 fc ff ff       	call   1150 <alarm@plt>
    14a7:	83 c4 10             	add    $0x10,%esp
    14aa:	8b 45 f4             	mov    -0xc(%ebp),%eax
    14ad:	83 ec 08             	sub    $0x8,%esp
    14b0:	6a 00                	push   $0x0
    14b2:	6a ff                	push   $0xffffffff
    14b4:	6a 31                	push   $0x31
    14b6:	6a 03                	push   $0x3
    14b8:	68 00 10 00 00       	push   $0x1000
    14bd:	50                   	push   %eax
    14be:	e8 dd fc ff ff       	call   11a0 <mmap@plt>
    14c3:	83 c4 20             	add    $0x20,%esp
    14c6:	89 45 f0             	mov    %eax,-0x10(%ebp)
    14c9:	83 7d f0 ff          	cmpl   $0xffffffff,-0x10(%ebp)
    14cd:	75 0a                	jne    14d9 <close@plt+0x2e9>
    14cf:	83 ec 0c             	sub    $0xc,%esp
    14d2:	6a ff                	push   $0xffffffff
    14d4:	e8 47 fc ff ff       	call   1120 <exit@plt>
    14d9:	83 ec 08             	sub    $0x8,%esp
    14dc:	8d 83 78 00 00 00    	lea    0x78(%ebx),%eax
    14e2:	50                   	push   %eax
    14e3:	ff 75 f0             	push   -0x10(%ebp)
    14e6:	e8 85 fc ff ff       	call   1170 <strcpy@plt>
    14eb:	83 c4 10             	add    $0x10,%esp
    14ee:	83 ec 04             	sub    $0x4,%esp
    14f1:	6a 25                	push   $0x25
    14f3:	6a 00                	push   $0x0
    14f5:	8d 83 78 00 00 00    	lea    0x78(%ebx),%eax
    14fb:	50                   	push   %eax
    14fc:	e8 bf fc ff ff       	call   11c0 <memset@plt>
    1501:	83 c4 10             	add    $0x10,%esp
    1504:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
    150b:	e8 2d fe ff ff       	call   133d <close@plt+0x14d>
    1510:	83 ec 08             	sub    $0x8,%esp
    1513:	6a 00                	push   $0x0
    1515:	6a ff                	push   $0xffffffff
    1517:	6a 21                	push   $0x21
    1519:	6a 07                	push   $0x7
    151b:	68 00 10 00 00       	push   $0x1000
    1520:	6a 00                	push   $0x0
    1522:	e8 79 fc ff ff       	call   11a0 <mmap@plt>
    1527:	83 c4 20             	add    $0x20,%esp
    152a:	89 45 ec             	mov    %eax,-0x14(%ebp)
    152d:	83 ec 04             	sub    $0x4,%esp
    1530:	6a 3c                	push   $0x3c
    1532:	ff 75 ec             	push   -0x14(%ebp)
    1535:	6a 00                	push   $0x0
    1537:	e8 f4 fb ff ff       	call   1130 <read@plt>
    153c:	83 c4 10             	add    $0x10,%esp
    153f:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
    1546:	00 
    1547:	8b 45 ec             	mov    -0x14(%ebp),%eax
    154a:	ff d0                	call   *%eax
    154c:	b8 00 00 00 00       	mov    $0x0,%eax
    1551:	8d 65 f8             	lea    -0x8(%ebp),%esp
    1554:	59                   	pop    %ecx
    1555:	5b                   	pop    %ebx
    1556:	5d                   	pop    %ebp
    1557:	8d 61 fc             	lea    -0x4(%ecx),%esp
    155a:	c3                   	ret    
    155b:	66 90                	xchg   %ax,%ax
    155d:	66 90                	xchg   %ax,%ax
    155f:	90                   	nop
    1560:	f3 0f 1e fb          	endbr32 
    1564:	55                   	push   %ebp
    1565:	e8 6b 00 00 00       	call   15d5 <close@plt+0x3e5>
    156a:	81 c5 3e 2a 00 00    	add    $0x2a3e,%ebp
    1570:	57                   	push   %edi
    1571:	56                   	push   %esi
    1572:	53                   	push   %ebx
    1573:	83 ec 0c             	sub    $0xc,%esp
    1576:	89 eb                	mov    %ebp,%ebx
    1578:	8b 7c 24 28          	mov    0x28(%esp),%edi
    157c:	e8 7f fa ff ff       	call   1000 <__cxa_finalize@plt-0x110>
    1581:	8d 9d 04 ff ff ff    	lea    -0xfc(%ebp),%ebx
    1587:	8d 85 00 ff ff ff    	lea    -0x100(%ebp),%eax
    158d:	29 c3                	sub    %eax,%ebx
    158f:	c1 fb 02             	sar    $0x2,%ebx
    1592:	74 29                	je     15bd <close@plt+0x3cd>
    1594:	31 f6                	xor    %esi,%esi
    1596:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
    159d:	8d 76 00             	lea    0x0(%esi),%esi
    15a0:	83 ec 04             	sub    $0x4,%esp
    15a3:	57                   	push   %edi
    15a4:	ff 74 24 2c          	push   0x2c(%esp)
    15a8:	ff 74 24 2c          	push   0x2c(%esp)
    15ac:	ff 94 b5 00 ff ff ff 	call   *-0x100(%ebp,%esi,4)
    15b3:	83 c6 01             	add    $0x1,%esi
    15b6:	83 c4 10             	add    $0x10,%esp
    15b9:	39 f3                	cmp    %esi,%ebx
    15bb:	75 e3                	jne    15a0 <close@plt+0x3b0>
    15bd:	83 c4 0c             	add    $0xc,%esp
    15c0:	5b                   	pop    %ebx
    15c1:	5e                   	pop    %esi
    15c2:	5f                   	pop    %edi
    15c3:	5d                   	pop    %ebp
    15c4:	c3                   	ret    
    15c5:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
    15cc:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
    15d0:	f3 0f 1e fb          	endbr32 
    15d4:	c3                   	ret    
    15d5:	8b 2c 24             	mov    (%esp),%ebp
    15d8:	c3                   	ret    

Disassembly of section .fini:

000015dc <.fini>:
    15dc:	f3 0f 1e fb          	endbr32 
    15e0:	53                   	push   %ebx
    15e1:	83 ec 08             	sub    $0x8,%esp
    15e4:	e8 57 fc ff ff       	call   1240 <close@plt+0x50>
    15e9:	81 c3 bf 29 00 00    	add    $0x29bf,%ebx
    15ef:	83 c4 08             	add    $0x8,%esp
    15f2:	5b                   	pop    %ebx
    15f3:	c3                   	ret    

Disassembly of section .rodata:

00002000 <_IO_stdin_used@@Base-0x4>:
    2000:	03 00                	add    (%eax),%eax
	...

00002004 <_IO_stdin_used@@Base>:
    2004:	01 00                	add    %eax,(%eax)
    2006:	02 00                	add    (%eax),%al
    2008:	70 72                	jo     207c <_IO_stdin_used@@Base+0x78>
    200a:	63 74 6c 28          	arpl   %si,0x28(%esp,%ebp,2)
    200e:	50                   	push   %eax
    200f:	52                   	push   %edx
    2010:	5f                   	pop    %edi
    2011:	53                   	push   %ebx
    2012:	45                   	inc    %ebp
    2013:	54                   	push   %esp
    2014:	5f                   	pop    %edi
    2015:	4e                   	dec    %esi
    2016:	4f                   	dec    %edi
    2017:	5f                   	pop    %edi
    2018:	4e                   	dec    %esi
    2019:	45                   	inc    %ebp
    201a:	57                   	push   %edi
    201b:	5f                   	pop    %edi
    201c:	50                   	push   %eax
    201d:	52                   	push   %edx
    201e:	49                   	dec    %ecx
    201f:	56                   	push   %esi
    2020:	53                   	push   %ebx
    2021:	29 00                	sub    %eax,(%eax)
    2023:	70 72                	jo     2097 <_IO_stdin_used@@Base+0x93>
    2025:	63 74 6c 28          	arpl   %si,0x28(%esp,%ebp,2)
    2029:	50                   	push   %eax
    202a:	52                   	push   %edx
    202b:	5f                   	pop    %edi
    202c:	53                   	push   %ebx
    202d:	45                   	inc    %ebp
    202e:	54                   	push   %esp
    202f:	5f                   	pop    %edi
    2030:	53                   	push   %ebx
    2031:	45                   	inc    %ebp
    2032:	43                   	inc    %ebx
    2033:	43                   	inc    %ebx
    2034:	4f                   	dec    %edi
    2035:	4d                   	dec    %ebp
    2036:	50                   	push   %eax
    2037:	29 00                	sub    %eax,(%eax)
    2039:	2f                   	das    
    203a:	64 65 76 2f          	fs gs jbe 206d <_IO_stdin_used@@Base+0x69>
    203e:	75 72                	jne    20b2 <_IO_stdin_used@@Base+0xae>
    2040:	61                   	popa   
    2041:	6e                   	outsb  %ds:(%esi),(%dx)
    2042:	64 6f                	outsl  %fs:(%esi),(%dx)
    2044:	6d                   	insl   (%dx),%es:(%edi)
	...

Disassembly of section .eh_frame_hdr:

00002048 <.eh_frame_hdr>:
    2048:	01 1b                	add    %ebx,(%ebx)
    204a:	03 3b                	add    (%ebx),%edi
    204c:	58                   	pop    %eax
    204d:	00 00                	add    %al,(%eax)
    204f:	00 0a                	add    %cl,(%edx)
    2051:	00 00                	add    %al,(%eax)
    2053:	00 e8                	add    %ch,%al
    2055:	ef                   	out    %eax,(%dx)
    2056:	ff                   	(bad)  
    2057:	ff 88 00 00 00 c8    	decl   -0x38000000(%eax)
    205d:	f0 ff                	lock (bad) 
    205f:	ff ac 00 00 00 e8 f0 	ljmp   *-0xf180000(%eax,%eax,1)
    2066:	ff                   	(bad)  
    2067:	ff c0                	inc    %eax
    2069:	00 00                	add    %al,(%eax)
    206b:	00 b8 f1 ff ff 74    	add    %bh,0x74fffff1(%eax)
    2071:	00 00                	add    %al,(%eax)
    2073:	00 f5                	add    %dh,%ch
    2075:	f2 ff                	repnz (bad) 
    2077:	ff d4                	call   *%esp
    2079:	00 00                	add    %al,(%eax)
    207b:	00 88 f3 ff ff f8    	add    %cl,-0x700000d(%eax)
    2081:	00 00                	add    %al,(%eax)
    2083:	00 18                	add    %bl,(%eax)
    2085:	f4                   	hlt    
    2086:	ff                   	(bad)  
    2087:	ff 1c 01             	lcall  *(%ecx,%eax,1)
    208a:	00 00                	add    %al,(%eax)
    208c:	18 f5                	sbb    %dh,%ch
    208e:	ff                   	(bad)  
    208f:	ff 50 01             	call   *0x1(%eax)
    2092:	00 00                	add    %al,(%eax)
    2094:	88 f5                	mov    %dh,%ch
    2096:	ff                   	(bad)  
    2097:	ff 9c 01 00 00 8d f5 	lcall  *-0xa730000(%ecx,%eax,1)
    209e:	ff                   	(bad)  
    209f:	ff                   	.byte 0xff
    20a0:	b0 01                	mov    $0x1,%al
	...

Disassembly of section .eh_frame:

000020a4 <.eh_frame>:
    20a4:	14 00                	adc    $0x0,%al
    20a6:	00 00                	add    %al,(%eax)
    20a8:	00 00                	add    %al,(%eax)
    20aa:	00 00                	add    %al,(%eax)
    20ac:	01 7a 52             	add    %edi,0x52(%edx)
    20af:	00 01                	add    %al,(%ecx)
    20b1:	7c 08                	jl     20bb <_IO_stdin_used@@Base+0xb7>
    20b3:	01 1b                	add    %ebx,(%ebx)
    20b5:	0c 04                	or     $0x4,%al
    20b7:	04 88                	add    $0x88,%al
    20b9:	01 00                	add    %eax,(%eax)
    20bb:	00 10                	add    %dl,(%eax)
    20bd:	00 00                	add    %al,(%eax)
    20bf:	00 1c 00             	add    %bl,(%eax,%eax,1)
    20c2:	00 00                	add    %al,(%eax)
    20c4:	3c f1                	cmp    $0xf1,%al
    20c6:	ff                   	(bad)  
    20c7:	ff                   	(bad)  
    20c8:	3a 00                	cmp    (%eax),%al
    20ca:	00 00                	add    %al,(%eax)
    20cc:	00 44 07 08          	add    %al,0x8(%edi,%eax,1)
    20d0:	20 00                	and    %al,(%eax)
    20d2:	00 00                	add    %al,(%eax)
    20d4:	30 00                	xor    %al,(%eax)
    20d6:	00 00                	add    %al,(%eax)
    20d8:	58                   	pop    %eax
    20d9:	ef                   	out    %eax,(%dx)
    20da:	ff                   	(bad)  
    20db:	ff e0                	jmp    *%eax
    20dd:	00 00                	add    %al,(%eax)
    20df:	00 00                	add    %al,(%eax)
    20e1:	0e                   	push   %cs
    20e2:	08 46 0e             	or     %al,0xe(%esi)
    20e5:	0c 4a                	or     $0x4a,%al
    20e7:	0f 0b                	ud2    
    20e9:	74 04                	je     20ef <_IO_stdin_used@@Base+0xeb>
    20eb:	78 00                	js     20ed <_IO_stdin_used@@Base+0xe9>
    20ed:	3f                   	aas    
    20ee:	1a 39                	sbb    (%ecx),%bh
    20f0:	2a 32                	sub    (%edx),%dh
    20f2:	24 22                	and    $0x22,%al
    20f4:	10 00                	adc    %al,(%eax)
    20f6:	00 00                	add    %al,(%eax)
    20f8:	54                   	push   %esp
    20f9:	00 00                	add    %al,(%eax)
    20fb:	00 14 f0             	add    %dl,(%eax,%esi,8)
    20fe:	ff                   	(bad)  
    20ff:	ff 20                	jmp    *(%eax)
    2101:	00 00                	add    %al,(%eax)
    2103:	00 00                	add    %al,(%eax)
    2105:	00 00                	add    %al,(%eax)
    2107:	00 10                	add    %dl,(%eax)
    2109:	00 00                	add    %al,(%eax)
    210b:	00 68 00             	add    %ch,0x0(%eax)
    210e:	00 00                	add    %al,(%eax)
    2110:	20 f0                	and    %dh,%al
    2112:	ff                   	(bad)  
    2113:	ff d0                	call   *%eax
    2115:	00 00                	add    %al,(%eax)
    2117:	00 00                	add    %al,(%eax)
    2119:	00 00                	add    %al,(%eax)
    211b:	00 20                	add    %ah,(%eax)
    211d:	00 00                	add    %al,(%eax)
    211f:	00 7c 00 00          	add    %bh,0x0(%eax,%eax,1)
    2123:	00 19                	add    %bl,(%ecx)
    2125:	f2 ff                	repnz (bad) 
    2127:	ff 93 00 00 00 00    	call   *0x0(%ebx)
    212d:	45                   	inc    %ebp
    212e:	0e                   	push   %cs
    212f:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
    2135:	44                   	inc    %esp
    2136:	83 03 02             	addl   $0x2,(%ebx)
    2139:	87 c5                	xchg   %eax,%ebp
    213b:	c3                   	ret    
    213c:	0c 04                	or     $0x4,%al
    213e:	04 00                	add    $0x0,%al
    2140:	20 00                	and    %al,(%eax)
    2142:	00 00                	add    %al,(%eax)
    2144:	a0 00 00 00 88       	mov    0x88000000,%al
    2149:	f2 ff                	repnz (bad) 
    214b:	ff 90 00 00 00 00    	call   *0x0(%eax)
    2151:	45                   	inc    %ebp
    2152:	0e                   	push   %cs
    2153:	08 85 02 42 0d 05    	or     %al,0x50d4202(%ebp)
    2159:	44                   	inc    %esp
    215a:	83 03 02             	addl   $0x2,(%ebx)
    215d:	84 c5                	test   %al,%ch
    215f:	c3                   	ret    
    2160:	0c 04                	or     $0x4,%al
    2162:	04 00                	add    $0x0,%al
    2164:	30 00                	xor    %al,(%eax)
    2166:	00 00                	add    %al,(%eax)
    2168:	c4 00                	les    (%eax),%eax
    216a:	00 00                	add    %al,(%eax)
    216c:	f4                   	hlt    
    216d:	f2 ff                	repnz (bad) 
    216f:	ff                   	(bad)  
    2170:	fb                   	sti    
    2171:	00 00                	add    %al,(%eax)
    2173:	00 00                	add    %al,(%eax)
    2175:	48                   	dec    %eax
    2176:	0c 01                	or     $0x1,%al
    2178:	00 49 10             	add    %cl,0x10(%ecx)
    217b:	05 02 75 00 42       	add    $0x42007502,%eax
    2180:	0f 03 75 78          	lsl    0x78(%ebp),%esi
    2184:	06                   	push   %es
    2185:	10 03                	adc    %al,(%ebx)
    2187:	02 75 7c             	add    0x7c(%ebp),%dh
    218a:	02 e2                	add    %dl,%ah
    218c:	c1 0c 01 00          	rorl   $0x0,(%ecx,%eax,1)
    2190:	41                   	inc    %ecx
    2191:	c3                   	ret    
    2192:	41                   	inc    %ecx
    2193:	c5 43 0c             	lds    0xc(%ebx),%eax
    2196:	04 04                	add    $0x4,%al
    2198:	48                   	dec    %eax
    2199:	00 00                	add    %al,(%eax)
    219b:	00 f8                	add    %bh,%al
    219d:	00 00                	add    %al,(%eax)
    219f:	00 c0                	add    %al,%al
    21a1:	f3 ff                	repz (bad) 
    21a3:	ff 65 00             	jmp    *0x0(%ebp)
    21a6:	00 00                	add    %al,(%eax)
    21a8:	00 45 0e             	add    %al,0xe(%ebp)
    21ab:	08 85 02 4c 0e 0c    	or     %al,0xc0e4c02(%ebp)
    21b1:	87 03                	xchg   %eax,(%ebx)
    21b3:	41                   	inc    %ecx
    21b4:	0e                   	push   %cs
    21b5:	10 86 04 41 0e 14    	adc    %al,0x140e4104(%esi)
    21bb:	83 05 43 0e 20 6d 0e 	addl   $0xe,0x6d200e43
    21c2:	24 41                	and    $0x41,%al
    21c4:	0e                   	push   %cs
    21c5:	28 44 0e 2c          	sub    %al,0x2c(%esi,%ecx,1)
    21c9:	44                   	inc    %esp
    21ca:	0e                   	push   %cs
    21cb:	30 4d 0e             	xor    %cl,0xe(%ebp)
    21ce:	20 47 0e             	and    %al,0xe(%edi)
    21d1:	14 41                	adc    $0x41,%al
    21d3:	c3                   	ret    
    21d4:	0e                   	push   %cs
    21d5:	10 41 c6             	adc    %al,-0x3a(%ecx)
    21d8:	0e                   	push   %cs
    21d9:	0c 41                	or     $0x41,%al
    21db:	c7                   	(bad)  
    21dc:	0e                   	push   %cs
    21dd:	08 41 c5             	or     %al,-0x3b(%ecx)
    21e0:	0e                   	push   %cs
    21e1:	04 00                	add    $0x0,%al
    21e3:	00 10                	add    %dl,(%eax)
    21e5:	00 00                	add    %al,(%eax)
    21e7:	00 44 01 00          	add    %al,0x0(%ecx,%eax,1)
    21eb:	00 e4                	add    %ah,%ah
    21ed:	f3 ff                	repz (bad) 
    21ef:	ff 05 00 00 00 00    	incl   0x0
    21f5:	00 00                	add    %al,(%eax)
    21f7:	00 10                	add    %dl,(%eax)
    21f9:	00 00                	add    %al,(%eax)
    21fb:	00 58 01             	add    %bl,0x1(%eax)
    21fe:	00 00                	add    %al,(%eax)
    2200:	d5 f3                	aad    $0xf3
    2202:	ff                   	(bad)  
    2203:	ff 04 00             	incl   (%eax,%eax,1)
	...

Disassembly of section .init_array:

00003ea8 <.init_array>:
    3ea8:	30 13                	xor    %dl,(%ebx)
	...

Disassembly of section .fini_array:

00003eac <.fini_array>:
    3eac:	e0 12                	loopne 3ec0 <_IO_stdin_used@@Base+0x1ebc>
	...

Disassembly of section .dynamic:

00003eb0 <.dynamic>:
    3eb0:	01 00                	add    %eax,(%eax)
    3eb2:	00 00                	add    %al,(%eax)
    3eb4:	01 00                	add    %eax,(%eax)
    3eb6:	00 00                	add    %al,(%eax)
    3eb8:	0c 00                	or     $0x0,%al
    3eba:	00 00                	add    %al,(%eax)
    3ebc:	00 10                	add    %dl,(%eax)
    3ebe:	00 00                	add    %al,(%eax)
    3ec0:	0d 00 00 00 dc       	or     $0xdc000000,%eax
    3ec5:	15 00 00 19 00       	adc    $0x190000,%eax
    3eca:	00 00                	add    %al,(%eax)
    3ecc:	a8 3e                	test   $0x3e,%al
    3ece:	00 00                	add    %al,(%eax)
    3ed0:	1b 00                	sbb    (%eax),%eax
    3ed2:	00 00                	add    %al,(%eax)
    3ed4:	04 00                	add    $0x0,%al
    3ed6:	00 00                	add    %al,(%eax)
    3ed8:	1a 00                	sbb    (%eax),%al
    3eda:	00 00                	add    %al,(%eax)
    3edc:	ac                   	lods   %ds:(%esi),%al
    3edd:	3e 00 00             	add    %al,%ds:(%eax)
    3ee0:	1c 00                	sbb    $0x0,%al
    3ee2:	00 00                	add    %al,(%eax)
    3ee4:	04 00                	add    $0x0,%al
    3ee6:	00 00                	add    %al,(%eax)
    3ee8:	f5                   	cmc    
    3ee9:	fe                   	(bad)  
    3eea:	ff 6f 28             	ljmp   *0x28(%edi)
    3eed:	02 00                	add    (%eax),%al
    3eef:	00 05 00 00 00 88    	add    %al,0x88000000
    3ef5:	03 00                	add    (%eax),%eax
    3ef7:	00 06                	add    %al,(%esi)
    3ef9:	00 00                	add    %al,(%eax)
    3efb:	00 48 02             	add    %cl,0x2(%eax)
    3efe:	00 00                	add    %al,(%eax)
    3f00:	0a 00                	or     (%eax),%al
    3f02:	00 00                	add    %al,(%eax)
    3f04:	de 00                	fiadds (%eax)
    3f06:	00 00                	add    %al,(%eax)
    3f08:	0b 00                	or     (%eax),%eax
    3f0a:	00 00                	add    %al,(%eax)
    3f0c:	10 00                	adc    %al,(%eax)
    3f0e:	00 00                	add    %al,(%eax)
    3f10:	15 00 00 00 00       	adc    $0x0,%eax
    3f15:	00 00                	add    %al,(%eax)
    3f17:	00 03                	add    %al,(%ebx)
    3f19:	00 00                	add    %al,(%eax)
    3f1b:	00 a8 3f 00 00 02    	add    %ch,0x200003f(%eax)
    3f21:	00 00                	add    %al,(%eax)
    3f23:	00 68 00             	add    %ch,0x0(%eax)
    3f26:	00 00                	add    %al,(%eax)
    3f28:	14 00                	adc    $0x0,%al
    3f2a:	00 00                	add    %al,(%eax)
    3f2c:	11 00                	adc    %eax,(%eax)
    3f2e:	00 00                	add    %al,(%eax)
    3f30:	17                   	pop    %ss
    3f31:	00 00                	add    %al,(%eax)
    3f33:	00 08                	add    %cl,(%eax)
    3f35:	05 00 00 11 00       	add    $0x110000,%eax
    3f3a:	00 00                	add    %al,(%eax)
    3f3c:	c0 04 00 00          	rolb   $0x0,(%eax,%eax,1)
    3f40:	12 00                	adc    (%eax),%al
    3f42:	00 00                	add    %al,(%eax)
    3f44:	48                   	dec    %eax
    3f45:	00 00                	add    %al,(%eax)
    3f47:	00 13                	add    %dl,(%ebx)
    3f49:	00 00                	add    %al,(%eax)
    3f4b:	00 08                	add    %cl,(%eax)
    3f4d:	00 00                	add    %al,(%eax)
    3f4f:	00 1e                	add    %bl,(%esi)
    3f51:	00 00                	add    %al,(%eax)
    3f53:	00 08                	add    %cl,(%eax)
    3f55:	00 00                	add    %al,(%eax)
    3f57:	00 fb                	add    %bh,%bl
    3f59:	ff                   	(bad)  
    3f5a:	ff 6f 01             	ljmp   *0x1(%edi)
    3f5d:	00 00                	add    %al,(%eax)
    3f5f:	08 fe                	or     %bh,%dh
    3f61:	ff                   	(bad)  
    3f62:	ff 6f 90             	ljmp   *-0x70(%edi)
    3f65:	04 00                	add    $0x0,%al
    3f67:	00 ff                	add    %bh,%bh
    3f69:	ff                   	(bad)  
    3f6a:	ff 6f 01             	ljmp   *0x1(%edi)
    3f6d:	00 00                	add    %al,(%eax)
    3f6f:	00 f0                	add    %dh,%al
    3f71:	ff                   	(bad)  
    3f72:	ff 6f 66             	ljmp   *0x66(%edi)
    3f75:	04 00                	add    $0x0,%al
    3f77:	00 fa                	add    %bh,%dl
    3f79:	ff                   	(bad)  
    3f7a:	ff 6f 04             	ljmp   *0x4(%edi)
	...

Disassembly of section .got:

00003fa8 <.got>:
    3fa8:	b0 3e                	mov    $0x3e,%al
	...
    3fb2:	00 00                	add    %al,(%eax)
    3fb4:	40                   	inc    %eax
    3fb5:	10 00                	adc    %al,(%eax)
    3fb7:	00 50 10             	add    %dl,0x10(%eax)
    3fba:	00 00                	add    %al,(%eax)
    3fbc:	60                   	pusha  
    3fbd:	10 00                	adc    %al,(%eax)
    3fbf:	00 70 10             	add    %dh,0x10(%eax)
    3fc2:	00 00                	add    %al,(%eax)
    3fc4:	80 10 00             	adcb   $0x0,(%eax)
    3fc7:	00 90 10 00 00 a0    	add    %dl,-0x5ffffff0(%eax)
    3fcd:	10 00                	adc    %al,(%eax)
    3fcf:	00 b0 10 00 00 c0    	add    %dh,-0x3ffffff0(%eax)
    3fd5:	10 00                	adc    %al,(%eax)
    3fd7:	00 d0                	add    %dl,%al
    3fd9:	10 00                	adc    %al,(%eax)
    3fdb:	00 e0                	add    %ah,%al
    3fdd:	10 00                	adc    %al,(%eax)
    3fdf:	00 f0                	add    %dh,%al
    3fe1:	10 00                	adc    %al,(%eax)
    3fe3:	00 00                	add    %al,(%eax)
    3fe5:	11 00                	adc    %eax,(%eax)
	...
    3ff7:	00 60 14             	add    %ah,0x14(%eax)
    3ffa:	00 00                	add    %al,(%eax)
    3ffc:	00 00                	add    %al,(%eax)
	...

Disassembly of section .data:

00004000 <.data>:
    4000:	00 00                	add    %al,(%eax)
    4002:	00 00                	add    %al,(%eax)
    4004:	04 40                	add    $0x40,%al
	...
    401e:	00 00                	add    %al,(%eax)
    4020:	48                   	dec    %eax
    4021:	54                   	push   %esp
    4022:	42                   	inc    %edx
    4023:	7b 58                	jnp    407d <_IO_stdin_used@@Base+0x2079>
    4025:	58                   	pop    %eax
    4026:	58                   	pop    %eax
    4027:	58                   	pop    %eax
    4028:	58                   	pop    %eax
    4029:	58                   	pop    %eax
    402a:	58                   	pop    %eax
    402b:	58                   	pop    %eax
    402c:	58                   	pop    %eax
    402d:	58                   	pop    %eax
    402e:	58                   	pop    %eax
    402f:	58                   	pop    %eax
    4030:	58                   	pop    %eax
    4031:	58                   	pop    %eax
    4032:	58                   	pop    %eax
    4033:	58                   	pop    %eax
    4034:	58                   	pop    %eax
    4035:	58                   	pop    %eax
    4036:	58                   	pop    %eax
    4037:	58                   	pop    %eax
    4038:	58                   	pop    %eax
    4039:	58                   	pop    %eax
    403a:	58                   	pop    %eax
    403b:	58                   	pop    %eax
    403c:	58                   	pop    %eax
    403d:	58                   	pop    %eax
    403e:	58                   	pop    %eax
    403f:	58                   	pop    %eax
    4040:	58                   	pop    %eax
    4041:	58                   	pop    %eax
    4042:	58                   	pop    %eax
    4043:	7d 00                	jge    4045 <_IO_stdin_used@@Base+0x2041>
	...
    405d:	00 00                	add    %al,(%eax)
    405f:	00 20                	add    %ah,(%eax)
    4061:	00 00                	add    %al,(%eax)
    4063:	00 04 00             	add    %al,(%eax,%eax,1)
    4066:	00 00                	add    %al,(%eax)
    4068:	20 00                	and    %al,(%eax)
    406a:	00 00                	add    %al,(%eax)
    406c:	00 00                	add    %al,(%eax)
    406e:	00 00                	add    %al,(%eax)
    4070:	35 00 0a 00 00       	xor    $0xa00,%eax
    4075:	00 00                	add    %al,(%eax)
    4077:	40                   	inc    %eax
    4078:	15 00 09 00 0b       	adc    $0xb000900,%eax
    407d:	00 00                	add    %al,(%eax)
    407f:	00 15 00 08 00 66    	add    %dl,0x66000800
    4085:	01 00                	add    %eax,(%eax)
    4087:	00 15 00 07 00 27    	add    %dl,0x27000700
    408d:	01 00                	add    %eax,(%eax)
    408f:	00 15 00 06 00 05    	add    %dl,0x5000600
    4095:	00 00                	add    %al,(%eax)
    4097:	00 15 00 05 00 06    	add    %dl,0x6000500
    409d:	00 00                	add    %al,(%eax)
    409f:	00 15 00 04 00 08    	add    %dl,0x8000400
    40a5:	00 00                	add    %al,(%eax)
    40a7:	00 15 00 03 00 56    	add    %dl,0x56000300
    40ad:	00 00                	add    %al,(%eax)
    40af:	00 15 00 02 00 02    	add    %dl,0x2000200
    40b5:	00 00                	add    %al,(%eax)
    40b7:	00 15 00 01 00 be    	add    %dl,0xbe000100
    40bd:	00 00                	add    %al,(%eax)
    40bf:	00 06                	add    %al,(%esi)
    40c1:	00 00                	add    %al,(%eax)
    40c3:	00 00                	add    %al,(%eax)
    40c5:	00 ff                	add    %bh,%bh
    40c7:	7f 06                	jg     40cf <_IO_stdin_used@@Base+0x20cb>
    40c9:	00 00                	add    %al,(%eax)
    40cb:	00 00                	add    %al,(%eax)
    40cd:	00 00                	add    %al,(%eax)
	...

Disassembly of section .bss:

000040d0 <.bss>:
    40d0:	00 00                	add    %al,(%eax)
	...

Disassembly of section .comment:

00000000 <.comment>:
   0:	47                   	inc    %edi
   1:	43                   	inc    %ebx
   2:	43                   	inc    %ebx
   3:	3a 20                	cmp    (%eax),%ah
   5:	28 55 62             	sub    %dl,0x62(%ebp)
   8:	75 6e                	jne    78 <__cxa_finalize@plt-0x1098>
   a:	74 75                	je     81 <__cxa_finalize@plt-0x108f>
   c:	20 39                	and    %bh,(%ecx)
   e:	2e 34 2e             	cs xor $0x2e,%al
  11:	30 2d 31 75 62 75    	xor    %ch,0x75627531
  17:	6e                   	outsb  %ds:(%esi),(%dx)
  18:	74 75                	je     8f <__cxa_finalize@plt-0x1081>
  1a:	31 7e 32             	xor    %edi,0x32(%esi)
  1d:	30 2e                	xor    %ch,(%esi)
  1f:	30 34 2e             	xor    %dh,(%esi,%ebp,1)
  22:	31 29                	xor    %ebp,(%ecx)
  24:	20 39                	and    %bh,(%ecx)
  26:	2e 34 2e             	cs xor $0x2e,%al
  29:	30 00                	xor    %al,(%eax)
