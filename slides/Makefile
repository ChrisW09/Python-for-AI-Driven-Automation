# Build the lecture decks.
#   make            -> all slide PDFs + all presenter (notes) PDFs
#   make slides     -> just the slide PDFs (what you project)
#   make notes      -> just the presenter PDFs (slide left, speaker notes right)
#   make 27_llm_fundamentals.pdf        -> one deck
#   make 27_llm_fundamentals_notes.pdf  -> one presenter deck
#   make clean      -> remove LaTeX aux files (keeps the PDFs)
#
# Two passes are run so the section-navigation bar and table of contents resolve.

LATEX   ?= pdflatex
LFLAGS   = -interaction=nonstopmode -halt-on-error
DECKS    = $(basename $(wildcard *.tex))
SLIDES   = $(addsuffix .pdf,$(DECKS))
NOTES    = $(addsuffix _notes.pdf,$(DECKS))
AUX      = *.aux *.log *.nav *.out *.snm *.toc *.vrb

.PHONY: all slides notes clean
.SECONDARY:

all: slides notes

slides: $(SLIDES)
notes: $(NOTES)

# The projected deck. Speaker notes are compiled out entirely.
%.pdf: %.tex
	$(LATEX) $(LFLAGS) $<
	$(LATEX) $(LFLAGS) $<

# The presenter deck: same slides, notes on a second screen to the right.
# \notesmode is what the decks test for in their preamble.
%_notes.pdf: %.tex
	$(LATEX) $(LFLAGS) -jobname=$*_notes "\def\notesmode{}\input{$<}"
	$(LATEX) $(LFLAGS) -jobname=$*_notes "\def\notesmode{}\input{$<}"

clean:
	rm -f $(AUX)
