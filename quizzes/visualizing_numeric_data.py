import pandas as pd
import matplotlib.pyplot as plt

def bp_histogram(bp):
    fig3, ax3 = plt.subplots(1)

    bp["diastolic"].plot.hist(color=(0.1,0.5,0.5,0.5), ax=ax3, bins=20)
    bp["systolic"].plot.hist(color=(1,0,0,0.5), ax=ax3, bins=20)
    ax3.set_xlabel("blood pressure (mmHg)")
    ax3.legend()
