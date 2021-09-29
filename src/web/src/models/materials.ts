import { BaseMetadata, BaseMetadataDto } from "."

export interface MaterialMetadataDto extends BaseMetadataDto {
}

export interface MaterialDto {
    id: string;
    content: string;
    metadata: MaterialMetadataDto;
}

export interface MaterialMetadata extends BaseMetadata {
}

export interface Material {
    id: string;
    content: string;
    metadata: MaterialMetadata;
}