from pydantic import Field
from adld_track_hub.utils.models import RowData
from typing import final

@final
class Schema(RowData):
    pub: str | None = Field(alias = "Publication")
    pmid: str | int | None = Field(alias = "PMID")
    cases: str | None = Field(alias = "Cases reported")
