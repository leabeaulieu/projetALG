import argparse

file_1 = "C:/Users/leabe/OneDrive/Bureau/ALG/Ecoli_100Kb/ecoli_100Kb_reads_5x.fasta"

def get_options() -> argparse.Namespace:
    """Give the options you want.


    Returns:
        Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        required=True,
        action="store",
        help='The fasta file.'
    )

    parser.add_argument(
        "-o",
        required=True,
        action="store",
        help='The output file .'
    )
    
    parser.add_argument(
        "-o2",
        required=True,
        action="store",
        help='The output file for gc_percent.'
    )

    return parser.parse_args()


def triplet(file):
    words = ["AAA", "AAC", "AAG", "AAT", "ACA", "AGA", "ATA", "ACC", "ACG", "ACT", "AGC", "AGG", "AGT", "ATC", "ATG", "ATT"]
    dict_triplet = dict()
    with open(file, "r") as file_reader:
        for line in file_reader:
            line = line.strip("\n")
            if ">" not in line:
                i=0
                while i != len(words)-1:
                    if words[i] in line :
                        if words[i] not in dict_triplet :
                            dict_triplet[words[i]] = [line]
                        else :
                            dict_triplet[words[i]].append(line)
                        i=len(words)-1
                    else:
                        i+=1
    return dict_triplet

def gc_percent(file):
    dict_gc = {}
    with open(file, "r") as fh:
        for line in fh:
            if ">" not in line:
                gc = 0
                for letter in line : 
                    if letter == "G" or letter == "C" :
                        gc += 1
                gc = gc / len(line[:-1])
                if str(gc) not in dict_gc :
                    dict_gc[str(gc)] = [line]
                else :
                     dict_gc[str(gc)].append(line)
    return dict_gc


def write_file(input_file, output_name):
    with open (output_name,"w") as out :
        dico_read = triplet(input_file)
        sorted_dict = {key: value for key, value in sorted(dico_read.items())}
        for i in sorted_dict.values():
            for j in i:
                out.write(j)
                out.write("\n")
                
def write_file_gc(input_file, output_name):
    with open (output_name,"w") as out :
        dico_gc = gc_percent(input_file)
        sorted_dict = dict(sorted(dico_gc.items()))
        for i in sorted_dict.values():
            for j in i:
                out.write(j)
        
if __name__ == '__main__':
    options = get_options()
    write_file(options.i, options.o1)
    write_file_gc(options.i, options.o2)
