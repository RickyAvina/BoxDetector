#!/bin/bash

#echo "Positional Parameters"
#echo '$1 = ' $1 # IP Address

# $1 = IP Address
# $2 = optional directory

if [ "$2" != "" ]; then
  scp -i ~/Documents/keys.pem $2/images/* ubuntu@$2:/home/ubuntu/images
  scp -i ~/Documents/keys.pem $2/labels/* ubuntu@$2:/home/ubuntu/labels
  scp -i ~/Documents/keys.pem $2/testImages/* ubuntu@$2:/home/ubuntu/testImages
  scp -i ~/Documents/keys.pem $2/testLabels/* ubuntu@$2:/home/ubuntu/testLabels
else
  scp -i ~/Documents/keys.pem /Volumes/BOXDATA/cubes/images/* ubuntu@$1:/home/ubuntu/images
  scp -i ~/Documents/keys.pem /Volumes/BOXDATA/cubes/labels/* ubuntu@$1:/home/ubuntu/labels
  scp -i ~/Documents/keys.pem /Volumes/BOXDATA/cubes/testImages/* ubuntu@$1:/home/ubuntu/testImages
  scp -i ~/Documents/keys.pem /Volumes/BOXDATA/cubes/testLabels/* ubuntu@$1:/home/ubuntu/testLabels
fi
