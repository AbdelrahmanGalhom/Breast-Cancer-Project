from pydantic import BaseModel
from typing import List, Optional, Literal

class RequestData(BaseModel):
    radius_mean: float
    texture_mean: float
    smoothness_mean: float
    symmetry_mean: float
    radius_se: float
    concavity_se: float
    concave_points_se: float
    fractal_dimension_se: float
    concavity_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float


