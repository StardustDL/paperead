export interface MaterialMetadataDto {
    creation: string;
    modification: string;
    name: string;
    tags: string[];
    targets: { [key: string]: string };
    extra: { [key: string]: string };
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
    targets: { [key: string]: string };
    extra: { [key: string]: string };
}

export interface Material {
    id: string;
    content: string;
    metadata: MaterialMetadata;
}