#! /bin/bash
#vars#

#############
echo "Welcome to SavoareBio shop!"
sleep 1
echo "What is your name ?"
sleep 1
read name
sleep 1
echo "Nice to meet you $name and welcome to our shop!"
sleep 1
echo "Do you like to check our menu  [no or yes]?"
sleep 1
read param
if [[ $param != "yes" ]] ;
    then
    echo "See you next time $name !"
    exit 1
fi
sleep 1
echo "Here is our menu $name "
sleep 1
menu=('1.coffee' '2.fruits' '3.juce' )
echo ${menu[@]}
sleep 1
echo "Witch of our products will be $name ?"
sleep 1
read chose
sleep 1
vari=0
case "$chose" in

    "coffee")
            vari=7
            echo "your chose is: $chose and it will cost you $ 7";;
    "fruits")
            vari=4
            echo "your chose is: $chose and it will cost you $ 4";;
    "juce")
            vari=3
            echo "your chose is: $chose and it will cost you $ 3";;
    *)
            vari=0
            echo " We don't have this product try again!"
            exit 1;;
esac
sleep 1
echo "Here is your recived !"
sleep 1
var=$(date)
echo ".......Product $chose........."
echo "....... $var"
echo "....... Price $ $vari........"
echo "....... Name: $name"
echo "......Enjoy your coffee ......"
echo "....Thank's for visiting!....."
sleep 1
echo " Do you want to do some other stuff inside our coffeshop [no or yes]?"
sleep 1
read param
if [[ $param != "yes" ]] ;
    then
    echo "See you next time $name !"
    exit 1
fi
sleep 1
echo "What do you want to do next ? we have some options , just check them:"
options=('1.hacking' '2.check-the-news' '3.check-wather' '4.coding' '5.litsten-to-music')
sleep 1
echo ${options[@]}
sleep 1

