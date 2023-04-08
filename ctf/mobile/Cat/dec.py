#dd if=cat.ab bs=1 skip=24 | python -c "import zlib,sys;sys.stdout.write(zlib.decompress(sys.stdin.read()))" | tar -xvf -
#shared/0/Pictures/IMAG0004.jpg
#HTB{ThisBackupIsUnprotected}
