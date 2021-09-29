import { BaseMetadataDto, BaseMetadata } from ".";

export interface NoteMetadataDto extends BaseMetadataDto {
}

export interface NoteDto {
    id: string;
    content: string;
    metadata: NoteMetadataDto;
}

export interface NoteMetadata extends BaseMetadata {
}

export interface Note {
    id: string;
    content: string;
    metadata: NoteMetadata;
}