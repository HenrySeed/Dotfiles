#!/usr/bin/python

import os
import platform
import getpass
from collections import namedtuple


class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    norm = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def apple():
    '''returns list of lines making up ascii apple art'''
    line_1 = (bcolors.green + '                 -/+:.            ' + bcolors.norm)
    line_2 = (bcolors.green + '                :++++.            ' + bcolors.norm)
    line_3 = (bcolors.green + '               /+++/.             ' + bcolors.norm)
    line_4 = (bcolors.green + '       .:-::- .+/:-``.::-         ' + bcolors.norm)
    line_5 = (bcolors.green + '    .:/++++++/::::/++++++/:`      ' + bcolors.norm)
    line_6 = (bcolors.yellow + '  .:///////////////////////:`     ' + bcolors.norm)
    line_7 = (bcolors.yellow + '  ////////////////////////`       ' + bcolors.norm)
    line_8 = (bcolors.red + ' -+++++++++++++++++++++++`        ' + bcolors.norm)
    line_9 = (bcolors.red + ' /++++++++++++++++++++++/         ' + bcolors.norm)
    line_10 = (bcolors.red + ' /sssssssssssssssssssssss.        ' + bcolors.norm)
    line_11 = (bcolors.red + ' :ssssssssssssssssssssssss-       ' + bcolors.norm)
    line_12 = (bcolors.purple + '  osssssssssssssssssssssssso/`    ' + bcolors.norm)
    line_13 = (bcolors.purple + '  `syyyyyyyyyyyyyyyyyyyyyyyy+`    ' + bcolors.norm)
    line_14 = (bcolors.blue + '   `ossssssssssssssssssssss/      ' + bcolors.norm)
    line_15 = (bcolors.blue + '     :ooooooooooooooooooo+.       ' + bcolors.norm)
    line_16 = (bcolors.blue + '      `:+oo+/:-..-:/+o+/-         ' + bcolors.norm)
    line_17 = ('                                  ')

    lines = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_9,\
            line_9, line_10, line_11, line_12, line_13, line_14, line_15, \
            line_16, line_17, '']
    return lines


def disk_usage(url):
    """
    Returns a named tuple with attributes 'total'and 'used', which are the
    amount of total and used space, in bytes.
    """

    st = os.statvfs('/Volumes/' + url)
    total = '%.2f' % ((st.f_blocks * st.f_frsize)/1000000000)
    used = '%.2f' % (((st.f_blocks - st.f_bfree) * st.f_frsize)/1000000000)
    return (total, used)


def hdd_chart(url):
    size = '%.0f' % float((disk_usage(url)[0]))
    full = (disk_usage(url)[1])



    full = ("%.0f" % float(full))
    portion = float(full)/float(size)
    filled = int("%.0f" % (portion * 30))
    hashes = filled * (bcolors.blue + '#' + bcolors.norm)
    meter = ' [' + str(full) + ' / ' + str(size) + ']'
    lines = (30 - filled) * (bcolors.norm + '-' + bcolors.norm)
    line = "  [" + (hashes) + (lines) + ']' + meter

    return line


def info():
    '''returns list of header nd info.'''
    my_os = platform.system()
    plat = platform.platform()
    if my_os == 'Darwin':
        user = bcolors.blue + 'User: ' + bcolors.norm + getpass.getuser()

        system_os = 'Mac OS X'

        ops = bcolors.blue + 'OS: ' + bcolors.norm + system_os + ' ' + \
            platform.mac_ver()[0]

        kernal = bcolors.blue + 'Kernal: ' + bcolors.norm + plat[14:20] + \
            ' ' + plat[0:6] + ' ' + plat[7:13]

        cpu = '2.7 GHz Intel Core i7'
        cpu_info = bcolors.blue + 'Cpu: ' + bcolors.norm + cpu

        charts = []

        volumes = os.listdir('/Volumes')
        volumes.remove("MobileBackups")

        for volume in volumes:
            charts.append(hdd_chart(volume))


        # full = (disk_usage()[1])
        # size = '%.0f' % float((disk_usage()[0]))
        # free = '%.0f' % (float(size) - float(full))

        hdd = bcolors.blue + 'HDD: ' + bcolors.norm #+ str(free) + \
            #' GB free of ' + size + ' GB'

        info_lines = [' ', ' ', user, ops, kernal, cpu_info, hdd] + charts
        info = info_lines + ([''] * (20 - len(info_lines)))
        return info


def screenfetch():
    ''''prints os logo and computer info'''
    os.system("clear")
    counter = 0
    logo = apple()
    sys_info = info()
    for line in logo:
        print('{0}{1}'.format(line, sys_info[counter]))
        counter += 1

screenfetch()
