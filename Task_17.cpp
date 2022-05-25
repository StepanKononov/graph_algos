#include <stdio.h>
#include <vector>
#include <algorithm>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);
    const int INF = 1000*1000*1000;
    std::vector<std::vector<int>> graph (n, std::vector<int> (n, INF));
    for (int i = 0; i < n; ++i) {
        graph[i][i] =0;
    }

    for (int i = 0; i < m; ++i) {
        int to_1, to_2;
        scanf("%d %d", &to_1, &to_2);
        to_1--;
        to_2--;
        graph[to_1][to_2] = 0;
        graph[to_2][to_1] = std::min(graph[to_2][to_1], 1);
    }

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                graph[i][j] = std::min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    int max = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            max = std::max(max, graph[i][j]);
        }
    }
    printf("%d", max);
    return 0;
}