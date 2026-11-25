# Bottle Conformity Test

A Python and YOLOv8 computer-vision prototype for detecting visible bottle
packaging defects from a webcam. It can also retrain an object-detection model
from a YOLO-format dataset supplied by the user.

> **Prototype only:** this project is not a validated industrial inspection
> system and does not certify product conformity. The live notebook currently
> displays `CONFORME` whenever it detects no defect. It does not verify that a
> bottle is present, and a missed detection must not be treated as proof of
> conformity. Do not use it as the sole basis for quality, safety, or
> regulatory decisions.

## What it does

The project demonstrates two workflows:

1. **Live inspection:** load a trained YOLO model, select an available camera,
   detect packaging defects, draw bounding boxes, and display a status.
2. **Model training:** fine-tune the YOLOv8n model for 50 epochs using the
   dataset paths and five class names in `dataset_final/data.yaml`.

The configured defect classes are:

| Class ID | Defect |
|---:|---|
| 0 | Missing cap |
| 1 | Misaligned cap |
| 2 | Missing label |
| 3 | Misaligned label |
| 4 | Foreign object |

The live notebook uses a confidence threshold of `0.40`. It does not save
inspection histories, maintain traceability records, provide user accounts,
or store results in a database.

No project screenshots are included in the current workspace.

## Technology

- Python
- Jupyter Notebook
- Ultralytics YOLO
- OpenCV for webcam capture and drawing
- PyTorch, installed as an Ultralytics dependency

The dependency versions in `requirements.txt` reflect the versions recorded
in the existing successful notebook run. They have not been independently
validated across operating systems or hardware.

## Project layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── dataset_final/
│   └── data.yaml
├── test_live.ipynb
├── train_run.ipynb
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── THIRD_PARTY_NOTICES.md
└── CHANGELOG.md
```

Dataset images, labels, model weights, training outputs, Jupyter checkpoints,
and the unrelated local `test.py` utility are excluded from the proposed
release. The ignore rules do not delete those local files.

## Prerequisites

- Python with `pip`. Notebook metadata records Python 3.12.4 and 3.13.9; a
  supported-version range has not yet been established.
- A webcam accessible to OpenCV for live inference.
- For training, a compatible PyTorch device. The training notebook currently
  selects `device=0`; change it to `device='cpu'` to request CPU training.
- A separately obtained, authorized dataset and model weights (see below).

## Installation

Create and activate a virtual environment, then install the direct runtime
dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```sh
source .venv/bin/activate
```

Open the notebooks in Jupyter or an editor with notebook support. A notebook
frontend is not pinned in `requirements.txt` and may need to be installed
separately.

## Assets and configuration

The dataset images, labels, and both `.pt` weight files are deliberately not
included because their redistribution permissions have not been verified.
Do not publish or redistribute them until you have confirmed the rights and
license terms.

For training, supply a YOLO-format dataset under `dataset_final/` with:

```text
dataset_final/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
└── val/
    ├── images/
    └── labels/
```

The included `data.yaml` lists the five class names and expects the train and
validation directories above. The training notebook also uses `yolov8n.pt`;
Ultralytics may download that pretrained model if it is not present. For live
inference, provide an authorized compatible `best.pt` at the project root.

No environment variables, database, migrations, authentication, or deployment
configuration are currently used.

## Run the workflows

1. Open `train_run.ipynb` to retrain the detector. It uses 50 epochs, image
   size 640, batch size 8, and `workers=0`. Adjust `device=0` when a CUDA GPU
   is unavailable.
2. Open `test_live.ipynb` for live inference. Select a camera index when
   prompted and press `q` in the OpenCV window to quit.

Training and inference have not been validated as a complete clean install
from this release layout because the dataset and weights are excluded.

## Testing and validation

There is currently no automated test suite or CI workflow. The existing
notebook output showed a model loading and a camera frame being processed in
one local environment; that is not a general compatibility or accuracy
certification. No industrial acceptance, false-negative, or performance
testing has been established.

## Security and operational use

The webcam workflow appears to process frames locally and contains no explicit
upload or persistence logic. Ultralytics may access the network to obtain
weights or dependencies. Use only data you are authorized to process.

The current “no defect detected” behavior is not a valid conformity decision.
Validate the model against representative production conditions, measure
false positives and false negatives, add a bottle-presence/inspection-validity
check, and obtain domain and regulatory review before operational deployment.
See [SECURITY.md](SECURITY.md) for reporting security issues.

## Contributing

Contributions are welcome; read [CONTRIBUTING.md](CONTRIBUTING.md) first.
Please include reproducible steps and do not submit private data, unlicensed
images, credentials, or model artifacts.

## License and third-party terms

Original project code and documentation are offered under the MIT License in
[LICENSE](LICENSE). That does not relicense dependencies or assets. In
particular, Ultralytics is distributed under AGPL-3.0 terms with separate
Enterprise licensing for some deployment scenarios; review the current
[Ultralytics license terms](https://www.ultralytics.com/license) before
commercial, embedded, or customer-facing use. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Author

`omarlr-pro`

## Search visibility

After the repository has been made public, you can add its public URL in
[Google Search Console](https://search.google.com/search-console/), verify
ownership, inspect the repository URL, and request indexing. Google decides
whether and when to index a page; indexing and ranking are not guaranteed.
