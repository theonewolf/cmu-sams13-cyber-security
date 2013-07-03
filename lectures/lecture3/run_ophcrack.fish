#!/usr/bin/fish
#
# Make sure that the Windows NTFS partition has been mounted somewhere. If it
# comes from a virtual disk, you may want to mount it thusly:
#
#       sudo kpartx -av VIRTUAL_DISK_FILE
#       sudo mount /dev/mapper/loopNUM1pNUM2 /PATH/TO/MOUNT/FOLDER
#
# where you suitably replace the variables with the proper numbers/folders.
#
# Example run:
#
#   > ./run_ophcrack.sh 3 /tmp/cracking fast:small \
#     /tmp/windows/WINDOWS/system32/config
#
# 30 hashes have been found in the encrypted SAM found in \
# /tmp/windows/WINDOWS/system32/config.
# 
# Opened 4 table(s) from /tmp/cracking//fast.
# Opened 4 table(s) from /tmp/cracking//small.
# 0h  0m  0s; Found empty password for user Guest (NT hash #1)
# 0h  0m  0s; Found empty password for user Wolfgang Richter (NT hash #4)
# 0h  0m  0s; Found empty password for 2nd LM hash #6
# 0h  0m  0s; Found empty password for 2nd LM hash #8
# 0h  0m  0s; Found empty password for 2nd LM hash #9
# 0h  0m  0s; Found empty password for 2nd LM hash #10
# 0h  0m  1s; Found password 8 for 2nd LM hash #7
# 0h  0m  1s; Found password D for 2nd LM hash #5
# 0h  0m  1s; Found password D1 for 2nd LM hash #11
# 0h  0m 17s; Found password MONKEY for 1st LM hash #10in table XP free fast \
              #1 at column 4815.
# 0h  0m 17s; Found password monkey for user user5 (NT hash #10)
# 0h  0m 19s; Found password 123456 for 1st LM hash #6in table XP free small \
              #1 at column 9753.
# 0h  0m 19s; Found password 123456 for user user1 (NT hash #6)
# 0h  0m 19s; Found password TRATOR for 2nd LM hash #0in table XP free small \
              #2 at column 9812.
# 0h  0m 20s; Found password ABC123 for 1st LM hash #8in table XP free fast \
              #0 at column 4655.
# 0h  0m 20s; Found password abc123 for user user3 (NT hash #8)
# 0h  0m 20s; Found password ADMINIS for 1st LM hash #0in table XP free fast \
              #1 at column 4678.
# 0h  0m 22s; Found password administrator for user Administrator (NT hash #0)
# 0h  0m 22s; Found password QWERTY for 1st LM hash #9in table XP free small \
              #3 at column 9595.
# 0h  0m 22s; Found password qwerty for user user4 (NT hash #9)
# 0h  0m 23s; Found password PASSWOR for 1st LM hash #5in table XP free fast \
              #1 at column 4489.
# 0h  0m 23s; Found password password for user user0 (NT hash #5)
# 0h  0m 23s; Found password PASSWOR for 1st LM hash #11in table XP free fast \
              #1 at column 4489.
# 0h  0m 23s; Found password password1 for user user6 (NT hash #11)
# 0h  0m 25s; Found password 1234567 for 1st LM hash #7in table XP free small \
              #2 at column 9353.
# 0h  0m 25s; Found password 12345678 for user user2 (NT hash #7)
# 0h  3m 31s; search (100%); tables: total 8, done 4, using 4; pwd found 10/12.
# 
# Results:
# 
# username / hash                  LM password    NT password
# Administrator                    ADMINISTRATOR  administrator
# Guest                            *** empty ***  *** empty ***
# HelpAssistant                    .............. .......
# SUPPORT_388945a0                 *** empty ***  .......
# Wolfgang Richter                 *** empty ***  *** empty ***
# user0                            PASSWORD       password
# user1                            123456         123456
# user2                            12345678       12345678
# user3                            ABC123         abc123
# user4                            QWERTY         qwerty
# user5                            MONKEY         monkey
# user6                            PASSWORD1      password1
 

# script variables 
set USAGE '%s <number of threads> <tables folder> <tables> <Windows config folder>\n'
set NUM_THREADS           ''
set TABLES_DIR            ''
set TABLES                ''
set WINDOWS_CONFIG_FOLDER ''



# job: make sure there are enough arguments and set them into global variables
#      otherwise print an error
function parse_args
    if test (count $argv) -lt 4
        printf $USAGE $_
        exit 1
    end

    set NUM_THREADS $argv[1]
    set TABLES_DIR $argv[2]
    set TABLES $argv[3]
    set WINDOWS_CONFIG_FOLDER $argv[4]
end

# this is the "main" thread of execution
parse_args $argv
ophcrack -g -n $NUM_THREADS -d $TABLES_DIR -t $TABLES -w $WINDOWS_CONFIG_FOLDER
