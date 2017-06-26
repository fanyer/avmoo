# url=https://jp.netcdn.space/digital/video/118lxvs00030/118lxvs00030-10jp.jpg

# wget -c 
# wget -i temp

for (( j = 1; j < 9; j++ )); do
        
    code="118lxvs0000$j"
    # echo $code

    # cd $code && pwd && cd ..
    # cd $code && touch temp && ls && cd ..

    cd $code && wget -c -i temp && cd ..

    # cd $code
    # for ((i=1;i<=28;i++))
    # {
    #  echo "https://jp.netcdn.space/digital/video/${code}/${code}jp-$i.jpg">>temp  
    # }
    # cd ..
done


