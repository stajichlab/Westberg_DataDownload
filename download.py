#!/usr/bin/env python3

import csv, re
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "jason.stajich@ucr.edu"
itsfh = open("Westberg_ITS.fasta","w")
lsufh = open("Westberg_LSU.fasta","w")
mrssufh = open("Westberg_mrSSU.fasta","w")
tubfh = open("Westberg_bTub.fasta","w")

p = re.compile("\s+")
with open("Westberg_suppl_table.csv","r") as fh:
        reader = csv.reader(fh, delimiter=',')
        for line in reader:
                if(line[0] != "Specieslabcode"):
                        print(line[0])
                        id = p.sub("_",line[0])
                        if len(line[1]) > 0: #ITS
                                handle = Entrez.esearch(db="nuccore", 
                                                        term=line[1]+"[ACC]")
                                record = Entrez.read(handle)
                                gi_list = record["IdList"]
                                gi_str = ",".join(gi_list)
                                handle = Entrez.efetch(db="nuccore", 
                                                       id=gi_str, rettype="fasta", 
                                                       retmode="text")
                                records = SeqIO.parse(handle, "fasta")
                                for record in records: # should only be one
                                        record.id = id
                                        SeqIO.write(record,itsfh,"fasta")

                        if len(line[2]) > 0: # LSU
                                handle = Entrez.esearch(db="nuccore", 
                                                        term=line[2]+"[ACC]")
                                record = Entrez.read(handle)
                                gi_list = record["IdList"]
                                gi_str = ",".join(gi_list)
                                handle = Entrez.efetch(db="nuccore", 
                                                       id=gi_str, rettype="fasta", 
                                                       retmode="text")
                                records = SeqIO.parse(handle, "fasta")
                                for record in records: # should only be one
                                        record.id = id
                                        SeqIO.write(record,lsufh,"fasta")

                        if len(line[3]) > 0: # mrSSU
                                handle = Entrez.esearch(db="nuccore", 
                                                        term=line[3]+"[ACC]")
                                record = Entrez.read(handle)
                                gi_list = record["IdList"]
                                gi_str = ",".join(gi_list)
                                handle = Entrez.efetch(db="nuccore", 
                                                       id=gi_str, rettype="fasta", 
                                                       retmode="text")
                                records = SeqIO.parse(handle, "fasta")
                                for record in records: # should only be one
                                        record.id = id
                                        SeqIO.write(record,mrssufh,"fasta")


                        if len(line[4]) > 0: # Tub
                                handle = Entrez.esearch(db="nuccore", 
                                                        term=line[4]+"[ACC]")
                                record = Entrez.read(handle)
                                gi_list = record["IdList"]
                                gi_str = ",".join(gi_list)
                                handle = Entrez.efetch(db="nuccore", 
                                                       id=gi_str, 
                                                       rettype="fasta", 
                                                       retmode="text")
                                records = SeqIO.parse(handle, "fasta")
                                for record in records: # should only be one
                                        record.id = id
                                        SeqIO.write(record,tubfh,"fasta")


