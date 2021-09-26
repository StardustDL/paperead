export interface MaterialMetadataDto {
    creation: string;
    modification: string;
    name: string;
    tags: string[];
    targets: string[];
}

export interface MaterialDto {
    id: string;
    content: string;
    metadata: MaterialMetadataDto;
}

export interface MaterialMetadata {
    creation: Date;
    modification: Date;
    name: string;
    tags: string[];
    targets: string[];
}

export interface Material {
    id: string;
    content: string;
    metadata: MaterialMetadata;
}