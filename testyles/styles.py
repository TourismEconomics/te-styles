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


def clear_font_cache():
    if (os.path.exists(mpl.get_cachedir())):
        shutil.rmtree(mpl.get_cachedir())
    return
