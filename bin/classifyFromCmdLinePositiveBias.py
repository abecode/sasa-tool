#!/usr/bin/python

""" This code reads lines from STDIN and classifies them as
negative/neutral/positive/unsure.  it also outputs valence (negative the
posterior probability of "negative" if classified as negative, or the
posterior probability of "positive" if classified positive, or 0 otherwise) as well as the posterior probability for each class. """

__author__ = "Abe Kazemzadeh"
__copyright__ = "Copyright 2013, University of Southern California"
__credits__ = []
__license__ = "http://www.apache.org/licenses/LICENSE-2.0"
__version__ = "1.0"
__maintainer__ = "last modified by Abe Kazemzadeh"
__email__ = "See the author's website"

import sys

try:
    from sasa.classifier import Classifier
except ImportError:
    raise ImportError("Did you try to run '. setup.env'?\n" + 
                      "(or add the sasa-tool directory to PYTHONPATH, ie export PYTHONPATH=<this director>)?")


classifier = Classifier("model.unigram.nb.bool.politics.positivebias")    

for line in sys.stdin:
    print "classifying %s"%line.strip()
    sentiment, valence, posterior = classifier.classifyFromText(line)
    print sentiment, 
    print valence, 
    print "pNeg=%s"%str(posterior.prob("negative")), 
    print "pNeu=%s"%str(posterior.prob('neutral')), 
    print "pPos=%s"%str(posterior.prob('positive')), 
    print "pUns=%s"%str(posterior.prob('unsure')), 
    print
