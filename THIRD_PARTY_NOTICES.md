# Third-party notices

This is an initial inventory of direct runtime dependencies and local assets,
not a complete legal or transitive-dependency audit.

| Component | Observed version | License information |
|---|---:|---|
| Ultralytics | 8.4.2 | Ultralytics describes its open-source software as AGPL-3.0 and offers a separate Enterprise license for certain deployment scenarios. Review the current [license terms](https://www.ultralytics.com/license). |
| OpenCV (`opencv-python`) | 4.12.0.88 | OpenCV 4.5.0 and later use Apache-2.0 according to the [OpenCV license page](https://opencv.org/license/). |

The versions above were visible in the existing notebook environment; they
were not installed or freshly scanned during this preparation.

## Excluded assets

The local dataset, custom `best.pt`, and `yolov8n.pt` are excluded from the
proposed public release until their origin and redistribution permissions are
verified. The MIT license in this repository does not grant rights to those
assets.

The complete license and vulnerability status of transitive Python
dependencies has not been established. Review them for the exact environment
and deployment use before release.
