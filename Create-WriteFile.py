# This python script will create and write to new_script.sh
# .sh will be a bash file
# Creates the file
fw = open('new_script.sh', 'w')
#1 st line needed for Bashscripts
fw.write('#!/bin/bash \n')
var1 = "I m a variable"
fw.write('echo 'var1';\n')
#last line of new_script.sh
fw.write('exit \n')
fw.close()
#End of program