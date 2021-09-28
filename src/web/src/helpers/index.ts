export function isRelativeUrl(url: string) {
    return url?.startsWith("./") || url?.startsWith("../") || url == "." || url == "..";
}