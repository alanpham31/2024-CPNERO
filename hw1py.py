import numpy as np
import seaborn as sns
import matplotlib as plt
import pandas as pd
import matplotlib.pyplot as plt

from allensdk.core.cell_types_cache import CellTypesCache

ctc = CellTypesCache(manifest_file='cell_types/manifest.json')
features = pd.DataFrame(ctc.get_all_features(require_reconstruction=True))
cell_metadata = pd.DataFrame(ctc.get_cells())

df = pd.merge(
    features[
        ['vrest', 'avg_isi', 'f_i_curve_slope', 'latency', 'number_branches', 'threshold_v_ramp', 'total_volume']
        ],

    cell_metadata[
        ['species', 'name', 'structure_hemisphere', 'structure_area_abbrev', 'structure_layer_name', 'disease_state']
        ],

    left_index=True, right_index=True)

df = df.dropna()

print(df.vrest)

