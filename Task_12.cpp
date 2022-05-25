#include <stdio.h>
#include <vector>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    const int colors = 100;
    std:: vector<std::vector<int>> matrix(1+n, std::vector<int>(1+colors, 0));
    for (int i = 0; i < m; i++){
        int v1,v2, color;
        scanf("%d %d %d", &v1, &v2, &color);
        matrix[v1][color] = v2;
        matrix[v2][color] = v1;
    }
    int steps;
    scanf("%d", &steps);
    int cur = 1;
    for(int i = 0; i<steps; i++){
        int color;
        scanf("%d", &color);
        cur = matrix[cur][color];
    }
    if (cur == 0){
        printf("INCORRECT");
    }
    else{
        printf("%d", cur);
    }

}