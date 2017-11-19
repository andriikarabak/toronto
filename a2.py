def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if DNA sequence dna is valid - contains no characters
    other than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence('AATCCGA')
    True
    >>> is_valid_sequence('ATTCGGS')
    False
    """

    valid_nucle = 'ACGT'

    for nucle in dna:
        if not nucle in valid_nucle:
            return False
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> atr

    Return the DNA sequence obtained by inserting DNA sequence dna2
    into DNA sequence dna1 at the given index.

    Precondition: the index is valid.

    >>> insert_sequence('ACCTG', 'AT', 3)
    ACCATTG
    >>> insert_sequence('ACCTTC', 'ATCG', 1)
    AATCGCCTTC
    """

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str
    
    Return the nucleotide's complement.
    
    >>> get_complement('A')
    T
    >>> get_complement{'G')
    C
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """ (str) - str
    
    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('ACGTAT')
    TGCATA
    """

    complementary_sequence = ''

    for nucl in dna:
        complementary_sequence = complementary_sequence + get_complement(nucl)
    return complementary_sequence

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1