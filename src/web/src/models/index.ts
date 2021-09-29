export interface BaseMetadataDto {
    creation: string;
    modification: string;
    name: string;
    tags: string[];
    targets: { [key: string]: string };
    extra: { [key: string]: string };
}

export interface BaseMetadata {
    creation: Date;
    modification: Date;
    name: string;
    tags: string[];
    targets: { [key: string]: string };
    extra: { [key: string]: string };
}