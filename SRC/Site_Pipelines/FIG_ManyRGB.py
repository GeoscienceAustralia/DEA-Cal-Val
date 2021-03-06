import DEAPlotting
import matplotlib.pyplot as plt

import importlib
importlib.reload(DEAPlotting)

#
### FIGURE 
#
# Plot large-area context RGB array for satellite data
#
def FIG_many_RGB(ls8_array, s2a_array, s2b_array, output, field_data, fignum):

    DEAPlotting.three_band_image_subplots(ls8_array, bands = ['red', 'green', 'blue'], num_cols=4, figsize = (18, 25), contrast_enhance=False)
    DEAPlotting.three_band_image_subplots(s2a_array, bands = ['nbart_red', 'nbart_green', 'nbart_blue'], num_cols=4, figsize = (18, 25), contrast_enhance=False)
    DEAPlotting.three_band_image_subplots(s2b_array, bands = ['nbart_red', 'nbart_green', 'nbart_blue'], num_cols=4, figsize = (18, 25), contrast_enhance=False)

    plt.savefig(output+field_data[0]+'_'+field_data[1]+'_'+field_data[2]+'_'+field_data[3]+'_'+'Fig'+str(fignum)+'_Satellite_bigRGB.png')
