import { marked } from "marked"
import { Document } from '../../models';
import { isRelativeUrl } from '../../helpers';

export class Media {
    title: string;
    url: string = "";
    description: string = "";
    cover: string = "";
    renderedDescription: string = "";

    constructor(title: string) {
        this.title = title;
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
            let media = new Media(title);
            while (index < tokens.length) { // detect url & description
                let token = tokens[index];
                if (token.type == "heading" && token.depth == 1) {
                    break;
                }

                let isMetadata = false;
                if (token.type == "paragraph") {
                    for (let subtoken of token.tokens) {
                        if (subtoken.type == "image" || subtoken.type == "link") {
                            let href = subtoken.href;

                            if (isRelativeUrl(href)) {
                                href = `${data.dataUrl}/${href}`;
                            }

                            switch (subtoken.text) {
                                case "url":
                                    if (media.url == "") {
                                        media.url = href;
                                        isMetadata = true;
                                    }
                                    break;
                                case "cover":
                                    if (media.cover == "") {
                                        media.cover = href;
                                        isMetadata = true;
                                    }
                                    break;
                            }
                        }
                    }
                }
                if (!isMetadata)
                    media.description += token.raw;
                index++;
            }


            media.renderedDescription = marked(media.description, {
                baseUrl: data.dataUrl,
                headerIds: false,
                smartLists: true,
                smartypants: true,
            })
            results.push(media);
        }
    }

    return results;
}