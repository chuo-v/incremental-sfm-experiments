import argparse
import os
from pathlib import Path
import numpy as np
import open3d as o3d
import plotly.graph_objects as go
from dotenv import load_dotenv


def visualize_point_cloud(
    dataset_name: str,
    matcher: str,
    data_dir: str = None,
    nb_neighbors: int = 20,
    std_ratio: float = 2.0,
    nb_points: int = 3,
    radius: float = 1.0,
):
    """
    Loads, filters, renders, and exports a full-width interactive 3D point cloud.
    """
    # Resolve data directory
    if data_dir is None:
        load_dotenv()
        data_dir = os.getenv("DATA_DIR")
        if not data_dir:
            raise ValueError(
                "DATA_DIR not found. Please pass 'data_dir' as an argument or "
                "ensure your .env file is configured."
            )

    data_dir_path = Path(data_dir)

    # Construct paths matching the incremental-sfm engine's output structure
    pc_dir = data_dir_path / dataset_name / "output" / "point_clouds"
    vis_dir = data_dir_path / dataset_name / "output" / "visualizations"
    vis_dir.mkdir(parents=True, exist_ok=True)

    ply_filename = f"point_cloud_{matcher}.ply"
    ply_path = pc_dir / ply_filename

    if not ply_path.exists():
        raise FileNotFoundError(
            f"[{matcher}] Point cloud file not found at: {ply_path}"
        )

    print(f"[{matcher}] Loading point cloud from: {ply_path}")

    # Load the point cloud using Open3D
    pcd = o3d.io.read_point_cloud(str(ply_path))

    if pcd.is_empty():
        raise ValueError(f"[{matcher}] The point cloud is empty or failed to load.")

    original_count = len(pcd.points)
    print(f"[{matcher}] Successfully loaded {original_count} points.")

    # Apply statistical and radius outlier removal
    print(f"[{matcher}] Running outlier removal...")
    pcd_filtered, _ = pcd.remove_statistical_outlier(
        nb_neighbors=nb_neighbors, std_ratio=std_ratio
    )
    pcd_filtered, _ = pcd_filtered.remove_radius_outlier(
        nb_points=nb_points, radius=radius
    )

    filtered_count = len(pcd_filtered.points)
    print(
        f"[{matcher}] Removed {original_count - filtered_count} extreme outliers. Remaining: {filtered_count} pts."
    )

    # Extract coordinates and standard 8-bit RGB colors for Plotly
    points = np.asarray(pcd_filtered.points)
    colors_normalized = np.asarray(pcd_filtered.colors)
    colors_rgb = (colors_normalized * 255).astype(int)
    colors_str = [f"rgb({r}, {g}, {b})" for r, g, b in colors_rgb]

    # Render full-width interactive 3D plot
    print(f"[{matcher}] Generating Plotly visualization...")
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=points[:, 0],
                y=points[:, 1],
                z=points[:, 2],
                mode="markers",
                marker=dict(size=2, color=colors_str, opacity=0.8),
                name=matcher,
            )
        ]
    )

    fig.update_layout(
        title=f"{matcher} Reconstruction ({dataset_name}) - {filtered_count} pts",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode="data",
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=0, y=-1.5, z=1.5),
            ),
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        height=800,
    )

    # Export figure to an HTML file
    html_path = vis_dir / f"point_cloud_{matcher}_visualization.html"
    fig.write_html(str(html_path))
    print(f"[{matcher}] Interactive 3D plot exported to: {html_path}")

    # Open the interactive plot
    fig.show()


def main():
    parser = argparse.ArgumentParser(
        description="Visualize SfM Point Cloud with Plotly"
    )
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Name of the dataset folder",
    )
    parser.add_argument(
        "--matcher",
        type=str,
        default="SIFT",
        choices=["SIFT", "SuperPoint", "ORB"],
        help="Feature matching algorithm used to generate the point cloud",
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default=None,
        help="Path to the datasets directory (overrides .env DATA_DIR)",
    )
    parser.add_argument(
        "--nb_neighbors",
        type=int,
        default=20,
        help="Number of neighbors for statistical outlier removal",
    )
    parser.add_argument(
        "--std_ratio",
        type=float,
        default=2.0,
        help="Standard deviation ratio for statistical outlier removal",
    )
    parser.add_argument(
        "--nb_points",
        type=int,
        default=3,
        help="Minimum number of points for radius outlier removal",
    )
    parser.add_argument(
        "--radius",
        type=float,
        default=1.0,
        help="Radius limit for radius outlier removal",
    )
    args = parser.parse_args()

    visualize_point_cloud(
        dataset_name=args.dataset,
        matcher=args.matcher,
        data_dir=args.data_dir,
        nb_neighbors=args.nb_neighbors,
        std_ratio=args.std_ratio,
        nb_points=args.nb_points,
        radius=args.radius,
    )


if __name__ == "__main__":
    main()
