import gzip

file_1 = "C:/Users/leabe/OneDrive/Bureau/ALG/Ecoli_100Kb/ecoli_100Kb_reads_5x.fasta"

def remove_header(input_file, output_file):
    with open(input_file, "r") as ifh:
        with open(output_file, "w") as ofh:
            first_line = True
            for line in ifh:
                if ">" not in ifh:
                    ofh.write(line[:-1])
                else:
                    if first_line:
                        first_line = False
                    else:
                        ofh.write("\n")

def triplet(file):
    words = ["AAA", "AAC", "AAG", "AAT", "ACA", "AGA", "ATA", "ACC", "ACG", "ACT", "AGC", "AGG", "AGT", "ATC", "ATG", "ATT"]
    dict_triplet = dict()
    with open(file, "r") as file_reader:
        #count_total = 0
        for line in file_reader:
            #count_total += 1
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

dict_read = triplet(file_1)
count=0
for i in dict_read.values() :
    print(len(i))
print(count)


def triplet_moche(file):
    triplet_A = []
    triplet_C = []
    triplet_G = []
    triplet_T = []
    all_triplets = []
    with open(file, "r") as file_reader:
        for line in file_reader:
            line = line.strip("\n")
            if ">" not in line:
                if "AAA" in line :
                    triplet_A.append(line)
                elif "CCC" in line :
                    triplet_C.append(line)
                elif "GGG" in line :
                    triplet_G.append(line)
                elif "TTT" in line :
                    triplet_T.append(line)
                for i in triplet_A and triplet_C and triplet_G and triplet_T: 
                    if i not in all_triplets: 
                        all_triplets.append(i)         
    return all_triplets
                

            

remove_header(file_1, "C:/Users/leabe/OneDrive/Bureau/ALG/Ecoli_100Kb/clean_file.txt")
#print(triplet(file_1))