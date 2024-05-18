int main()
{
    setuid(0);
    system("/bin/cat /root/flag");
}