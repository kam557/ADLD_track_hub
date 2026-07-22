from pydantic import Field
from adld_track_hub.utils.models import RowData
from typing import final

@final
class Schema(RowData):
    publications: int | None = Field(alias = "Publications")
    literature_cases: int | None = Field(alias = "Literature case labels")
    families: int | None = Field(alias = "Multigenerational families")
    estimated_individuals: str | None = Field(alias = "Estimated unique affected individuals")
    status: str | None = Field(alias = "Deduplication status")
