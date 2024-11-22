import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 ip_shifter.py')
    run('mkdir /usr/share/ipshifter')
    run('cp ip_shifter.py /usr/share/ipshifter/ip_shifter.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/ipshifter/ip_shifter.py "$@"')
    with open('/usr/bin/ipshifter','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/ipshifter & chmod +x /usr/share/ipshifter/ip_shifter.py')
    print('''\n\ncongratulation IpShifter is installed successfully \nfrom now just type \x1b[6;30;42mipshifter\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/ipshifter ')
    run('rm /usr/bin/ipshifter ')
    print('[!] now IpShifter  has been removed successfully')
