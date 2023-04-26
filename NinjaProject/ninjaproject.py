#!/usr/bin/python3
#pip3 install python-nmap

import nmap
import os

sc = nmap.PortScanner()
OS = nm.command_line()

def main():
    n = input("1- Network scanner\n2- Vulnerabilies detection\n3- Exploit\nchoose a number \n\n\n> ")

    if n == '1':
        nmap()
    if n =='2':
        vuln()
    if n == '3':
        os.system('msfconsole')
    else :
        print("Please choose a number between 1 and 3")

def nmap():
    print("*********************************")
    print("**********NINJA PROJECT**********")
    print("*********************************")
    ip = input("Enter the IP address: ")
    sc.scan(ip , '1-1024')
    print(sc,scaninfo())
    print(sc[ip]['tcp'].keys())

    def vuln():
        print("*****************************************")
        print("**********NINJA VULNERABILITIES**********")
        print("*****************************************")
        ip = input("\nPlease enter the IP adress: ")
        print(os.system('nmap -sV --script=vulnscan.nse' +ip))

def OS():
    print("⠀⠀⠀⠀⠀⠀⠀⣠⠤⠒⠒⠀⠀⠒⠒⠠⠄⣀")
    print("⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠆⢀⠀⢤⣀⠀⠉⠲⣄")
    print("⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⣈⣠⡍⡢⣂⠈⢁⠠⠀⠀⠈⢆⠀⠀⠀")
    print("⠀⠀⠀⠀⣰⠁⠀⠀⠀⠈⡏⢠⣼⠿⣎⣎⣀⡄⣀⠀⢁⠈⡆⠀")
    print("⠀⠀⣀⡀⠇⠀⠀⠐⠁⠀⠱⣌⣛⡆⠙⠀⢟⡓⠛⠇⡀⠀⢸⠀⠀")
    print("⢰⣏⢣⢸⠀⠀⠀⢀⠀⠀⠀⠀⠁⡼⠷⠢⠴⣷⡄⠀⠀⠀⢸⠀⠀")
    print("⠈⡇⠉⠘⡄⠀⠀⠀⠀⠀⠀⠀⣠⣗⣕⣺⣛⣿⠇⠀⠀⠀⡇⠀⠀")
    print("⠀⠱⡀⠀⠈⠢⣄⠀⠀⠀⠀⠞⡃⣿⣿⣿⣿⣅⠸⠀⠀⡸⠀")
    print("⠀⠈⢄⠀⠀⡨⠓⠦⣀⠀⠑⠍⠒⠊⢩⣤⠞⠀⢀⡴⢱⣾⢭⡆")
    print("⠀⠀⠀⢠⠛⠇⠀⠀⠀⠈⠑⠒⠲⠤⠤⣤⠴⠒⠚⢉⠤⠊⢨⠇⠁")
    print("⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠤⠀⡠⠒⠁⠀⠀⠀⠀⠀")
    print("⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("*********OS Scan*********")
    ip = input("Enter the IP address: ")
    sc.scan(ip , '-O')






if __name__ == "__main__":
    main()







