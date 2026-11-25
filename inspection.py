from typing import Literal

InspectionOutcome = Literal["defect_detected", "no_defect_detected"]


def classify_result(detection_count: int) -> InspectionOutcome:
    if detection_count < 0:
        raise ValueError("detection_count cannot be negative")
    if detection_count:
        return "defect_detected"
    return "no_defect_detected"
