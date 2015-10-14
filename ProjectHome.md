This is a tool for doing sentiment analysis.  The short-term goal of this project is to share the sentiment analysis research.  The long-term goal of this project is to allow researchers the ability to demonstrate and test sentiment analysis tools, so that performance can be evaluated and compared.

Currently, the models are trained on Twitter data from the 2012 US Presidential election.  In the future we hope to have general models as well as models for other domains.

This code was first released by the collaboration of two labs at the
University of Southern California (USC), the [Signal Analysis and Interpretation Laboratory (SAIL)](http://sail.usc.edu) and [Annenberg Innovation Laboratory (AIL)](http://annenberglab.com).
The sentiment research at SAIL is supported by grants including NSF, NIH, and
DARPA.  The sentiment research at AIL is sponsored by the lab sponsors,
especially IBM, an AIL founding sponsor, and Orange, the flagship brand of
France Telecom.

This work was made possible by using existing open source projects and code.
NLTK (nltk.org) provides some of the basic classes of the SASA tool,
e.g. frequency distributions and classifiers.  Christopher Potts' twitter-specific tokenizer for sentiment analysis is used for tokenization.