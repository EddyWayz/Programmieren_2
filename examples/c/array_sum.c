#include <stdio.h>

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i = 0; i < 5; ++i) {
        sum += arr[i];
    }
    printf("Summe: %d\n", sum);
    return 0;
}
