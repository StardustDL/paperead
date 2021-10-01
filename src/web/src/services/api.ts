import { isRelativeUrl } from '../helpers';
import { ApiMetadata } from '../models';
import { Material, MaterialDto, MaterialMetadata } from '../models/materials'
import { Note, NoteDto, NoteMetadata, NoteMetadataDto } from '../models/notes'
import { MaterialRepository } from './repository';

export class Api {
    baseUrl: string;
    materials: MaterialRepository;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
        this.materials = new MaterialRepository(`${this.baseUrl}/materials`);
    }

    async metadata() {
        let results = await fetch(`${this.baseUrl}/index.json`);
        return <ApiMetadata>(await results.json());
    }
}
