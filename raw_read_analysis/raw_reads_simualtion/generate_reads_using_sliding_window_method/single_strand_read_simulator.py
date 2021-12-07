import sys

whole_genome_seq = sys.argv[1] #input .fa wgs file
out_raw_read_file = sys.argv[2] #output .fa raw read file
read_len = 150 #length of each read is 150 base pairs

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


raw_reads = []
for i in range(0, len(concatinated_whole_genome_seq) + 15, 15):
    raw_reads.append(concatinated_whole_genome_seq[i:i+read_len])

    #reads_dict[i] = concatinated_whole_genome_seq[i:i+150]


position_of_the_last_read_of_len_150 = 3907831


#remove reads that are shorter than 150bp
trimmed_raw_reads = raw_reads[0:position_of_the_last_read_of_len_150 + 1] #TODO: check if the range is inclusive, no not inclusive so make sure we grab the last read by adding 1

#write reads to a file
f = open(out_raw_read_file, "a")
f.write(header_line + "\n") #the header line is taken from the ref wgs file
for i in  range(len(trimmed_raw_reads)):
    f.write(trimmed_raw_reads[i] + "\n")
f.close()
