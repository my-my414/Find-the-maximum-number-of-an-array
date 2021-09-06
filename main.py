#include<stdio.h>
int main()
{
    int myarray[5]={34,56,67,23,45};
    int i,max=0;
    for(i=0;i<5;i++)
    {
        if(myarray[i]>max)
        {
            max=myarray[i];
        }
    }
    printf("%d",&max);
}
