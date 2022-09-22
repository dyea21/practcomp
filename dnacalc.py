#! /usr/bin/env python

#DNASeq = 'ATCGATCGATCG'

DNASeq = input('Enter a DNA sequence: ')
DNASeq = DNASeq.upper()
DNASeqp = DNASeq.replace(' ', '')

print('\n\nSequence: ', DNASeq, '\n')

SeqLength = float(len(DNASeq))

print('Sequence Length: ', SeqLength)

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

#print('A: ', NumberA/SeqLength)
#print('C: ', NumberC/SeqLength)
#print('G: ', NumberG/SeqLength)
#print('T: ', NumberT/SeqLength)

TotalStrong = NumberC + NumberG
TotalWeak = NumberA + NumberT

if SeqLength < 14:

	MeltTemp = (4 * TotalStrong) + (2* TotalWeak)
	print('\nMelting Temp: ', MeltTemp, ' C\n')
else:

	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print('\nMelting Temp: ', MeltTempLong, ' C\n')

BaseList = 'ATCG'
for Base in BaseList:
	Percent = 100 * DNASeq.count(Base) / SeqLength
	print(Base, Percent, '%')

Comp=DNASeq.replace('A','t')
Comp=Comp.replace('T','a')
Comp=Comp.replace('C','g')
Comp=Comp.replace('G','c')

print('\nThe complimentary sequence is: ', Comp, '\n')

print('The reverse compliment is: ', Comp[::-1], '\n')

