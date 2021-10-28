import marked from "marked";

export function isRelativeUrl(url: string) {
    return url?.startsWith("./") || url?.startsWith("../") || url == "." || url == "..";
}

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