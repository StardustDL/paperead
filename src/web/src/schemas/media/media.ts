// @ts-ignore
import marked from 'marked'
import { Document } from '../../models';
import { isRelativeUrl } from '../../helpers';

export class Media {
    title: string;
    url: string;
    description: string;
    renderedDescription: string = "";

    constructor(title: string, url: string, description: string = "") {
        this.url = url;
        this.title = title;
        this.description = description;
        this.renderedDescription = marked(this.description);
    }
}

export function parse(data: Document) {

    let results: Media[] = [];

    let tokens: any[] = marked.lexer(data.content);

    let index = 0;
    while (index < tokens.length) {
        let title = null;
        while (title == null && index < tokens.length) { // detect title in heading 1
            let token = tokens[index];
            if (token.type == "heading" && token.depth == 1)
                title = token.text;
            index++;
        }
        if (title != null) {
            let url = null;
            let description = "";
            while (index < tokens.length) { // detect url & description
                let token = tokens[index];
                if (token.type == "heading" && token.depth == 1) {
                    break;
                }

                let isUrl = false;
                if (url == null) {
                    if (token.type == "paragraph" && token.tokens.length == 1) {
                        let subtoken = token.tokens[0];
                        if (subtoken.type == "image") {
                            isUrl = true;
                            url = subtoken.href;
                            if (isRelativeUrl(url)) {
                                url = `${data.dataUrl}/${url}`;
                            }
                        }
                    }
                }
                if (!isUrl)
                    description += token.raw;
                index++;
            }

            results.push(new Media(title, url, description));
        }
    }

    return results;
}