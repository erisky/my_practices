#include <stdio.h>
#include <sys/types.h>
#include <regex.h>


int main(int argc, char *argv[])
{
    int ret, status;
    regex_t re;


//printf("Hello regcomp\n");
    if (argc < 2 ) {
        printf("required re and string\n");
        return 0;
    }

    printf("pattern:%s input %s\n", argv[1], argv[2]);

    char *pattern = argv[1];
    if (regcomp(&re, pattern, REG_EXTENDED|REG_NOSUB) != 0) {
        printf("Fail to compile re");
    }

    status = regexec(&re, argv[2], 0, NULL, 0);
    regfree(&re);
    if (status == 0) 
        printf("Match!!\n");
    else 
        printf("Not Match!!\n");

    return 0;
}
