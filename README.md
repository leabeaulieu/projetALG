<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/6/6c/Logo_Universit%C3%A9_Rennes_1_.svg/1280px-Logo_Universit%C3%A9_Rennes_1_.svg.png" height="100px"/>
# PROJECT ALG

## Read organizer

**UE ALG**

*Christelle LALANNE and Léa BEAULIEU - M2 IBI/BIS*

This project is dedicated to reorganize the reads from sequencing so that a generic compressor type gzip better compress these data.

## LAUCH

`python read_organizer.py -i myreads.fa -o1 myreads_organized_tri.txt -o1 myreads_organized_gc.txt -o3 myreads_organized_al.txt`


```
positional arguments:
  -i                    name of the input fasta file 
  -o1                   name of the first output file
  -o2                   name of the second output file
  -o3                   name of the third output file

```

## FILES

Script :
* **read_organizer.py** : python file containing our 3 functions

Additional files : 
* **rapport_dev.pdf** : PDF file that explains the structure of the program and specifies the operation of the key functions.
* **rapport_scientifique.pdf** : PDF file that explains the context, expose the techniques used to organize the reads, and give the results obtained.

## Credits 

* *Python 3.10.7 documentation* - https://docs.python.org/3/
