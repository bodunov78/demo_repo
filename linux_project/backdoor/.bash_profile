# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs
#!/bin/bash
ter=`who am i| tr -s ' ' ':'| cut -d ':' -f2`
#echo $ter

if [ "$ter" == "tty13" ]
then 
#echo "ok"
vlock
fi
