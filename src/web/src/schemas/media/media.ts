import { marked } from "marked"
import { Document } from '../../models';
import { isRelativeUrl } from '../../helpers';

export class Media {
    title: string;
    url: string = "";
    description: string = "";
    cover: string = "";
    lrc: string = "";
    author: string = "";
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
                            let resolvedHref = href;

                            if (isRelativeUrl(resolvedHref)) {
                                resolvedHref = `${data.dataUrl}/${resolvedHref}`;
                            }

                            switch (subtoken.text) {
                                case "url":
                                    if (media.url == "") {
                                        media.url = resolvedHref;
                                        isMetadata = true;
                                    }
                                    break;
                                case "cover":
                                    if (media.cover == "") {
                                        media.cover = resolvedHref;
                                        isMetadata = true;
                                    }
                                    break;
                                case "lrc":
                                    if (media.lrc == "") {
                                        media.lrc = resolvedHref;
                                        isMetadata = true;
                                    }
                                    break;
                                case "author":
                                    if (media.author == "") {
                                        media.author = href;
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