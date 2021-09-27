import matplotlib.pyplot as plt
import matplotlib as mpl
import shutil
import os

mainStyles = 'https://raw.githubusercontent.com/TourismEconomics/te-styles/main/oxfordeconomics.mplstyle'


def init_styles(styleSheet = mainStyles):

    ''' Initialises styling for TE plots with hosted stylesheet or manual override'''

    clear_font_cache()

    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = 'Lato'
    plt.style.use(styleSheet)

    return



def subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw):
    fig, axes = plt.subplots(nrows, ncols, sharex=sharex, sharey=sharey, squeeze=squeeze, subplot_kw=subplot_kw, gridspec_kw=gridspec_kw, **fig_kw)

    plt.xlabel('Source: Oxford Economics', wrap=True, horizontalalignment='left', fontsize=8, x=0)
    return fig, axes

def clear_font_cache():
    if (os.path.exists(mpl.get_cachedir())):
        shutil.rmtree(mpl.get_cachedir())
    return
