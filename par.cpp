#include<iostream>
using namespace std;
int main(int argc, char** argv)
{
	std::string args = argv[1];
	std::string command = "python zipify.py ";
	if(argv[1] == std::string("--unpack"))
	{
		command = command + "--unpack-par ";
		command = command + std::string(argv[2]) +" ";
		command = command + std::string(argv[3]);
	}else if(argv[1] == "--pack")
	{
		command = command + "--pack-dir ";
		command = command + std::string(argv[2])+ " ";
		command = command + std::string(argv[3]);
	}
}