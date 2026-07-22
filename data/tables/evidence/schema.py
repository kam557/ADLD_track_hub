from pydantic import Field
from adld_track_hub.utils.models import RowData
from typing import final

@final
class Schema(RowData):
    publications: str | None = Field(alias = "Publications")
    literature_cases: str | None = Field(alias = "Literature case labels")
    families: str | None = Field(alias = "Multigenerational families")
    estimated_individuals: str | None = Field(alias = "Estimated unique affected individuals")
    status: str | None = Field(alias = "Deduplication status")
