#include <locale.h>
#include <wchar.h>
#include <uchar.h>
#include <stdio.h>

void wcharToChar16(wchar_t *param_1, char16_t *param_2, size_t param_3) {
    int iVar1;
    char16_t *puVar2;

    iVar1 = *param_1;
    puVar2 = param_2;
    
    if (1 < param_3) {
        do {
            param_2 = puVar2;
            
            if (iVar1 == 0) 
                break;
            
            param_1 = param_1 + 1;
            param_2 = puVar2 + 1;
            *puVar2 = (char16_t)iVar1;
            
            param_3 = param_3 - 1;
            iVar1 = *param_1;
            puVar2 = param_2;
        } while (1 < param_3);
    }

    *param_2 = 0;
    return;
}

int main() {
    setlocale(LC_ALL, "en_US.UTF-8");

    wchar_t awStack16008[100];
    char16_t SupportMsg[100];

    fgetws(awStack16008, 100, stdin);
    wcharToChar16(awStack16008, SupportMsg, 100);

    for (int i = 0; i < sizeof(awStack16008); ++i) {
        printf("0x%02X ", ((unsigned char *)awStack16008)[i]);
    }

    printf("\n====================================================\n");

    for (int i = 0; i < sizeof(SupportMsg); ++i) {
        printf("0x%02X ", ((unsigned char *)SupportMsg)[i]);
    }

    return 0;
}

