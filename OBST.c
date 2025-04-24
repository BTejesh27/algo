#include <stdio.h>
#include <limits.h>

int optimalBST(int freq[], int n) {
    int cost[n][n];

    for (int i = 0; i < n; i++)
        cost[i][i] = freq[i];

    for (int L = 2; L <= n; L++) {
        for (int i = 0; i <= n - L; i++) {
            int j = i + L - 1;
            cost[i][j] = INT_MAX;

            int total = 0;
            for (int k = i; k <= j; k++)
                total += freq[k];

            for (int r = i; r <= j; r++) {
                int c = ((r > i) ? cost[i][r - 1] : 0) +
                        ((r < j) ? cost[r + 1][j] : 0) + total;
                if (c < cost[i][j])
                    cost[i][j] = c;
            }
        }
    }

    return cost[0][n - 1];
}

int main() {
    int freq[] = {34, 8, 50};
    int n = sizeof(freq) / sizeof(freq[0]);
    printf("Minimum cost of OBST is: %d\n", optimalBST(freq, n));
    return 0;
}
