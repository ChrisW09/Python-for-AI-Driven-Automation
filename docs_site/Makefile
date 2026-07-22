# Build the course documentation site.
#   make html       -> docs_site/_build/html/index.html
#   make linkcheck  -> report every unreachable link in the site
#   make clean      -> remove generated sources and build output

SPHINXBUILD ?= sphinx-build
SOURCEDIR    = .
BUILDDIR     = _build
# -W turns warnings into errors so a broken cross-link fails the build
# instead of quietly shipping; --keep-going still reports all of them.
SPHINXOPTS  ?= -W --keep-going

.PHONY: html linkcheck clean

html:
	python3 generate.py
	$(SPHINXBUILD) $(SPHINXOPTS) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"
	@echo
	@echo "Open $(BUILDDIR)/html/index.html"

linkcheck:
	python3 generate.py
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck"

clean:
	rm -rf "$(BUILDDIR)" modules extras _static
