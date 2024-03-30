import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps
from matplotlib.colors import LinearSegmentedColormap


def truncate_colormap(color_map_name: str,
                      minval: float = 0.0,
                      maxval: float = 1.0,
                      rgb_quantization_levels: int = 100) -> LinearSegmentedColormap:
    """
    Truncate a given colormap to a specified range.
    Please refer to:
    https://blog.csdn.net/weixin_46090057/article/details/119882021

    Args
    ----
    color_map_name: string
        The name of the colormap to be truncated.
    minval: float
        The minimum value of the truncated range.
        Default is 0.0.
    maxval: float
        The maximum value of the truncated range.
        Default is 1.0.
    rgb_quantization_levels: int
        The number of RGB quantization levels
        used to define the new colormap.
        Default is 100.

    Returns
    -------
    Returns the truncated colormap.
    """
    selected_color_map = colormaps[color_map_name]

    truncated_color_map = LinearSegmentedColormap.from_list(
        f"trunc({color_map_name}, {minval:.2f}, {maxval:.2f})",
        selected_color_map(
            np.linspace(minval, maxval, rgb_quantization_levels)
        ),
    )
    return truncated_color_map


if __name__ == "__main__":

    two_dim_data_gradient = np.linspace(0, 50, 100).reshape((10, 10))

    trunc_cmap_plasma = truncate_colormap("plasma", 0.2, 1.0)
    trunc_cmap_viridis = truncate_colormap("viridis", 0.2, 1.0)

    fig, ax = plt.subplots(ncols=4)

    ax[0].imshow(
        two_dim_data_gradient,
        interpolation="nearest",
        cmap=colormaps["plasma"]
    )
    ax[1].imshow(
        two_dim_data_gradient,
        interpolation="nearest",
        cmap=trunc_cmap_plasma
    )
    ax[2].imshow(
        two_dim_data_gradient,
        interpolation="nearest",
        cmap=colormaps["viridis"]
    )
    ax[3].imshow(
        two_dim_data_gradient,
        interpolation="nearest",
        cmap=trunc_cmap_viridis
    )

    plt.show()
