import unittest

from inspection import classify_result


class ClassifyResultTests(unittest.TestCase):
    def test_detected_defects_require_review(self):
        self.assertEqual(classify_result(1), "defect_detected")

    def test_no_detections_do_not_confirm_conformity(self):
        self.assertEqual(classify_result(0), "no_defect_detected")

    def test_negative_detection_count_is_rejected(self):
        with self.assertRaises(ValueError):
            classify_result(-1)


if __name__ == "__main__":
    unittest.main()
