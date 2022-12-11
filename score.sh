for i in {1..15}
do
    python read_organizer.py -i myreads.fa -o myreads_organized_$i.txt -min $i
    gzip myreads_organized_$i.txt
    new=$(ls -l myreads_organized_$i.txt.gz | awk '{print $5}')
    echo $new >> score.txt
    
done

#à partir de 8  on n'améliore plus tellement le score, à partir d'une certaine valeur de min (9 pour 40x il me semble), le fichier redevient même plus gros
