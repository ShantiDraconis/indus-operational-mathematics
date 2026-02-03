# Indus Operational Mathematics - Build Instructions

## Building the Book

### Requirements

- LaTeX distribution (TeX Live 2020 or later, or MiKTeX)
- Required LaTeX packages (installed by default in most distributions):
  - amsmath, amsfonts, amssymb, amsthm
  - graphicx, hyperref, geometry
  - fancyhdr, enumerate, listings
  - xcolor, tikz, float

### Compilation Steps

```bash
cd book/
pdflatex main.tex
pdflatex main.tex  # Run twice for table of contents
```

If you have bibliography entries:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Output

The compiled PDF will be `book/main.pdf`

## Running the Code

### Requirements

- Python 3.8 or later
- For Jupyter notebook analysis:
  - pandas
  - matplotlib
  - seaborn
  - numpy
  - jupyter

### Install Dependencies

```bash
pip install pandas matplotlib seaborn numpy jupyter
```

### Run Python Scripts

```bash
cd code/
python indus_dfa.py
python operator_model.py
```

### Run Jupyter Notebook

```bash
cd code/
jupyter notebook frequency_analysis.ipynb
```

## Data Files

Data files are in CSV format in the `data/` directory. They can be:
- Opened in spreadsheet applications (Excel, LibreOffice Calc)
- Processed with Python pandas
- Analyzed with R or other statistical tools

## Figures

The `figures/` directory is organized by category. Add your own figures here:
- Use PDF or SVG for vector graphics
- Use PNG (300 DPI) for raster images
- Follow the naming conventions in the README files

## Repository Status

This repository is ready for:
- ✅ Development and collaboration
- ✅ Version control with Git
- ✅ LaTeX compilation
- ✅ Python analysis
- ✅ Zenodo archiving (add DOI badge to README when available)

## Next Steps

1. Populate figure directories with actual diagrams
2. Expand data files with complete corpus data
3. Add more detailed analysis in Jupyter notebooks
4. Create automated build scripts
5. Generate PDF releases for Zenodo
6. Add CI/CD for automated LaTeX compilation
