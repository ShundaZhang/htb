'''

    printf("[X] That entry is encrypted - please enter your WIDE decryption key: ");
    fgets(local_c8,0x10,stdin);
    mbstowcs(local_1c8,local_c8,0x10);
    iVar1 = wcscmp(local_1c8,L"sup3rs3cr3tw1d3");
    if (iVar1 == 0) {
      for (local_1d4 = 0;
          (local_1d4 < 0x80 && (*(char *)((long)&local_98 + (long)(int)local_1d4) != '\0'));
          local_1d4 = local_1d4 + 1) {
        *(byte *)((long)&local_98 + (long)(int)local_1d4) =
             *(byte *)((long)&local_98 + (long)(int)local_1d4) ^
             (char)(local_1d4 * 0x1b) + (char)((int)(local_1d4 * 0x1b) / 0xff);
      }
      puts((char *)&local_98);
    }

szhan21@szhan21-NUC:~/ctf/htb/ctf/re/WIDE$ ./wide db.ex
[*] Welcome user: kr4eq4L2$12xb, to the Widely Inflated Dimension Editor [*]
[*]    Serving your pocket dimension storage needs since 14,012.5 B      [*]
[*]                       Displaying Dimensions....                      [*]
[*]       Name       |              Code                |   Encrypted    [*]
[X] Primus           | people breathe variety practice  |                [*]
[X] Cheagaz          | scene control river importance   |                [*]
[X] Byenoovia        | fighting cast it parallel        |                [*]
[X] Cloteprea        | facing motor unusual heavy       |                [*]
[X] Maraqa           | stomach motion sale valuable     |                [*]
[X] Aidor            | feathers stream sides gate       |                [*]
[X] Flaggle Alpha    | admin secret power hidden        |       *        [*]
Which dimension would you like to examine? 6
[X] That entry is encrypted - please enter your WIDE decryption key: sup3rs3cr3tw1d3
HTB{som3_str1ng5_4r3_w1d3}

'''
