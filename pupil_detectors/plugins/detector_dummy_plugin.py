"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2019 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""
import typing as T

from .detector_base_plugin import PupilDetector, PupilDetectorPlugin


class DetectorDummyPlugin(PupilDetectorPlugin):

    ########## PupilDetectorPlugin API

    @property
    def pupil_detector(self) -> PupilDetector:
        return self

    def gl_display(self):
        pass

    ########## PupilDetector API

    ##### Legacy API

    def set_2d_detector_property(self, name: str, value: T.Any):
        pass

    def set_3d_detector_property(self, name: str, value: T.Any):
        pass

    ##### Core API

    def detect(self, frame, user_roi, visualize, pause_video: bool = False, **kwargs):
        return {}

    def namespaced_detector_properties(self) -> dict:
        return {}

    def on_resolution_change(self, old_size, new_size):
        pass
