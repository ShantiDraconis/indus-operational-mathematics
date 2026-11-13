"""Os testes desta pasta são do pacote python/indus_analysis (distribuição indus-analysis,
com setup.py próprio). src/indus_analysis.py tem o mesmo nome, então python/ vai na frente."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "python")))
