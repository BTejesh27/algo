#include <stdio.h>
#include <string.h>
#define P 0xD8
#define W 8
#define T (1 << (W - 1))

unsigned char c(unsigned char *d, size_t l) {
    unsigned char r = 0;
    for (size_t i = 0; i < l; ++i) {
        r ^= d[i];
        for (unsigned char b = 8; b > 0; --b)
            r = (r & T) ? (r << 1) ^ P : r << 1;
    }
    return r;
}

int main() {
    unsigned char m[] = "Hello, tejesh!";
    printf("Message: %s\nCRC: 0x%02X\n", m, c(m, strlen((char *)m)));
    return 0;
}
