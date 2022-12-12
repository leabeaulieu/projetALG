import time
from timer_code import Timer  	# should be in the same directory 
from progression_bar import update_progress # should be in the same directory 

if __name__ == "__main__":
    n = 60
    with Timer() as total_time:  # time all instructions in the ’with’ statements
        for i in range(n):
            update_progress(i/float(60))
            time.sleep(0.1) 
            import argparse

            def get_options() -> argparse.Namespace:
                '''
                Give the options you want.

                Returns:
                    Namespace: The parsed arguments.
                '''
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
                    help='The output file.'
                )

                parser.add_argument(
                    "-f",
                    required=False,
                    action="store",
                    default = "minimizer",
                    help='The function called.'
                )
                
                parser.add_argument(
                    "-min",
                    required=False,
                    default = 8,
                    type = int,
                    action="store",
                    help='The length of the word for the minimizer function.'
                )

                return parser.parse_args()

            def minimizer(file,min):
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


            def write_file_minimizer(input_file, output_name, min):
                '''
                Write the file that will contains sorted reads by kmers.

                Args:
                    input_file : a fasta file
                    output_file : a text file
                '''
                with open (output_name,"w") as out :
                    dict_read = minimizer(input_file, min)
                    sorted_dict = {key: value for key, value in sorted(dict_read.items())}
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
                    dict_gc = gc_percent(input_file)
                    sorted_dict = dict(sorted(dict_gc.items()))
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
            
            if __name__ == '__main__':
                options = get_options()
                if options.f == "minimizer" :
                    write_file_minimizer(options.i, options.o, options.min)
                elif options.f == "gc" :
                    write_file_gc(options.i, options.o)
                elif options.f == "alphabet" :
                    write_file_alphabetically(options.i, options.o)

        update_progress(1)
    total_time.print("Time spent = {} seconds")