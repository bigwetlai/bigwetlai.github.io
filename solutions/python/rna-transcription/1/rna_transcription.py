def to_rna(dna_strand):
    DNA = "GCTA"
    RNA_transcript = "CGAU"

    dna_strand = dna_strand.translate(str.maketrans(DNA, RNA_transcript))

    return dna_strand
