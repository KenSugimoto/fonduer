from sqlalchemy import Column, Float

from fonduer.meta import Meta
from fonduer.utils.models.annotation import AnnotationKeyMixin, AnnotationMixin


class PredictionKey(AnnotationKeyMixin, Meta.Base):  # type: ignore
    pass


class Prediction(AnnotationMixin, Meta.Base):  # type: ignore
    """
    A probability associated with a Candidate, indicating the degree of belief
    that the Candidate is true.

    A Prediction's annotation key indicates which process or method produced
    the Prediction, e.g., which model with which ParameterSet.
    """

    value = Column(Float, nullable=False)
