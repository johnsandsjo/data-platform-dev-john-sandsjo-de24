import matplotlib.pyplot as plt


def line_chart(x, y, **options):
    fig, ax = plt.subplots(1)

    ax.plot(x, y, linewidth=4)
    # ax.set(
    #     title=options.get("title"),
    #     xlabel=options.get("xlabel"),
    #     ylabel=options.get("ylabel"),
    # )
    #instead of writign all this, we can "unload" the dictionary with **options 
    ax.set(**options)

    fig.tight_layout()
    return fig