#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void question(){
    int key = 0x0;
    char buffer[32];
    printf("Aimez-vous le ctf kaizen ? : ");
    fflush(stdout);
    gets(buffer);
    if(key == 0xc0d3b005){
        printf("Ca doit vouloir dire oui : KZS{}\n");
        fflush(stdout);
    }
    else{
        printf("Votre avis sera pris en compte o.o ...");
        fflush(stdout);
    }
}

int main(int argc, char* argv[]){
    question();
    return 0;
}
