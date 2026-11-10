# incremental-sfm-experiments

`incremental-sfm-experiments` is the experimental, benchmarking, and analytical workspace for the [`incremental-sfm`](https://github.com/chuo-v/incremental-sfm) pipeline. It contains Jupyter notebooks, post-processing utilities, quantitative JSON telemetry logs, reconstructed 3D point clouds (`.ply`), comparative charts (`.png`), and standalone browser-interactive 3D visualizations (`.html`) across five multi-view datasets.

## Companion Repositories & Datasets

This repository operates alongside two companion repositories and the public OpenMVG benchmark suite that complete the 3D reconstruction ecosystem:

- **[`incremental-sfm`](https://github.com/chuo-v/incremental-sfm):** The core pure-Python incremental Structure from Motion (SfM) engine and polymorphic feature-matching pipeline (`SIFT`, `SuperPoint` + `LightGlue`, and `ORB`).
- **[`incremental-sfm-datasets`](https://github.com/chuo-v/incremental-sfm-datasets):** Houses the curated Phase 2 NTU campus image sequences (`nantah-memorial-P42` and `yunnan-garden-pavilion-P71`) and calibrated camera intrinsic matrices (`K.txt`).
- **[`openMVG/SfM_quality_evaluation`](https://github.com/openMVG/SfM_quality_evaluation):** Provides the Phase 1 calibrated multi-view benchmark sequences and ground-truth camera intrinsics (`K.txt`):
  - [`entry-P10`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/entry-P10) (10 views)
  - [`Herz-Jesus-P25`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/Herz-Jesus-P25) (25 views)
  - [`castle-P30`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/castle-P30) (30 views)

## Interactive 3D Point Cloud Visualizations (`.html`)

Every baseline and ablation run in this repository includes a pre-rendered, standalone **interactive 3D HTML visualization** (`point_cloud_<MATCHER>_visualization.html`) inside its respective `output/.../visualizations/` directory.

These files are completely self-contained and require **no Python environment or 3D software** to inspect:
1. **Download a single file or clone the repository:** Click any link in the table below and select **"Download raw file"** (top-right corner of the GitHub file viewer) to save an individual `.html` file, or clone this repository to your local machine.
2. **Open in your browser:** Double-click the downloaded `point_cloud_<MATCHER>_visualization.html` file to open it directly in any web browser (Chrome, Safari, Firefox, or Edge).
3. **Interact with the 3D scene:** Use your mouse or trackpad to **orbit (left-click + drag)**, **pan (right-click + drag)**, and **zoom (scroll)** around the reconstructed point cloud.

### Quick Links to Final Baseline 3D Visualizations (`output/01_final/`)

Click any link below to view the file on GitHub, then click the **Download raw file** button to download and open the interactive 3D model in your browser:

| Phase | Dataset | SIFT (`.html`) | SuperPoint + LightGlue (`.html`) | ORB (`.html`) |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Benchmark** | `entry-P10` | [`point_cloud_SIFT_visualization.html`](./output/01_final/01_benchmark_entry_p10/visualizations/point_cloud_SIFT_visualization.html) | [`point_cloud_SuperPoint_visualization.html`](./output/01_final/01_benchmark_entry_p10/visualizations/point_cloud_SuperPoint_visualization.html) | [`point_cloud_ORB_visualization.html`](./output/01_final/01_benchmark_entry_p10/visualizations/point_cloud_ORB_visualization.html) |
| **Phase 1: Benchmark** | `Herz-Jesus-P25` | [`point_cloud_SIFT_visualization.html`](./output/01_final/02_benchmark_herz_jesus_p25/visualizations/point_cloud_SIFT_visualization.html) | [`point_cloud_SuperPoint_visualization.html`](./output/01_final/02_benchmark_herz_jesus_p25/visualizations/point_cloud_SuperPoint_visualization.html) | [`point_cloud_ORB_visualization.html`](./output/01_final/02_benchmark_herz_jesus_p25/visualizations/point_cloud_ORB_visualization.html) |
| **Phase 1: Benchmark** | `castle-P30` | [`point_cloud_SIFT_visualization.html`](./output/01_final/03_benchmark_castle_p30/visualizations/point_cloud_SIFT_visualization.html) | [`point_cloud_SuperPoint_visualization.html`](./output/01_final/03_benchmark_castle_p30/visualizations/point_cloud_SuperPoint_visualization.html) | [`point_cloud_ORB_visualization.html`](./output/01_final/03_benchmark_castle_p30/visualizations/point_cloud_ORB_visualization.html) |
| **Phase 2: NTU Field** | `nantah-memorial-P42` | [`point_cloud_SIFT_visualization.html`](./output/01_final/04_evaluation_nantah_memorial_p42/visualizations/point_cloud_SIFT_visualization.html) | [`point_cloud_SuperPoint_visualization.html`](./output/01_final/04_evaluation_nantah_memorial_p42/visualizations/point_cloud_SuperPoint_visualization.html) | [`point_cloud_ORB_visualization.html`](./output/01_final/04_evaluation_nantah_memorial_p42/visualizations/point_cloud_ORB_visualization.html) |
| **Phase 2: NTU Field** | `yunnan-garden-pavilion-P71` | [`point_cloud_SIFT_visualization.html`](./output/01_final/05_evaluation_yunnan_garden_pavilion_p71/visualizations/point_cloud_SIFT_visualization.html) | [`point_cloud_SuperPoint_visualization.html`](./output/01_final/05_evaluation_yunnan_garden_pavilion_p71/visualizations/point_cloud_SuperPoint_visualization.html) | [`point_cloud_ORB_visualization.html`](./output/01_final/05_evaluation_yunnan_garden_pavilion_p71/visualizations/point_cloud_ORB_visualization.html) |

*(Note: Interactive `.html` visualizations for all three ablation conditions are identically structured under [`output/02_ablations/`](./output/02_ablations/).)*

## Experimental Design

Our evaluation is structured into three analytical tracks across five datasets:

1. **Final Baseline Evaluations (`01_final`):**
   - **Phase 1 (Controlled Benchmark Validation):** Evaluates `SIFT`, `SuperPoint`, and `ORB` on calibrated [OpenMVG `Benchmarking_Camera_Calibration_2008`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008) sequences ([`entry-P10`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/entry-P10), [`Herz-Jesus-P25`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/Herz-Jesus-P25), and [`castle-P30`](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008/castle-P30)) at full resolution (`downscale_factor = 1.0`, `max_features = 50000`, `lowe_ratio_threshold = 0.75`, `ransac_threshold = 3.0`, `min_parallax_degrees = 1.0`).
   - **Phase 2 (Unconstrained NTU Campus Reconstruction):** Evaluates all three matchers on handheld smartphone sequences captured on the NTU campus (`nantah-memorial-P42` and `yunnan-garden-pavilion-P71` from [`incremental-sfm-datasets`](https://github.com/chuo-v/incremental-sfm-datasets)) with adapted field parameters (`downscale_factor = 0.5`, `max_features = 50000`, `lowe_ratio_threshold = 0.80`, `ransac_threshold = 6.0`, `min_parallax_degrees = 1.0`).
2. **Component Ablation Studies (`02_ablations`):**
   - **`01_disable_clahe`:** Evaluates the impact of disabling Contrast Limited Adaptive Histogram Equalization (`apply_clahe = False`) across shadowed stone facades, rough concrete, and dense foliage.
   - **`02_disable_symmetric_matching`:** Evaluates the impact of disabling bidirectional mutual nearest-neighbor cross-checking (`disable_symmetric_matching = True`).
   - **`03_disable_parallax_filter`:** Evaluates the impact of removing the minimum ray-intersection triangulation angle filter (`min_parallax_degrees = 0.0`).
3. **Cross-Condition Comparative Synthesis (`03_comparative_analysis`):**
   - Aggregates telemetry across the baseline and all three ablation conditions per dataset to generate unified multi-metric synthesis charts.

## Repository Structure

```text
incremental-sfm-experiments/
├── notebooks/
│   ├── 01_final/                           # Baseline evaluation notebooks (Phase 1 & Phase 2)
│   ├── 02_ablations/                       # Component ablation notebooks
│   │   ├── 01_disable_clahe/
│   │   ├── 02_disable_symmetric_matching/
│   │   └── 03_disable_parallax_filter/
│   └── 03_comparative_analysis/            # Cross-ablation synthesis notebooks
├── output/
│   ├── 01_final/                           # Artifacts for final baseline runs
│   │   └── <experiment_dir>/
│   │       ├── metrics/                    # Frame-by-frame & summary JSON telemetry
│   │       ├── point_clouds/               # Reconstructed 3D point clouds (.ply)
│   │       └── visualizations/             # Interactive 3D HTML files & PNG charts
│   ├── 02_ablations/                       # Artifacts for all 3 ablation conditions
│   │   ├── 01_disable_clahe/<experiment_dir>/...
│   │   ├── 02_disable_symmetric_matching/<experiment_dir>/...
│   │   └── 03_disable_parallax_filter/<experiment_dir>/...
│   └── 03_comparative_analysis/            # Multi-condition synthesis charts (.png)
│       └── <experiment_dir>/
├── scripts/
│   ├── __init__.py
│   └── visualize_point_cloud.py            # Point cloud outlier filtering & HTML rendering utility
├── requirements.txt                        # Python dependencies for notebooks & visualization
├── README.md                               # Project documentation
└── LICENSE                                 # MIT License
```

### Output Artifacts per Dataset Run

Each experiment directory (`01_benchmark_entry_p10` through `05_evaluation_yunnan_garden_pavilion_p71`) inside `output/01_final/` and `output/02_ablations/<ablation>/` contains:

* **`metrics/run_metrics_<MATCHER>.json`:** Logs pipeline hyperparameters, two-view initialization statistics, frame-by-frame PnP tracking and triangulation counts, and summary metrics (`total_3d_points`, `total_raw_matches`, `overall_rmse`, `rmse_variance`, `total_time_seconds`, `avg_frame_time_seconds`, `match_survival_rate`, `tracking_inlier_ratio`, `mean_track_length`, and `global_relocalizations`).
* **`point_clouds/point_cloud_<MATCHER>.ply`:** Standard ASCII `.ply` point cloud exported by the SfM engine.
* **`visualizations/point_cloud_<MATCHER>_visualization.html`:** Standalone interactive 3D point cloud viewer after Open3D Statistical and Radius Outlier Removal.
* **`visualizations/metrics_bar_chart_<dataset>.png` & `metrics_tradeoff_chart_<dataset>.png`:** Comparative bar and trade-off plots across `SIFT`, `SuperPoint`, and `ORB`.

Additionally, each directory inside `output/03_comparative_analysis/<experiment_dir>/` contains:

* **`metrics_synthesis_chart_<experiment_dir>.png`:** A unified multi-metric chart comparing the final baseline against all three component ablations across all matchers.

## Installation & Usage

### Viewing Pre-Computed Results

All JSON metrics, `.ply` point clouds, `.png` plots, and interactive `.html` 3D visualizations are already committed under [`output/`](./output/). You can browse the notebooks and charts directly on GitHub or download and open the `.html` files locally in any browser without installing dependencies.

### Re-Running Notebooks & Visualization Scripts

#### Option 1: Google Colab (Self-Contained)

Open any notebook under [`notebooks/`](./notebooks/) directly in Google Colab and run all cells. No manual setup is required—the notebook cells automatically clone [`incremental-sfm`](https://github.com/chuo-v/incremental-sfm) (`v1.2.0`), install all required engine and visualization packages (`plotly`, `kaleido`, `open3d`), and fetch the Phase 1 [OpenMVG benchmark sequences](https://github.com/openMVG/SfM_quality_evaluation/tree/master/Benchmarking_Camera_Calibration_2008) and Phase 2 [`incremental-sfm-datasets`](https://github.com/chuo-v/incremental-sfm-datasets) sequences directly from GitHub.

#### Option 2: Local Execution

1. Ensure **Python 3.10+** is installed and clone [`incremental-sfm`](https://github.com/chuo-v/incremental-sfm) as a sibling directory (`../incremental-sfm`) to your working directory.
2. Install the analytical and visualization dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Jupyter Lab or Jupyter Notebook to execute any notebook under [`notebooks/`](./notebooks/) or run [`scripts/visualize_point_cloud.py`](./scripts/visualize_point_cloud.py):
   ```bash
   jupyter lab
   ```