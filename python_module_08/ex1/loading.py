#!/usr/bin/env python3

from importlib.util import find_spec
from importlib.machinery import ModuleSpec
from importlib.metadata import version


def packages_infos(requirements: list[str], excludes: list[str]) -> None:
    response: dict[str, str] = {'pandas': 'Data manipulation ready',
                                'matplotlib': 'Visualization ready',
                                'requests': 'Network access ready',
                                'numpy': 'Numerical computation ready'}

    try:
        for pack in requirements:
            try:
                package: ModuleSpec | None = None
                if not (pack in excludes):
                    package = find_spec(pack)

                name = getattr(package, "name", "unknown")
                package_version = version(name)
                print(f"[OK] {name} ({package_version}) - {response[name]}")
            except Exception:
                if pack in response.keys():
                    print(f"[MISSING] {pack} - {response[pack]}")
    except Exception:
        raise Exception("Error on geting packages infos.")


def loading() -> None:
    try:
        print("LOADING STATUS: Loading programs...\n")

        requirements: list[str] = ['numpy', 'pandas', 'requests', 'matplotlib']

        packages_infos(requirements, [])
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":

    try:
        loading()

        import pandas as pd
        from pandas import DataFrame
        import numpy as np
        import matplotlib.pyplot as plt

        def generate_random_points(
            num_points: int = 1000,
            seed: int | None = None
        ) -> tuple[list[int], list[int]]:
            if seed is not None:
                np.random.seed(seed)
            res_x = np.random.randint(0, 101, size=num_points).tolist()
            res_y = np.random.randint(0, 101, size=num_points).tolist()
            return [int(x) for x in res_x], [int(y) for y in res_y]

        def create_dataframe(x: list[int], y: list[int]) -> DataFrame:
            return pd.DataFrame({'x': x, 'y': y})

        def visualize_points(
                df: DataFrame,
                title: str = 'Scatter Plot of Random Points'
        ) -> None:
            plt.figure(figsize=(8, 6))
            plt.scatter(df['x'], df['y'], c='blue', alpha=0.5, edgecolors='k')
            plt.title(title)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True)
            plt.show()

        def save_scatter_plot(
                df: DataFrame,
                filename: str = 'scatter_plot.png',
                title: str = 'Scatter Plot of Random Points') -> str | None:
            try:
                plt.figure(figsize=(8, 6))
                plt.scatter(df['x'], df['y'], c='blue',
                            alpha=0.5, edgecolors='k')
                plt.title(title)
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.grid(True)
                plt.savefig(filename, dpi=300, bbox_inches='tight')
                plt.close()
                return filename
            except Exception:
                raise Exception("Error on saving visualisation")

        print("\nAnalyzing Matrix data...")
        num_points = 1000
        print(f"Processing {num_points} data points...")
        x, y = generate_random_points(num_points, seed=42)
        df: DataFrame = create_dataframe(x, y)

        print("Generating visualization...")
        # visualize_points(df)
        print("\nAnalysis complete!")
        graph: str | None = save_scatter_plot(df)
        print(f"Results saved to: {graph}")
    except Exception as err:
        print(f"\nError: {err}")
