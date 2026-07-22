# Build the course documentation site.
#   make html      -> docs_site/_build/html/index.html
#   make clean     -> remove generated sources and build output

SPHINXBUILD ?= sphinx-build
SOURCEDIR    = .
BUILDDIR     = _build

.PHONY: html clean

html:
	python3 generate.py
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"
	@echo
	@echo "Open $(BUILDDIR)/html/index.html"

clean:
	rm -rf "$(BUILDDIR)" modules extras
