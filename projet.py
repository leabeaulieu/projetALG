import gzip

file_1 = "C:/Users/leabe/OneDrive/Bureau/ALG/Ecoli_100Kb/ecoli_100Kb_reads_5x.fasta"

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

def write_file(input_file, output_name):
    with open (output_name,"w") as out :
        dico_read = triplet(input_file)
        sorted_dict = {key: value for key, value in sorted(dico_read.items())}
        for i in sorted_dict.values():
            for j in i:
                out.write(j)
                out.write("\n")
