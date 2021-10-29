import { isRelativeUrl } from '../helpers'
import { ApiMetadata } from '../models'
import { MaterialRepository } from './repository'

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

    async title() {
        let result = (await this.metadata()).site.title;
        return result == "" ? "Paperead" : result;
    }
}
