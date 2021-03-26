import pandas as pd


def plot_decline_curve(parent, curve_name=None, reset=True):
    """Plot decline curve from curves that have been created"""

    figure = parent.widget_production_plot

    phase = parent.ui.comboBoxPhase.currentText()

    if curve_name is None:

        if phase == "oil":
            curve_name = str(parent.ui.comboBoxOilDeclineCurves.currentText())
        else:
            curve_name = str(parent.ui.comboBoxGasDeclineCurves.currentText())

    if reset:
        well_name = parent.ui.comboBoxWellSelect.currentText()
        parent.widget_production_plot.plot_production(parent, well_name)

    if phase == "Oil":
        color = "g"
        units = "MBO"
        unit_factor = 1_000
    else:
        color = "r"
        units = "MCF"
        unit_factor = 1_000

    df_curve = parent.decline_curves_dict.get(curve_name)
    figure.axes.plot(
        df_curve.index,
        df_curve[curve_name],
        color,
        label=curve_name,
        linestyle="dashdot",
        linewidth=2,
    )
    figure.axes.legend(
        bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0
    )

    # Technical EURs (MBO/BCF), user monthly grouper to handle daily data

    groupby_monthly = df_curve.groupby(pd.Grouper(freq="M")).sum()

    plot_decline_curve.eur_1_year = round(groupby_monthly[curve_name][:11].sum() / unit_factor, 1)
    plot_decline_curve.eur_5_year = round(groupby_monthly[curve_name][:59].sum() / unit_factor, 1)
    plot_decline_curve.eur_10_year = round(groupby_monthly[curve_name][:119].sum() / unit_factor, 1)
    plot_decline_curve.eur_50_year = round(groupby_monthly[curve_name][:599].sum() / unit_factor, 1)

    textstr = "\n".join(
        (
            f"{curve_name}",
            f"1 Year EUR: {plot_decline_curve.eur_1_year:,} {units}",
            f"5 Year EUR: {plot_decline_curve.eur_5_year:,} {units}",
            f"10 Year EUR: {plot_decline_curve.eur_10_year:,} {units}",
        )
    )

    try:
        del figure.ax.texts[-1]
    except:
        pass

    text_box_props = dict(boxstyle="round", facecolor="white")
    text_box = figure.axes.text(
        0.75,
        0.95,
        textstr,
        transform=figure.axes.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=text_box_props,
    )

    figure.draw()
