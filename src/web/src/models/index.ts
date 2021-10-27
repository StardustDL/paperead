export interface DocumentMetadataDto {
    creation: string;
    modification: string;
    name: string;
    tags: string[];
    schema: string;
    targets: { [key: string]: string };
    extra: { [key: string]: string };
}

export interface DocumentMetadata {
    creation: Date;
    modification: Date;
    name: string;
    tags: string[];
    schema: string;
    targets: { [key: string]: string };
    extra: { [key: string]: string };
}


export interface DocumentDto {
    id: string;
    content: string;
    metadata: DocumentMetadataDto;
}

export interface Document {
    id: string;
    content: string;
    dataUrl: string;
    metadata: DocumentMetadata;
}

export interface ApiMetadata {
    version: string;
}