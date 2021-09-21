import matplotlib.pyplot as plt
import matplotlib as mpl
import shutil
import os

def init_styles():
    clear_font_cache()

    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = 'Lato'
    plt.style.use('https://raw.githubusercontent.com/jackminchin/te-styles/main/oxfordeconomics.mplstyle')


    plt.title()

    return


def clear_font_cache():
    if (os.path.exists(mpl.get_cachedir())):
        shutil.rmtree(mpl.get_cachedir())
    return
