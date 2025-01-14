/*

sudo apt-get install libmcrypt-dev
gcc dec.c -o dec -lmcrypt -ggdb

$ ./dec > log.txt
$ grep HTB log.txt
Decrypted contents: HTB{t1m_l3arn_C}
Decrypted contents: HTB{t1m_l3arn_C}

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mcrypt.h>
#include <math.h>
#include <stdint.h>
#include <stdlib.h>

int encrypt(void* buffer, int buffer_len, char* IV, char* key, int key_len) {
  MCRYPT td = mcrypt_module_open("rijndael-128", NULL, "cbc", NULL);
  int blocksize = mcrypt_enc_get_block_size(td);

  if( buffer_len % blocksize != 0 ) { 
    return 1; 
  }

  mcrypt_generic_init(td, key, key_len, IV);
  mcrypt_generic(td, buffer, buffer_len);
  mcrypt_generic_deinit (td);
  mcrypt_module_close(td);
  
  return 0;
}

int decrypt(void* buffer, int buffer_len, char* IV, char* key, int key_len) {
  MCRYPT td = mcrypt_module_open("rijndael-128", NULL, "cbc", NULL);
  int blocksize = mcrypt_enc_get_block_size(td);

  if( buffer_len % blocksize != 0 ){ 
    return 1;
  }
  
  mcrypt_generic_init(td, key, key_len, IV);
  mdecrypt_generic(td, buffer, buffer_len);
  mcrypt_generic_deinit (td);
  mcrypt_module_close(td);
  
  return 0;
}

void* read_file(char* filename, int len) {
  FILE *fp = fopen(filename, "rb");
  void* data = malloc(len);
  fread(data, 1, len, fp);
  fclose(fp);
  return data;
}

int main(int argc, char* argv[]) // gcc src.c -o dec -lmcrypt -ggdb
{
  char* IV = "AAAAAAAAAAAAAAAA";
  //char *key = getenv("KEY");
  char *key = "VXISlqY>Ve6D<{#F";
  int keysize = 16;
  char* buffer;
  int buffer_len = 16;

  //void *ciphertext = read_file("flag.enc", buffer_len);
  FILE *fp = fopen("core", "rb");
  void *ciphertext = malloc(buffer_len);
  fseek(fp, 0L, SEEK_END);
  int size = ftell(fp);
  fseek(fp, 0L, SEEK_SET);
  for ( int i = 0; i < size-16; i++)
  {
    fread(ciphertext, 1, buffer_len, fp);
    decrypt(ciphertext, buffer_len, IV, key, keysize);
    printf("Decrypted contents: %s\n", ciphertext);
  }
  fclose(fp);

  return 0;
}

