from __future__ import absolute_import
import os
import pkg_resources

from permamodel.components.bmi_frost_number import BmiFrostnumberMethod as FrostNumber
from permamodel.components.bmi_Ku_component import BmiKuMethod as Ku


FrostNumber.__name__ = "FrostNumber"
FrostNumber.METADATA = os.path.abspath(
    pkg_resources.resource_filename("pymt_permamodel", "data/FrostNumber")
)

Ku.__name__ = "Ku"
Ku.METADATA = os.path.abspath(
    pkg_resources.resource_filename("pymt_permamodel", "data/Ku")
)

__all__ = ["FrostNumber", "Ku"]
