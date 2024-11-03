#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void leak() { 
    FILE *file = fopen("/proc/self/maps", "r"); 
    if (file == NULL) { 
        printf("Unable to open file %s\n", "/proc/self/maps"); 
        return; 
    } 
    char ch; 
    while ((ch = fgetc(file)) != EOF) { 
        putchar(ch); 
    } 
    fclose(file); 
} 

void verification() {
    char buffer[32];
    printf("Etes-vous sur ? : ");
    fflush(stdout);
    gets(buffer);
}

void question() {
    int key=0;
    char buffer[32];
    printf("Aimez-vous le ctf kaizen ? : ");
    fflush(stdout);
    gets(buffer);
    if (key == 0x13371337) {
        leak();
    }
}


int main(int argc, char* argv[]){
    question();
    verification();
    printf("Votre avis sera pris en compte o.o ...");
    return 0;
}
