#include <stdio.h>
#include <stdbool.h>

int main(void){
    
    int size;
    do 
    {
        printf("Enter the size -> ");
        scanf("%d", &size);
    }
    while(size < 1);

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("0");
        }
        printf("\n");
    }
}
