#!/bin/bash

FILES="1000M[1-4]/R*"

for i in $FILES
do
    printf '%s ' $i |tr / ' ' >> result.csv

    start=`date +%s%N`
    mafft --retree 2 --maxiterate 0 $i/rose.unaln.fasta > $i/mafft_fftns2.aln.fasta
    end=`date +%s%N`
    java -jar FastSP.jar -r $i/rose.aln.true.fasta -e $i/mafft_fftns2.aln.fasta -o $i/mafft_fftns2.result
    sed -n '3p;4p;6p' < $i/mafft_fftns2.result | awk  '{printf "%.4f ", $2}' >> result.csv
    ./FastTree -nt -gtr $i/mafft_fftns2.aln.fasta > $i/mafft_fftns2_fasttree.nwk
    python compare.py $i/rose.tt $i/mafft_fftns2_fasttree.nwk >> result.csv
    printf '%s ' $(bc <<< "scale=2;($end - $start)/1000000000" ) >> result.csv

    start=`date +%s%N`
    ./muscle3.8.31_i86linux64 -maxiters 2 -in $i/rose.unaln.fasta -out $i/muscle_2.aln.fasta
    end=`date +%s%N`
    java -jar FastSP.jar -r $i/rose.aln.true.fasta -e $i/muscle_2.aln.fasta -o $i/muscle_2.result
    sed -n '3p;4p;6p' < $i/muscle_2.result | awk  '{printf "%.4f ", $2}' >> result.csv
    ./FastTree -nt -gtr $i/muscle_2.aln.fasta > $i/muscle_2_fasttree.nwk
    python compare.py $i/rose.tt $i/muscle_2_fasttree.nwk >> result.csv
    printf '%s ' $(bc <<< "scale=2;($end - $start)/1000000000" ) >> result.csv

    ./FastTree -nt -gtr $i/rose.aln.true.fasta > $i/true_fasttree.nwk
    python compare.py $i/rose.tt $i/true_fasttree.nwk >> result.csv
    printf '\n' >> result.csv

    echo ----------------------$i--------------------------------

done

printf '16S.M R0 ' >> result.csv

start=`date +%s%N`
mafft --retree 2 --maxiterate 0 16S.M/R0/cleaned.unaligned.fasta > 16S.M/R0/mafft_fftns2.aligned.fasta
end=`date +%s%N`
java -jar FastSP.jar -r 16S.M/R0/cleaned.alignment.fasta -e 16S.M/R0/mafft_fftns2.aligned.fasta -o 16S.M/R0/mafft_fftns2.result
sed -n '3p;4p;6p' < 16S.M/R0/mafft_fftns2.result | awk  '{printf "%.4f ", $2}' >> result.csv
./FastTree -nt -gtr 16S.M/R0/mafft_fftns2.aligned.fasta > 16S.M/R0/mafft_fftns2_fasttree.nwk
python compare.py 16S.M/R0/16S.M.reference.nwk 16S.M/R0/mafft_fftns2_fasttree.nwk >> result.csv
printf '%s ' $(bc <<< "scale=2;($end - $start)/1000000000" ) >> result.csv

start=`date +%s%N`
./muscle3.8.31_i86linux64 -maxiters 2 -in 16S.M/R0/cleaned.unaligned.fasta -out 16S.M/R0/muscle_2.aligned.fasta
end=`date +%s%N`
java -jar FastSP.jar -r 16S.M/R0/cleaned.alignment.fasta -e 16S.M/R0/muscle_2.aligned.fasta -o 16S.M/R0/muscle_2.result
sed -n '3p;4p;6p' < 16S.M/R0/muscle_2.result | awk  '{printf "%.4f ", $2}' >> result.csv
./FastTree -nt -gtr 16S.M/R0/muscle_2.aligned.fasta > 16S.M/R0/muscle_2_fasttree.nwk
python compare.py 16S.M/R0/16S.M.reference.nwk 16S.M/R0/muscle_2_fasttree.nwk >> result.csv
printf '%s ' $(bc <<< "scale=2;($end - $start)/1000000000" ) >> result.csv

./FastTree -nt -gtr 16S.M/R0/cleaned.alignment.fasta > 16S.M/R0/true_fasttree.nwk
python compare.py 16S.M/R0/16S.M.reference.nwk 16S.M/R0/true_fasttree.nwk >> result.csv
printf '\n' >> result.csv

python table_n_plottin.py