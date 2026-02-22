Timer Programming in C      #include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
    time_t next = time(NULL) + 5;

    while (1) {
        if (time(NULL) >= next) {
            printf("Timer executed\n");
            next += 5;   
        }
        usleep(100000);  
    }
    return 0;
}