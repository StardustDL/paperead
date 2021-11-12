if(-not (Test-Path ./public/static/css)){
    mkdir ./public/static/css
}
if(-not (Test-Path ./public/static/js)){
    mkdir ./public/static/js
}
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.0.0/github-markdown.min.css -OutFile ./public/static/css/github-markdown.min.css
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/aplayer/1.10.1/APlayer.min.css -OutFile ./public/static/css/APlayer.min.css
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/white.min.css -OutFile ./public/static/css/reveal-white.min.css
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/black.min.css -OutFile ./public/static/css/reveal-black.min.css
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/github.min.css -OutFile ./public/static/css/highlight-white.min.css
Invoke-WebRequest https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/monokai.min.css -OutFile ./public/static/css/highlight-black.min.css