class HTMLParser:
    @staticmethod
    def check_non_content_tags(text:str) -> bool:
        if(any([el in text.upper() for el in ["<!DOCTYPE HTML>","<HTML>", "<HEAD>","<BODY>","<STYLE>","<LINK","<SCRIPT"]])): return False
        else: return True

    @staticmethod
    def create_preview(html:str,template:str) -> str:
        template = template.lower()
        if("<body>" in template and html):
            preview_html = template.replace("<body>","<body> \n \t"+html)
            print(preview_html)
            return  preview_html
        else: return template