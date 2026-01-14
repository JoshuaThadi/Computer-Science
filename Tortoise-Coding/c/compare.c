#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char name[100];
    
    printf("Enter your name -> ");
    scanf("%s", name);

    printf("Hello, Boss %s!\n", name);
    return 0;
}

/*char* input(const char* prompt)
{
    printf("%s", prompt);
    char *buffer = malloc(100);
    fgets(buffer, 100, stdin);
    return buffer;
}

int main(void)
{
    char* name = input("Enter your name: ");
    printf("hello, %s", name);
    free(name);
    return 0;
}*/
