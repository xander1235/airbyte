# generated by datamodel-codegen:
#   filename:  NormalizationDestinationDefinitionConfig.yaml

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class NormalizationDestinationDefinitionConfig(BaseModel):
    class Config:
        extra = Extra.allow

    normalizationRepository: str = Field(
        ...,
        description="a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used.",
    )
    normalizationTag: str = Field(
        ...,
        description="a field indicating the tag of the docker repository to be used for normalization.",
    )
    normalizationIntegrationType: str = Field(
        ...,
        description="a field indicating the type of integration dialect to use for normalization.",
    )