import sys
import os

sys.path.insert(0, os.path.abspath('../quaternions_acse'))

extensions = ['sphinx.ext.autodoc']
source_suffix = '.rst'
master_doc = 'index'
project = u'Quaternions'
exclude_patterns = ['_build']
autoclass_content = "both"
