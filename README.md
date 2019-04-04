# Automatic_Classification_of_Poetry_by_Neural_Scansion
CS570 Term Project: Automatic Classification of Poetry by Neural Scansion

[Detailed Report](https://github.com/q0115643/Automatic_Classification_of_Poetry_by_Neural_Scansion/blob/master/Team13_Final%20Paper_Automatic%20Classification%20of%20Poetry%20by%20Neural%20Scansion.pdf)


## Base Paper

"Automatic Classification of Poetry by Meter and Rhyme"

Proceedings of AAAI 2016

University of Ottawa

Chris Tanasescu, Bryan Paget, and Diana Inkpen 


## Our Model


End-to-End model of

### poem crawler

from https://www.poetryfoundation.org/

### Syllable Extraction

Model: Character-level Bi-LSTM-CRF model

Dataset: WebCelex (160,595 words with syllable structures)

For poetryfoundation poem data (to extract syllables for ultimate goal)

34,324 words are included in WebCelex <- Known words

25,729 words are not included (need to extract by our model) <- Unknown words

Trainset 154,595 words(including all known words), Devset 3,000, Testset 3,000 words


### Meter(강세) Generation

Model: Character-level Bi-LSTM-CRF model

Dataset: For Better For Verse (4B4V) (87 poems, 1,187 lines with syllable, meter features)

Trainset 951 lines, Devset 118, Testset 118 lines

Include special characters (?, !, ‘, .) those might have information for meters

By using syllables, we lose the word structures

add Word-Boundaries (*) to syllables (ex. *And* | *sings* | *a* | *me | lan | cho | ly* | *strain* )

### Also the baseline model by "Automatic Classification of Poetry by Meter and Rhyme"

## Results and Evaluations

in [Detailed Report](https://github.com/q0115643/Automatic_Classification_of_Poetry_by_Neural_Scansion/blob/master/Team13_Final%20Paper_Automatic%20Classification%20of%20Poetry%20by%20Neural%20Scansion.pdf)
