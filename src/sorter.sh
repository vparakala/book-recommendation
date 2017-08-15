for FILE in $(cat tfidfs)
    do
        echo $FILE
        sort -r -k 2 -n -o $FILE $FILE
    done
