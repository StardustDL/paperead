import { isRelativeUrl } from '../helpers';
import { ApiMetadata, Document, DocumentMetadata, DocumentMetadataDto } from '../models';
import { Material, MaterialDto } from '../models/materials'
import { Note, NoteDto } from '../models/notes'

export class MaterialRepository {
    baseUrl: string;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async all() {
        let results = await fetch(`${this.baseUrl}/index.json`);
        return <string[]>(await results.json());
    }

    async get(id: string) {
        let results = await fetch(`${this.baseUrl}/${id}/index.json`);
        let raw = <MaterialDto>(await results.json());

        let item: Material = {
            ...raw,
            metadata: {
                ...raw.metadata,
                creation: new Date(raw.metadata.creation.toString()),
                modification: new Date(raw.metadata.modification.toString()),
            },
            dataUrl: this.resolveRelativeUrl(id)
        };
        return item;
    }

    notes(id: string) {
        return new NoteRepository(`${this.baseUrl}/${id}/notes`, this.resolveRelativeUrl(id, "./notes"));
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

        await fetch(`${this.baseUrl}/`, {
            body: JSON.stringify(raw),
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    async delete(id: string) {
        await fetch(`${this.baseUrl}/${id}`, {
            method: "DELETE"
        });
    }

    resolveRelativeUrl(id: string, url: string = ".") {
        if (isRelativeUrl(url))
            return `${this.baseUrl}/${id}/${url}`
        return url;
    }
}

export class NoteRepository {
    baseUrl: string;
    dataUrl: string;

    constructor(baseUrl: string, dataUrl: string) {
        this.baseUrl = baseUrl;
        this.dataUrl = dataUrl;
    }

    async all() {
        let results = await fetch(`${this.baseUrl}/index.json`);
        return <string[]>(await results.json());
    }

    async get(id: string) {
        let results = await fetch(`${this.baseUrl}/${id}/index.json`);
        let raw = <NoteDto>(await results.json());

        let item: Note = {
            ...raw,
            metadata: {
                ...raw.metadata,
                creation: new Date(raw.metadata.creation.toString()),
                modification: new Date(raw.metadata.modification.toString()),
            },
            dataUrl: this.dataUrl
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

        await fetch(`${this.baseUrl}/`, {
            body: JSON.stringify(raw),
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    async delete(id: string) {
        await fetch(`${this.baseUrl}/${id}/`, {
            method: "DELETE"
        });
    }
}