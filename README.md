<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/6/6c/Logo_Universit%C3%A9_Rennes_1_.svg/1280px-Logo_Universit%C3%A9_Rennes_1_.svg.png" height="100px"/>
# PROJECT ALG

## Read organizer

**UE ALG**

*Christelle LALANNE and Léa BEAULIEU - M2 IBI/BIS*

This project is dedicated to reorganize the reads from sequencing so that a generic compressor type gzip better compress these data.

## LAUCH

`python read_organizer.py -i myreads.fa -o myreads_organized.txt -f "minimizer" -min 7`


```
Positional arguments:
  -i                    Name of the input fasta file 
  -o                    Name of the output file
  
Optional arguments :
  -f                    Method/function used to generate the output file : "minimizer", "gc" or "alphabet".
                        By default, function "minimizer" is called.
  -min                  Length of smallest lexicographic word wanted for each read if method "minimizer" is used.
                        By default, min = 8.

```

## FILES

Script :
* **read_organizer.py** : python file containing our 3 functions

Additional files : 
* **rapport_dev.pdf** : PDF file that explains the structure of the program and specifies the operation of the key functions.
* **rapport_scientifique.pdf** : PDF file that explains the context, expose the techniques used to organize the reads, and give the results obtained.

## Credits 

* *Python 3.10.7 documentation* - https://docs.python.org/3/
