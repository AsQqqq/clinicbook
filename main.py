import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, IconButton
from flet_core.control_event import ControlEvent


def main(page:ft.Page) -> None:
    """Main func"""
    page.title = "КлиникБук"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "light"
    page.window_width = 720
    page.window_height = 405
    page.window_resizable = False
    
    """SETUP"""
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label="I agree to stuff", value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign Up', width=200, disabled=True)
    button_register: ElevatedButton = ElevatedButton(text='Register', width=200)
    button_change_themes: IconButton = IconButton(icon="dark_mode", selected_icon="light_mode", style=ft.ButtonStyle(
        color={"":ft.colors.BLACK,"selected":ft.colors.WHITE}
    ), icon_size=25)

    """FUNC"""
    def validate(e: ControlEvent) -> None:
        """Check value"""
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
    
        page.update()
    
    def submit(e: ControlEvent) -> None:
        """Sign Up"""
        print(f'Username {text_username.value}')
        print(f'Password {text_password.value}')

        page.clean()
        page.add(
            Row(
            controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
            alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def register(e: ControlEvent) -> None:
        """Register"""
        pass

    def change_theme(e: ControlEvent) -> None:
        """Change theme"""
        if page.theme_mode == "light":
            page.theme_mode = "dark"
        else:
            page.theme_mode = "light"
        button_change_themes.selected = not button_change_themes.selected
        page.update()

        

    """CONNECT"""
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    button_register.on_click = register
    button_change_themes.on_click = change_theme


    page.add(
        Row(
        controls=[
            Column(
        [
            text_username,
            text_password,
            checkbox_signup,
            button_submit,
            button_register
        ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        Row(
        controls=[
            button_change_themes
        ],
        alignment=ft.MainAxisAlignment.END
        )
    )
        

if __name__ == '__main__':
    ft.app(target=main, assets_dir='icons')