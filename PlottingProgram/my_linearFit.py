
import numpy as np
import matplotlib.pyplot as plt
from typing import Sequence, Union

def plot_data(
    x: Union[Sequence[float], np.ndarray],
    y: Union[Sequence[float], np.ndarray],
    xlabel: str = 'x',
    ylabel: str = 'y'
):
    """
    Create a linear fit of y vs. x and plot both the raw data and the fit.

    Parameters
    ----------
    x, y : array-like
        Sequences of numerical data. Must have the same length.
    xlabel, ylabel : str, optional
        Labels for the x- and y-axes.
    """

    # Convert inputs to numpy arrays
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)

    # Validate shapes
    if x_arr.ndim != 1 or y_arr.ndim != 1:
        raise ValueError("Both x and y must be one-dimensional sequences.")
    if x_arr.shape[0] != y_arr.shape[0]:
        raise ValueError(f"x and y must have the same length. "
                         f"Got len(x)={x_arr.shape[0]} and len(y)={y_arr.shape[0]}.")

    # Compute linear fit
    slope, intercept = np.polyfit(x_arr, y_arr, deg=1)

    # Plot settings
    marker_size = 6
    label_font  = 14
    tick_font   = 12
    line_width  = 2

    fig, ax = plt.subplots(figsize=(8, 5))

    # Raw data
    ax.scatter(
        x_arr, y_arr,
        s=marker_size**2,
        color='C1',
        label='Data'
    )

    # Linear fit
    ax.plot(
        x_arr,
        slope * x_arr + intercept,
        color='C2',
        linewidth=line_width,
        label= f'Linear Fit: ${ylabel.split(' ')[0]} = {slope:.3f}\\,{xlabel.split(' ')[0]}$' + f'${intercept:+.3f}$'
    )

    # Labels, title, ticks
    ax.set_xlabel(xlabel, fontsize=label_font)
    ax.set_ylabel(ylabel, fontsize=label_font)
    ax.tick_params(labelsize=tick_font)
    ax.set_title(
        f'Linear Fit: ${ylabel.split(' ')[0]} = {slope:.3f}\\,{xlabel.split(' ')[0]}$' + f'${intercept:+.3f}$',
        fontsize=label_font
    )

    # Legend and layout
    ax.legend(fontsize=tick_font)
    plt.tight_layout()
    plt.show()

    # Send the fit back to the calling instruction
    thefit = f'Linear Fit:\n\t   {ylabel.split(' ')[0]} = {slope:.3f}{xlabel.split(' ')[0]}' + f'{intercept:+.3f}'
    return thefit    # end function

# ENTERING THE DATA. Any example could be deleted when using your own data
# Example 1
# horizontal axis data
t = [0.415, 0.463, 0.495, 0.543, 0.59, 0.623, 0.67, 0.703, 0.75,
              0.798, 0.83, 0.878, 0.911]
# vertical axis data
y = [94.502235, 117.412667, 135.238955, 162.386387, 190.20431,
              213.717107, 245.60903, 273.357827, 308.50975, 347.228182,
              381.35147, 422.513902, 456.130699]
xlabel='t (s)'
ylabel='y (m)'
thefit = plot_data(t, y, xlabel, ylabel)
print(thefit)
#----------------End example 1

# Example 2
xlabel='T (K)'
ylabel='P (atm)'

# horizontal axis data
T = [ 173, 223, 273, 323, 373, 423]

# vertical axis data
P = [ 36.0, 46.4, 56.7, 67.1, 77.5, 88.0]

thefit = plot_data(T, P, xlabel, ylabel)
print(thefit)
#----------------End example 2


