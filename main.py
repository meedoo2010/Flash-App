from flet import *
def main(page:Page):
    page.bgcolor=Colors.WHITE
    
    flashlight = Flashlight()
    page.overlay.append(flashlight)
    
    ph = PermissionHandler()
    page.overlay.append(ph)
    
    def open_app(e):
        ph.open_app_settings()
    
    
    app_bar = AppBar(bgcolor=Colors.BLACK,
                     title= Text('Flash Light [MK]',
                     color=Colors.WHITE),
                     toolbar_height=48,
                     actions=[
                         IconButton(Icons.SETTINGS,on_click=open_app)
                     ]
                     )
    row1 = Row([
        Text('\n\nFlash Light App',size=31,color='black')
    ],alignment=MainAxisAlignment.CENTER)
    
    row2 = Row([
        Image(src="logof.png",width=240)
    ],alignment=MainAxisAlignment.CENTER)
    
    row3 = Row([
        ElevatedButton("No",
                       width=120,
                       icon=Icons.PLAY_ARROW,
                       style=ButtonStyle(
                           padding=15,
                           shape=ContinuousRectangleBorder(radius=100)
                       ),
                       on_click=lambda _: flashlight.turn_on()
                       ),
        
        ElevatedButton("OFF",
                       width=120,
                       icon=Icons.PLAY_DISABLED_SHARP,
                       style=ButtonStyle(
                           padding=15,
                           shape=ContinuousRectangleBorder(radius=100)
                       ),
                       on_click=lambda _: flashlight.turn_off()
                       )
    ],alignment=MainAxisAlignment.CENTER)
    
    
    row4 = Row([
        Text('\n\n\n\n\n\n\n\n\n\n\n\nMade by Mohamed Khaled Saad',size=10,color='black')
    ],alignment=MainAxisAlignment.CENTER)
    
    
    
    
    page.add(app_bar, row1, row2, row3, row4)    
    page.update()
app(main,assets_dir='assets/')
