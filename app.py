from pathlib import Path

import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO

from inspection import classify_result


st.set_page_config(page_title="Bottle Defect Demo")


@st.cache_resource
def load_model(model_path: str) -> YOLO:
    return YOLO(model_path)


st.title("Bottle packaging defect demo")
st.caption(
    "A local computer-vision prototype. It flags detected defects for review; "
    "it does not certify conformity."
)

model_path = st.text_input("Path to an authorized YOLO model", value="best.pt")
confidence = st.slider(
    "Detection confidence threshold",
    min_value=0.10,
    max_value=0.95,
    value=0.40,
    step=0.05,
)
uploaded_image = st.file_uploader(
    "Choose a bottle image",
    type=("jpg", "jpeg", "png", "webp"),
)

if uploaded_image is None:
    st.info("Add an image to run a local inspection.")
    st.stop()

if uploaded_image.size > 20 * 1024 * 1024:
    st.error("Image is larger than the 20 MiB demo limit.")
    st.stop()

model_file = Path(model_path).expanduser()
if not model_file.is_file():
    st.error(
        f"Model not found: {model_file}. Provide an authorized .pt weights file "
        "or train one using train_run.ipynb."
    )
    st.stop()

model = load_model(str(model_file.resolve()))
image_bytes = np.frombuffer(uploaded_image.getvalue(), dtype=np.uint8)
image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
if image is None:
    st.error("The selected file could not be decoded as an image.")
    st.stop()

with st.spinner("Running the detector on this image..."):
    result = model.predict(
        source=image,
        conf=confidence,
        device="cpu",
        verbose=False,
    )[0]

boxes = result.boxes
detection_count = 0 if boxes is None else len(boxes)
outcome = classify_result(detection_count)
annotated_image = result.plot()

if outcome == "defect_detected":
    st.error(f"{detection_count} defect indication(s) detected - review required.")
else:
    st.warning("No defect detected - conformity is not verified.")

st.image(
    cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB),
    caption="Detector output",
    use_container_width=True,
)

encoded_ok, encoded_image = cv2.imencode(".jpg", annotated_image)
if not encoded_ok:
    st.error("Could not encode the annotated image for download.")
    st.stop()

st.download_button(
    "Download annotated image",
    data=encoded_image.tobytes(),
    file_name="bottle-inspection.jpg",
    mime="image/jpeg",
)

st.caption(
    "The configured detector has defect classes only; it does not verify bottle "
    "presence, inspection completeness, or product conformity."
)
