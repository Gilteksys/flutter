import flet as ft

def main(page: ft.Page):    
    page.bgcolor = ft.colors.BROWN_300
    
    
    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else: 
                elem.opacity = 0.5
                
        main_image.update()
        options.update()
        
        product_images = ft.Container(
            content=ft.Column(
                alingnment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    main_image := ft.Image(
                        scr='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                    ),     
                    
                    options:= ft.Row(                                          
                        controls=[
                            ft.Container(
                                image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                                width=80,
                                height=80,
                                opacity=1,
                                on_click=change_main_image
                            ),
                            ft.Container(
                                image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                                width=80,
                                height=80,
                                opacity=0.5,
                                on_click=change_main_image
                            ),
                            ft.Container(
                                image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                                width=80,
                                height=80,
                                opacity=0.5,
                                on_click=change_main_image
                            )
                        ]
                        
                    )   
                ]

            )
        )
        
        product_details = ft.Container()


        
    layout = ft.Container(
        width=1000,
        height=400,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),

    )        
        
    page.add(layout)        
        
        
if __name__ == '__main__':
    ft.app(target=main)