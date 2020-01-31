hljs.initHighlightingOnLoad();
marked.setOptions({
    smartLists: true,
    smartypants: false,
    highlight: function (code,lang,callback) {
        return hljs.highlightAuto(code).value;
    }
});
$('.markdown-wrapper').each(
function(index,e){
    var markdown_string=e.innerHTML;
    markdown_string = marked(markdown_string);
    e.innerHTML= markdown_string;
    renderMathInElement(e,
    {
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
        ]
    }
    );
}
);