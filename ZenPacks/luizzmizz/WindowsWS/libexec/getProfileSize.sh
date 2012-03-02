#!/bin/bash
COMPUTER=$1
USERNAME=$2
PASSWORD=$3
PROFILEPATH=$4

unitat=`echo $PROFILEPATH|awk -F ":" '{print $1}'`
path=`echo $PROFILEPATH|awk -F ":" '{print $2}'`
profileSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;cd \"$path\";du"|grep "Total number of bytes:"|awk -F ": " '{print $2}'`
desktopSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;cd \"$path\"/Desktop;du"|grep "Total number of bytes:"|awk -F ": " '{print $2}'`

echo -n "profileSize:$profileSize "
echo -n "desktopSize:$desktopSize "
