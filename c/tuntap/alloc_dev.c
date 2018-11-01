#include <stdio.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <ifaddrs.h>
#include <linux/if.h>
#include <linux/if_tun.h>

int tun_alloc(char *dev)
{
      struct ifreq ifr;
      int fd, err;

      if( (fd = open("/dev/net/tun", O_RDWR)) < 0 ) {
            printf("error!!\n");
         return -1;
      }
      memset(&ifr, 0, sizeof(ifr));

      /* Flags: IFF_TUN   - TUN device (no Ethernet headers) 
       *        IFF_TAP   - TAP device  
       *
       *        IFF_NO_PI - Do not provide packet information  
       */ 
      ifr.ifr_flags = IFF_TAP | IFF_NO_PI ;
      if( *dev )
         strncpy(ifr.ifr_name, dev, IFNAMSIZ);

      if( (err = ioctl(fd, TUNSETIFF, (void *) &ifr)) < 0 ){
         close(fd);
         printf("erro = %d\n", err);
         return err;
      }
      printf("ifname=%s", ifr.ifr_name);
      strcpy(dev, ifr.ifr_name);
      printf("fd = %d\n",fd);
      return fd;
}              



int main(void)
{
    int ret = 0; 
    char buf[] = "tap0";
    int cg = 0;
    int rlen=0;
    char sendbuf[1000];
    char recvbuf[1000];
    
    ret = tun_alloc(buf);

    printf("Get dev=%s", buf);

    while ((cg = getc(stdin)) != 'q') {
        printf("cg = %d\n", cg);
        sprintf(sendbuf,"111111111111111111111111111111111111122222222222222222222");
        write(ret, sendbuf, 32);
        printf("sent\n");
        rlen = read(ret, recvbuf, 1000);
        printf("recv:%d bytes\n", rlen);

    }



    return ret;
}
