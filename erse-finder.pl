# file: erse-finder.pl
# This script was used for a school project to find ERSE's in gene promoters using data form the Eukaryotic Promoter Database (EPD).   
# Originally written back in 2016 

while ($_ = readline) {
         print $& /CCAAT[ACGT]9CCAC[GA]/ || /CCAAT[ACGT]26CCACG/ || /ATTGG[ACGT]CCACG/; print "\t"; print $F[1]

}

