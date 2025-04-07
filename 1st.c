#include <stdio.h>
#include <string.h>
#define POLYNOMIAL 0xD8
#define WIDTH 8
#define TOPBIT (1 << (WIDTH - 1))

unsigned char crc8(unsigned char *data, size_t length) {
    unsigned char remainder = 0;
    for (size_t byte = 0; byte < length; ++byte) {
        remainder ^= data[byte];
        for (unsigned char bit = 8; bit > 0; --bit) {
            if (remainder & TOPBIT) {
                remainder = (remainder << 1) ^ POLYNOMIAL;
            } else {
                remainder = (remainder << 1);
            }
        }
    }
    return remainder;
}

int main() {
    unsigned char message[] = "Hello, CRC!";
    size_t messageLength = strlen((char *)message);
    unsigned char crc = crc8(message, messageLength);
    printf("Message: %s\n", message);
    printf("CRC: 0x%02X\n", crc);
    return 0;
}
