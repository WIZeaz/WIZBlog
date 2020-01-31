function reply(e){
	var comment_block=e.parentNode.parentNode;
	var info=comment_block.firstElementChild.textContent;
	var content=comment_block.getElementsByClassName('markdown-wrapper')[0].textContent;
	$('#comment-content')[0].value='> '+info+'\n'+'> '+content+'\n'+$('#comment-content')[0].value;
}

