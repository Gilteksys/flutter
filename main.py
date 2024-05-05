from flet import *

def main(page: Page):
    page.bgcolor = colors.BLACK54    
    page.vertical_alignment = MainAxisAlignment.CENTER
    
    images = [
        'img/imagem-1.jpeg',
        'img/imagem-2.jpeg',
        'img/imagem-3.jpeg',
        'img/imagem-4.jpeg',
        'img/imagem-5.jpeg',
        'img/imagem-6.jpeg',
        'img/imagem-7.jpeg',
        'img/imagem-8.jpeg',
    ]
    
    def change_posters():
        for poster in posters.controls: 
            poster.content.offset.x += poster.data * 0.2
            poster.content.scale.scale -= poster.data * 0.1
            poster.content.opacity -= poster.data * 0.3              
        posters.update()        
    
    def handle_dismiss(e):
        for num, poster in enumerate(posters.controls):
            if e.control == posters.controls[0]:
                posters.controls.clear()
                posters.controls.extend([
                    Dismissible(
                        content=Container(
                            image_src=img,
                            border_radius=border_radius.all(10),
                            image_fit=ImageFit.COVER,
                            aspect_ratio=9/16,
                            offset=Offset(x=0, y=0),
                            scale=Scale(scale=1),
                            opacity=1,
                            shadow=BoxShadow(blur_radius=50, color=colors.RED_ACCENT_200),
                            animate=Animation(duration=300, curve=AnimationCurve.DECELERATE),
                            animate_offset=True,
                            animate_scale=True,
                            animate_opacity=True                        
                        ),
                        data=pos,
                        on_dismiss=handle_dismiss
                    ) for pos, img in reversed(list(enumerate(images))) 
                ])
                break                
            
            poster.data -= 1
            poster.content.offset.x = 0
            poster.content.opacity =1
            poster.content.scale.scale = 1            
        change_posters()            
    
    posters = Stack(
        height=500,
        controls=[
            Dismissible(
                content=Container(
                    image_src=img,
                    border_radius=border_radius.all(10),
                    image_fit=ImageFit.COVER,
                    aspect_ratio=9/16,
                    offset=Offset(x=0, y=0),
                    scale=Scale(scale=1),
                    opacity=1,
                    shadow=BoxShadow(blur_radius=50, color=colors.RED_ACCENT_200),
                    animate=Animation(duration=300, curve=AnimationCurve.DECELERATE),
                    animate_offset=True,
                    animate_scale=True,
                    animate_opacity=True                        
                ),
                data=pos,
                on_dismiss=handle_dismiss
            ) for pos, img in reversed(list(enumerate(images))) 
        ]
    )        
    
    layout = Row(controls=[posters], alignment=MainAxisAlignment.CENTER)  
      
    page.add(layout)     
    change_posters()          
if __name__ == '__main__':
    app(main, assets_dir='assets')