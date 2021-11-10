import { marked } from "marked"

export function isRelativeUrl(url: string) {
    return url?.startsWith("./") || url?.startsWith("../") || url == "." || url == "..";
}


function counter(content: string) {
    const cn = (content.match(/[\u4E00-\u9FA5]/g) || []).length;
    const en = (content.replace(/[\u4E00-\u9FA5]/g, '').match(/[a-zA-Z0-9_\u0392-\u03c9\u0400-\u04FF]+|[\u4E00-\u9FFF\u3400-\u4dbf\uf900-\ufaff\u3040-\u309f\uac00-\ud7af\u0400-\u04FF]+|[\u00E4\u00C4\u00E5\u00C5\u00F6\u00D6]+|\w+/g) || []).length;
    return [cn, en];
};

export function min2read(content: string, { cn = 300, en = 160 } = {}) {
    var len = counter(content);
    var readingTime = len[0] / cn + len[1] / en;
    return readingTime;
};

export function wordcount(content: string) {
    var len = counter(content);
    var count = len[0] + len[1];
    return count;
};

function htmlEscapeToText(text: string) {

    return text.replace(/\&\#[0-9]*;|&amp;/g, function (escapeCode: string) {

        if (escapeCode.match(/amp/)) {

            return '&';

        }

        return String.fromCharCode(parseInt(escapeCode.match(/[0-9]+/)![0]));
    });
}

var plainTextRenderer = new marked.Renderer();

// render just the text of a link
plainTextRenderer.link = function (href, title, text) {
    return text;
};

// render just the text of a paragraph
plainTextRenderer.paragraph = function (text) {
    return htmlEscapeToText(text) + '\r\n';
};

// render just the text of a heading element, but indecate level
plainTextRenderer.heading = function (text, level) {
    return level + ') ' + text;
};

plainTextRenderer.blockquote = function (quote) {
    return quote;
};

plainTextRenderer.codespan = function (code) {
    return code;
};

plainTextRenderer.list = function (body, ordered, start) {
    return body;
};


// render nothing for images
plainTextRenderer.image = function (href, title, text) {
    return '';
};
plainTextRenderer.code = function (code, infostring, escaped) {
    return '';
};

export function renderToPlainText(mdtext: string) {
    return mdtext;
    return marked(mdtext, {
        renderer: plainTextRenderer
    })
}