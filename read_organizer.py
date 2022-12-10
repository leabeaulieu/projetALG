import gzip
import argparse

file_1 = "/home/lea/Documents/ALG/Ecoli_100Kb/ecoli_100Kb_reads_40x.fasta"
'''
def get_options() -> argparse.Namespace:
    
    Give the options you want.

    Returns:
        Namespace: The parsed arguments.
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        required=True,
        action="store",
        help='The fasta file.'
    )

    parser.add_argument(
        "-o1",
        required=True,
        action="store",
        help='The output file for kmer.'
    )

    parser.add_argument(
            "-o2",
            required=True,
            action="store",
            help='The output file for gc_percent.'
        )
    
    parser.add_argument(
            "-o3",
            required=True,
            action="store",
            help='The output file for alphabetically.'
        )


    return parser.parse_args()

def remove_header(input_file, output_file):
    with open(input_file, "r") as ifh:
        with open(output_file, "w") as ofh:
            for line in ifh:
                if ">" not in line:
                    ofh.write(line)'''


def kmer(file,min):
    '''
    Finds the smallest lexicographic word of length "min" for each read.
    Args:
        file : a fasta file
        min : length of word
    Returns:
        dict_kmer : a dictionnary that contains smallest lexicographic words of length "min" as keys
                    and a list of reads associated as values.
    '''    
    dict_kmer = dict()
    with open(file, "r") as file_reader:
        for line in file_reader:
            line = line.strip("\n")
            smallest_word = ""
            if ">" not in line:
                smallest_word = line[:min]
                word = ""
                i = 1
                while i != len(line)-min+1:
                    word = line[i:i+min]
                    if word < smallest_word :
                        smallest_word = word
                    i+=1
                if smallest_word not in dict_kmer :
                    dict_kmer[smallest_word] = [line]
                else :
                    dict_kmer[smallest_word].append(line)
    return dict_kmer

def gc_percent(file):
    '''
    Take the GC% of reads in order to sort the reads.

    Args:
        file : a fasta file
    Returns:
        dict_gc : a dictionnary that contains GC% values in keys and reads in values.
    '''
    dict_gc = {}
    with open(file, "r") as fh:
        for line in fh:
            if ">" not in line:
                gc = 0
                for letter in line : 
                    if letter == "G" or letter == "C" :
                        gc += 1
                gc = gc / len(line[:-1])
                if gc not in dict_gc :
                    dict_gc[gc] = [line]
                else :
                     dict_gc[gc].append(line)
    return dict_gc


def sort_reads(file):
    '''
    Sorts the reads by lexicographical order.

    Args:
        file : a fasta file
    Returns:
        sorted_reads : a list that contains sorted reads in alphabetical order.
    '''
    reads = []
    with open(file, "r") as fh:
        for line in fh:
            if ">" not in line:
                reads.append(line)
    sorted_reads = sorted(reads)
    return sorted_reads


def write_file_kmer(input_file, output_name, min):
    '''
    Write the file that will contains sorted reads by kmers.

    Args:
        input_file : a fasta file
        output_file : a text file
    '''
    with open (output_name,"w") as out :
        dico_read = kmer(input_file, min)
        sorted_dict = {key: value for key, value in sorted(dico_read.items())}
        for i in sorted_dict.values():
            for j in i:
                out.write(j)
                out.write("\n")

def write_file_gc(input_file, output_name):
    '''
    Write the file that will contains sorted reads by GC%.

    Args:
        input_file : a fasta file
        output_file : a text file
    '''
    with open (output_name,"w") as out :
        dico_gc = gc_percent(input_file)
        sorted_dict = dict(sorted(dico_gc.items()))
        for i in sorted_dict.values():
            for j in i:
                out.write(j)

def write_file_alphabetically(input_file, output_name):
    '''
    Write the file that will contains sorted reads in alphabetical order.

    Args:
        input_file : a fasta file
        output_file : a text file
    '''
    with open (output_name,"w") as out :
        sorted_reads = sort_reads(input_file)
        for i in sorted_reads :
            out.write(i)
 
'''if __name__ == '__main__':
    options = get_options()
    write_file_tri(options.i, options.o1, min)
    write_file_gc(options.i, options.o2)
    write_file_alphabetically(options.i, options.o3)
'''
    
 
write_file_kmer(file_1, "/home/lea/Documents/ALG/Ecoli_100Kb/sort_file_tri.txt", 8)
#print(kmer(file_1))
write_file_gc(file_1, "/home/lea/Documents/ALG/Ecoli_100Kb/sort_file_gc.txt")
write_file_alphabetically(file_1, "/home/lea/Documents/ALG/Ecoli_100Kb/sort_file_al.txt")



