"""
chart_helpers.py
Helper functions for the AI Analytics system.
Always import this file and apply the analytics style before generating charts.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os

# ─────────────────────────────────────────────────────────
# THEME APPLICATION
# ─────────────────────────────────────────────────────────

# Colors — Dark theme (default)
DARK = {
    "background": "#1A1A2E",
    "text_primary": "#E8E8F0",
    "text_secondary": "#9090A8",
    "story_color": "#4FC3F7",
    "negative": "#EF5350",
    "positive": "#66BB6A",
    "gray": "#555570",
    "grid": "#2A2A45",
    "spine": "#3A3A5A",
}

# Colors — Light theme
LIGHT = {
    "background": "#FAFAFA",
    "text_primary": "#1A1A2E",
    "text_secondary": "#5A5A72",
    "story_color": "#1565C0",
    "negative": "#C62828",
    "positive": "#2E7D32",
    "gray": "#B0B0C0",
    "grid": "#E8E8F0",
    "spine": "#C8C8D8",
}


def get_theme(theme="dark"):
    """Return color dict for the given theme. Use 'dark' or 'light'."""
    return DARK if theme == "dark" else LIGHT


def apply_style(fig, ax, theme="dark", show_grid=True, spine_bottom_only=True):
    """
    Apply analytics style to a matplotlib figure and axes.
    Call this after creating your chart, before saving.
    """
    c = get_theme(theme)

    fig.patch.set_facecolor(c["background"])
    ax.set_facecolor(c["background"])

    # Spines
    for spine in ax.spines.values():
        spine.set_visible(False)
    if spine_bottom_only:
        ax.spines["bottom"].set_visible(True)
        ax.spines["bottom"].set_color(c["spine"])
        ax.spines["bottom"].set_linewidth(0.8)

    # Tick colors
    ax.tick_params(colors=c["text_secondary"], labelsize=10)

    # Grid
    if show_grid:
        ax.yaxis.grid(True, color=c["grid"], linewidth=0.5, linestyle="-")
        ax.set_axisbelow(True)
    ax.xaxis.grid(False)

    # Title styling
    if ax.get_title():
        ax.title.set_color(c["text_primary"])
        ax.title.set_fontsize(14)
        ax.title.set_fontweight("semibold")
        ax.title.set_loc("left")  # Left-align titles

    # Axis label styling
    ax.xaxis.label.set_color(c["text_secondary"])
    ax.yaxis.label.set_color(c["text_secondary"])

    return fig, ax


# ─────────────────────────────────────────────────────────
# CHART FACTORY FUNCTIONS
# ─────────────────────────────────────────────────────────

def bar_chart(
    categories,
    values,
    title,
    story_index=None,
    theme="dark",
    xlabel=None,
    ylabel=None,
    annotation=None,
    figsize=(10, 5.5),
):
    """
    Horizontal bar chart with gray-first-then-color styling.

    Parameters:
        categories: list of category labels
        values: list of numeric values
        title: action title for the chart (states the insight)
        story_index: int or list of ints — index of bars to highlight in story color
        theme: 'dark' or 'light'
        xlabel: optional x-axis label
        ylabel: optional y-axis label
        annotation: dict with keys 'index' (bar index), 'text' (annotation string)
        figsize: tuple (width, height) in inches
    """
    c = get_theme(theme)
    fig, ax = plt.subplots(figsize=figsize)

    # Base color: all gray
    colors = [c["gray"]] * len(categories)

    # Apply story color
    if story_index is not None:
        if isinstance(story_index, int):
            story_index = [story_index]
        for i in story_index:
            colors[i] = c["story_color"]

    bars = ax.barh(categories, values, color=colors, height=0.6)

    # Direct value labels
    for bar, val in zip(bars, values):
        label_x = bar.get_width() + (max(values) * 0.01)
        ax.text(
            label_x,
            bar.get_y() + bar.get_height() / 2,
            f"{val:,.0f}" if isinstance(val, (int, float)) else str(val),
            va="center",
            ha="left",
            color=c["text_secondary"],
            fontsize=10,
        )

    # Annotation
    if annotation:
        idx = annotation["index"]
        bar = bars[idx]
        ax.annotate(
            annotation["text"],
            xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
            xytext=(bar.get_width() + max(values) * 0.12, bar.get_y() + bar.get_height() / 2),
            ha="left",
            va="center",
            color=c["story_color"],
            fontsize=10,
            fontweight="semibold",
        )

    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    ax.invert_yaxis()  # Largest bar at top
    ax.set_xlim(0, max(values) * 1.25)

    apply_style(fig, ax, theme=theme)
    plt.tight_layout()
    return fig, ax


def line_chart(
    x,
    y_series,
    title,
    story_keys=None,
    theme="dark",
    xlabel=None,
    ylabel=None,
    figsize=(10, 5.5),
):
    """
    Line chart with gray-first-then-color styling.

    Parameters:
        x: list of x values (dates or categories)
        y_series: dict of {label: [values]} for each line
        title: action title for the chart
        story_keys: list of keys from y_series to highlight in story color
        theme: 'dark' or 'light'
    """
    c = get_theme(theme)
    fig, ax = plt.subplots(figsize=figsize)

    story_keys = story_keys or []

    for i, (label, values) in enumerate(y_series.items()):
        is_story = label in story_keys
        color = c["story_color"] if is_story else c["gray"]
        lw = 2.5 if is_story else 1.0
        zorder = 3 if is_story else 2

        ax.plot(x, values, color=color, linewidth=lw, zorder=zorder, label=label)

        # End-of-line label
        ax.text(
            len(x) - 1,
            values[-1],
            f"  {label}",
            va="center",
            ha="left",
            color=color,
            fontsize=10,
            fontweight="semibold" if is_story else "normal",
        )

    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    apply_style(fig, ax, theme=theme)
    ax.set_xlim(0, len(x) - 1 + len(x) * 0.15)  # Space for end labels
    plt.tight_layout()
    return fig, ax


def grouped_bar_chart(
    categories,
    series_dict,
    title,
    story_series=None,
    theme="dark",
    xlabel=None,
    ylabel=None,
    figsize=(10, 5.5),
):
    """
    Grouped bar chart (vertical) for side-by-side period comparisons.

    Parameters:
        categories: list of category labels
        series_dict: dict of {series_label: [values]} — e.g., {'2024': [...], '2025': [...]}
        title: action title
        story_series: list of series labels to highlight
        theme: 'dark' or 'light'
    """
    c = get_theme(theme)
    fig, ax = plt.subplots(figsize=figsize)

    story_series = story_series or []
    n_series = len(series_dict)
    n_cats = len(categories)
    width = 0.6 / n_series
    x = np.arange(n_cats)

    for i, (label, values) in enumerate(series_dict.items()):
        is_story = label in story_series
        color = c["story_color"] if is_story else c["gray"]
        offset = (i - (n_series - 1) / 2) * width
        bars = ax.bar(x + offset, values, width=width * 0.9, color=color, label=label)

    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    apply_style(fig, ax, theme=theme)
    plt.tight_layout()
    return fig, ax


# ─────────────────────────────────────────────────────────
# SAVE UTILITY
# ─────────────────────────────────────────────────────────

def save_chart(fig, filename, output_dir="../outputs/charts", dpi=200):
    """
    Save chart to the outputs/charts directory.

    Parameters:
        fig: matplotlib figure
        filename: filename without path (e.g., 'beat-03-island-yoy.png')
        output_dir: directory to save into
        dpi: resolution (default 200 for presentation quality)
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"✅ Chart saved: {filepath}")
    return filepath


# ─────────────────────────────────────────────────────────
# USAGE EXAMPLE
# ─────────────────────────────────────────────────────────
# 
# from helpers.chart_helpers import bar_chart, save_chart
#
# fig, ax = bar_chart(
#     categories=["Maui", "O'ahu", "Kaua'i", "Big Island", "Moloka'i"],
#     values=[107, 93, 96, 98, 95],
#     title="Maui was the only island with visitor growth in 2025",
#     story_index=0,
#     theme="dark",
#     annotation={"index": 0, "text": "Only island up YoY"},
# )
# save_chart(fig, "beat-02-island-yoy.png")
