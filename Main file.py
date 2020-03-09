import pandas as pd
import matplotlib as mpl
import numpy as np
import cmapPy as cmp
import cmapPy.pandasGEXpress.setup_GCToo_logger as setup_logger
from cmapPy.pandasGEXpress.parse_gct import parse
from cmapPy.pandasGEXpress.write_gct import write


data = parse('PAAD.gct')

data.row_metadata_df.dropna(inplace=True)

data.data_df = data.data_df.loc[data.row_metadata_df.index]
data.data_df = data.data_df.apply (pd.to_numeric, errors='coerce')
data.data_df =  data.data_df.replace(np.nan, 0)
write(data, 'save.gct')
