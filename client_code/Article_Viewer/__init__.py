from ._anvil_designer import Article_ViewerTemplate
from anvil import *
from anvil.js import get_dom_node

import random
import anvil.server

class Article_Viewer(Article_ViewerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.article_data=properties['item']
        
    def scroll_into_view(self,comp,pos='start'):
        get_dom_node(comp).scrollIntoView({"behavior":"smooth","block":pos})
    
    def jump(self,**event_args):
        self.scroll_into_view(event_args['sender'].tag,'center')

    def back_click(self, **event_args):
        set_url_hash('')

    def html_parser(self):
        import re
        '''
        If markdown is not able to offer you what you need, you can also insert an html code inside your markdown and let the parser convert it to HTML.
        This needs to be of the following pattern 
        -HTMLSTART-
        your html code here
        -HTMLEND-
        '''
        html_codes=[]
        def replace_html_slot(match):
            html_codes.append(match.group(1))
            return f"{{html_slot{len(html_codes)}}}"

        pattern = r'-HTMLSTART-([\s\S]*?)-HTMLEND-'
        self.article.content=re.sub(pattern, replace_html_slot, self.article.content)
        for index,html_code in enumerate(html_codes):
            self.article.add_component(HtmlTemplate(html=html_code),slot=f'html_slot{index+1}')

    def timer_1_tick(self, **event_args):
        self.timer_1.interval=0
        with anvil.server.no_loading_indicator:
            bg=self.article_data["bg"]
            if not bg.startswith('#'):
                get_dom_node(self.flow_panel_1).style.backgroundImage=f'url({bg})'
            else:
                self.flow_panel_1.background=bg
            self.title.text=self.article_data['title']
            self.subtitle.text=self.article_data['subtitle']
            self.date.text=f'Date: {self.article_data["date"].strftime("%d %B %Y")}'
            self.article.content=self.article_data['cont']
            self.html_parser()
            self.contents={i:i.innerText for i in get_dom_node(self.article).getElementsByTagName('h1')}
            for key,value in self.contents.items():
                l=Link(text=value,tag=key,font_size=18,icon='fa:dot',foreground='theme:primary',spacing_above='none',spacing_below='none',icon_align='left_edge')
                l.set_event_handler('click',self.jump)
                self.index.add_component(l)
