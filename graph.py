from multiprocessing.dummy import Array
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from config import ranks, colors

def create_graph_image(base: int, history: list[int]):
    mmrhistory = [base]
    mmr = base
    for match in history:
        mmr += match
        mmrhistory.append(mmr)
    xs = np.arange(len(mmrhistory))
    plt.style.use('lounge_style.mplstyle')
    lines = plt.plot(mmrhistory)
    plt.setp(lines, 'color', 'snow', 'linewidth', 1.0)
    xmin, xmax, ymin, ymax = plt.axis()
    plt.xlabel("Matches played")
    plt.ylabel("MMR")
    plt.grid(True, 'both', 'both', color='snow', linestyle=':')

    for i in range(len(ranks)):
        if ranks[i] > ymax:
            continue
        maxfill = ymax
        if i + 1 < len(ranks):
            if ranks[i] < ymin and ranks[i+1] < ymin:
                continue
            if ranks[i+1] < ymax:
                maxfill = ranks[i+1]
        if ranks[i] < ymin:
            minfill = ymin
        else:
            minfill = ranks[i]
        plt.fill_between(xs, minfill, maxfill, color=colors[i])
    plt.fill_between(xs, ymin, mmrhistory, color='#212121')
    b = BytesIO()
    plt.savefig(b, format='png', bbox_inches='tight')
    b.seek(0)
    plt.close()
    return b
