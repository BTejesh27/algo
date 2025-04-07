#include <stdio.h>
#include <string.h>

void characterStuffing(const char* input, char* output) {
    const char FLAG = 'F';
    const char ESC = 'E';
    int j = 0;
    output[j++] = FLAG;
    for (int i = 0; input[i] != '\0'; i++) {
        if (input[i] == FLAG || input[i] == ESC) {
            output[j++] = ESC;
        }
        output[j++] = input[i];
    }
    output[j++] = FLAG;
    output[j] = '\0';
}

void bitStuffing(const char* input, char* output) {
    int count = 0, j = 0;
    for (int i = 0; input[i] != '\0'; i++) {
        output[j++] = input[i];
        if (input[i] == '1') {
            count++;
            if (count == 5) {
                output[j++] = '0';
                count = 0;
            }
        } else {
            count = 0;
        }
    }
    output[j] = '\0';
}

int main() {
    char input[100], stuffed[200];
    printf("Enter data for Character Stuffing: ");
    scanf("%s", input);
    characterStuffing(input, stuffed);
    printf("Character Stuffed Output: %s\n", stuffed);
    printf("\nEnter binary data for Bit Stuffing: ");
    scanf("%s", input);
    bitStuffing(input, stuffed);
    printf("Bit Stuffed Output: %s\n", stuffed);
    return 0;
}
