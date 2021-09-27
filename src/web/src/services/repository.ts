import { isRelativeUrl } from '../helpers';
import { Material, MaterialDto, MaterialMetadata } from '../models/materials'
import { Note, NoteDto, NoteMetadata, NoteMetadataDto } from '../models/notes'

export class MaterialRepository {
    baseUrl: string
    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async all() {
        let results = await fetch(`${this.baseUrl}/materials/`);
        return <string[]>(await results.json());
    }

    async get(id: string) {
        let results = await fetch(`${this.baseUrl}/materials/${id}`);
        let raw = <MaterialDto>(await results.json());

        let item: Material = {
            ...raw,
            metadata: {
                ...raw.metadata,
                creation: new Date(raw.metadata.creation.toString()),
                modification: new Date(raw.metadata.modification.toString()),
            },
        };
        return item;
    }

    notes(id: string) {
        return new NoteRepository(`${this.baseUrl}/materials/${id}`);
    }

    async update(value: Material) {
        let raw: MaterialDto = {
            ...value,
            metadata: {
                ...value.metadata,
                creation: value.metadata.creation.toISOString(),
                modification: value.metadata.modification.toISOString(),
            },
        };

        await fetch(`${this.baseUrl}/materials/`, {
            body: JSON.stringify(raw),
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    async delete(id: string) {
        await fetch(`${this.baseUrl}/materials/${id}`, {
            method: "DELETE"
        });
    }

    resolveRelativeUrl(id: string, url: string = "."){
        if(isRelativeUrl(url))
            return `${this.baseUrl}/materials/${id}/${url}`
        return url;
    }
}

export class NoteRepository {
    baseUrl: string
    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async all() {
        let results = await fetch(`${this.baseUrl}/notes/`);
        return <string[]>(await results.json());
    }

    async get(id: string) {
        let results = await fetch(`${this.baseUrl}/notes/${id}`);
        let raw = <NoteDto>(await results.json());

        let item: Note = {
            ...raw,
            metadata: {
                ...raw.metadata,
                creation: new Date(raw.metadata.creation.toString()),
                modification: new Date(raw.metadata.modification.toString()),
            },
        };
        return item;
    }

    async update(value: Note) {
        let raw: NoteDto = {
            ...value,
            metadata: {
                ...value.metadata,
                creation: value.metadata.creation.toISOString(),
                modification: value.metadata.modification.toISOString(),
            },
        };

        await fetch(`${this.baseUrl}/notes/`, {
            body: JSON.stringify(raw),
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    async delete(id: string) {
        await fetch(`${this.baseUrl}/notes/${id}`, {
            method: "DELETE"
        });
    }
}