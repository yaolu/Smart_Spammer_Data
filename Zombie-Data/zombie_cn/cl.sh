#!/bin/bash
for file in `ls *`
do
		cat $file|sed 's/<[^<*"ctt"]*>/\n/g'|grep \"ctt\"|sed 's/<[^<*]*>//g' >>c$file
done

