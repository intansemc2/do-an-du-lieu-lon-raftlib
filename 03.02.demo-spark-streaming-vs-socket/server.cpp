#include <stdio.h>      // standard input and output library
#include <stdlib.h>     // this includes functions regarding memory allocation
#include <string.h>     // contains string functions
#include <errno.h>      //It defines macros for reporting and retrieving error conditions through error codes
#include <time.h>       //contains various functions for manipulating date and time
#include <unistd.h>     //contains various constants
#include <sys/types.h>  //contains a number of basic derived types that should be used whenever appropriate
#include <arpa/inet.h>  // defines in_addr structure
#include <sys/socket.h> // for socket creation
#include <netinet/in.h> //contains constants and structures needed for internet domain addresses

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string readInputFile(string path)
{
    string line;
    ifstream myfile(path);
    if (myfile.is_open())
    {
    	string newLine = "";
        while (getline(myfile, newLine))
        {
            line += newLine + "\n";
        }
        myfile.close();
    }
    return line;
}

int main()
{
    int clintListn = 0, clintConnt = 0;
    struct sockaddr_in ipOfServer;

    clintListn = socket(AF_INET, SOCK_STREAM, 0); // creating socket

    memset(&ipOfServer, '0', sizeof(ipOfServer));

    ipOfServer.sin_family = AF_INET;
    ipOfServer.sin_addr.s_addr = htonl(INADDR_ANY);
    ipOfServer.sin_port = htons(9999); // this is the port number of running server

    bind(clintListn, (struct sockaddr *)&ipOfServer, sizeof(ipOfServer));
    listen(clintListn, 20);

    string inputFile = readInputFile("input.txt");
    cout << ">> Write: " << inputFile << " ... " << endl;

    clintConnt = accept(clintListn, (struct sockaddr *)NULL, NULL);
    while (1)
    {
        string portInput = inputFile;

        /////////////////////////////////////////////////////////////////////
        //Deal with the socket

        //Write data to the socket
        portInput = portInput + "\r\n"; // Add "\r\n" for spark know
        write(clintConnt, portInput.c_str(), strlen(portInput.c_str()));
        //Wait a bit
        sleep(1);

        /////////////////////////////////////////////////////////////////////
    }

    return 0;
}