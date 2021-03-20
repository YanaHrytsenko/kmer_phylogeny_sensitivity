import sys

whole_genome_seq = sys.argv[1] #input .fa wgs file
out_raw_read_file = sys.argv[2] #output .fa raw read file
read_len = 150 #length of each read is 150 base pairs

#my whole genome seq is split by lines as for a standart .fa file, concatinate lines first
concatinated_whole_genome_seq = ""
header_line = ""
with open (whole_genome_seq) as f:
    line = f.readline().strip("\n")
    header_line = line #contains .fa format first line
    counter = 1
    #concatinated_whole_genome_seq = concatinated_whole_genome_seq + line
    while line:
        line = f.readline().strip("\n")
        counter += 1
        concatinated_whole_genome_seq = concatinated_whole_genome_seq + line

'''
#remove N's
clean_whole_genome_seq = ""
for i in range(len(concatinated_whole_genome_seq)):
    if(concatinated_whole_genome_seq[i] != 'N'):
        clean_whole_genome_seq = clean_whole_genome_seq + concatinated_whole_genome_seq[i]
    else:
        continue
'''


#generate raw reads, store them sequentially in a list

#reads_dict = {} #optional: store reads by position in the sequence in a dictionary

raw_reads = []
for i in range(0, len(concatinated_whole_genome_seq) + 15, 15): #why 15?
    raw_reads.append(concatinated_whole_genome_seq[i:i+read_len])

    #reads_dict[i] = concatinated_whole_genome_seq[i:i+150]

'''
#print out the dictionary of reads by sorted position
for key in sorted(reads_dict.keys()):
    print(key,reads_dict[key]) #to write it to a file just add >> file_to_store.txt
'''

'''
#check if there are reads that are less than 150bp long
for i in range(len(raw_reads)):
    if(len(raw_reads[i]) != 150):
        print(i, raw_reads[i])
'''
position_of_the_last_read_of_len_150 = 3907831 #checked it manually, change to getting this valu computationaly


#remove reads that are shorter than 150bp
trimmed_raw_reads = raw_reads[0:position_of_the_last_read_of_len_150 + 1] #TODO: check if the range is inclusive, no not inclusive so make sure we grab the last read by adding 1

#write reads to a file
f = open(out_raw_read_file, "a")
f.write(header_line + "\n") #the header line is taken from the ref wgs file
for i in  range(len(trimmed_raw_reads)):
    f.write(trimmed_raw_reads[i] + "\n")
f.close()
