from pydantic import Field
from adld_track_hub.utils.models import RowData
from typing import final

@final
class Schema(RowData):
    origin: str | None = Field(alias = "Country of origin")
    number: str | None = Field(alias = "Number of Individuals Affected ")
    age: str | None = Field(alias = "Age of Onset (years)")
    symptoms: str | None = Field(alias = "Commonly reported symptoms")
    imaging: str | None = Field(alias = "Commonly reported imaging results")
