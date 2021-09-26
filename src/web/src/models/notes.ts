export interface NoteMetadataDto {
    creation: string;
    modification: string;
    name: string;
}

export interface NoteDto {
    id: string;
    content: string;
    metadata: NoteMetadataDto;
}

export interface NoteMetadata {
    creation: Date;
    modification: Date;
    name: string;
}

export interface Note {
    id: string;
    content: string;
    metadata: NoteMetadata;
}