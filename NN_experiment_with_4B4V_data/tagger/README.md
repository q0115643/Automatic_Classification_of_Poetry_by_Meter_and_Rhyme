## NER Tagger

NER Tagger is an implementation of a Named Entity Recognizer that obtains state-of-the-art performance in NER on the 4 CoNLL datasets (English, Spanish, German and Dutch) without resorting to any language-specific knowledge or resources such as gazetteers. Details about the model can be found at: http://arxiv.org/abs/1603.01360


## Initial setup

To use the tagger, you need Python 2.7, with Numpy and Theano installed.


## Tag sentences

The fastest way to use the tagger is to use one of the pretrained models:

```
./tagger.py --model models/english/ --input input.txt --output output.txt
```

The input file should contain one sentence by line, and they have to be tokenized. Otherwise, the tagger will perform poorly.


## Train a model

To train your own model, you need to use the train.py script and provide the location of the training, development and testing set:

```
./train.py --train train.txt --dev dev.txt --test test.txt
```

The training script will automatically give a name to the model and store it in ./models/
There are many parameters you can tune (CRF, dropout rate, embedding dimension, LSTM hidden layer size, etc). To see all parameters, simply run:

```
./train.py --help
```

Input files for the training script have to follow the same format than the CoNLL2003 sharing task: each word has to be on a separate line, and there must be an empty line after each sentence. A line must contain at least 2 columns, the first one being the word itself, the last one being the named entity. It does not matter if there are extra columns that contain tags or chunks in between. Tags have to be given in the IOB format (it can be IOB1 or IOB2).


Options:

  -h, --help            show this help message and exit

  -T TRAIN, --train=TRAIN
                        Train set location

  -d DEV, --dev=DEV     Dev set location

  -t TEST, --test=TEST  Test set location

  -s TAG_SCHEME, --tag_scheme=TAG_SCHEME
                        Tagging scheme (IOB or IOBES)

  -l LOWER, --lower=LOWER
                        Lowercase words (this will not affect character
                        inputs)

  -z ZEROS, --zeros=ZEROS
                        Replace digits with 0

  -c CHAR_DIM, --char_dim=CHAR_DIM
                        Char embedding dimension

  -C CHAR_LSTM_DIM, --char_lstm_dim=CHAR_LSTM_DIM
                        Char LSTM hidden layer size

  -b CHAR_BIDIRECT, --char_bidirect=CHAR_BIDIRECT
                        Use a bidirectional LSTM for chars

  -w WORD_DIM, --word_dim=WORD_DIM
                        Token embedding dimension

  -W WORD_LSTM_DIM, --word_lstm_dim=WORD_LSTM_DIM
                        Token LSTM hidden layer size

  -B WORD_BIDIRECT, --word_bidirect=WORD_BIDIRECT
                        Use a bidirectional LSTM for words

  -p PRE_EMB, --pre_emb=PRE_EMB
                        Location of pretrained embeddings

  -A ALL_EMB, --all_emb=ALL_EMB
                        Load all embeddings

  -a CAP_DIM, --cap_dim=CAP_DIM
                        Capitalization feature dimension (0 to disable)

  -f CRF, --crf=CRF     Use CRF (0 to disable)

  -D DROPOUT, --dropout=DROPOUT
                        Droupout on the input (0 = no dropout)

  -L LR_METHOD, --lr_method=LR_METHOD
                        Learning method (SGD, Adadelta, Adam..)

  -r RELOAD, --reload=RELOAD
                        Reload the last saved model
