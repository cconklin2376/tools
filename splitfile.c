// Barrowed code from SO
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char fn[250], nfn[250];
    long int size, n, k;
    int i, ch;
    FILE *f, *ft; //file and temp file

    printf("enter the file you want to split with full path : ");
    scanf("%s", fn);
    printf("enter the number of parts you want to split the file : ");
    scanf("%ld", &n);

    f=fopen(fn, "rb");
    if (f==NULL)
    {
        printf("couldn't open file");
        exit(0);
    }

    fseek(f, 0, 2);
    size = ftell(f);
    printf("the size of the file in bytes is : %ld\n", size);

    i = 1;
    k = size/n;
    rewind(f);
    sprintf(nfn, "%s.%d", fn, i);
    ft = fopen(nfn, "wb");
    while(1)
    {
        ch = fgetc(f);
        if (ch==EOF)
            break;
        fputc(ch, ft);
        if (ftell(f)==(i*k))
        {
            i = i+1;
            fclose(ft);
            sprintf(nfn, "%s.%d", fn, i);
            ft=fopen(nfn, "wb");
        }
    }
}
