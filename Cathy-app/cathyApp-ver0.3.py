# ラジオボタン化と同種類のボタンの同時押しの非対応化
# credentials.jsonとtoken.jsonのファイルパスの入力欄の追加
# api-key入力欄（入力テキストの非表示）の追加
# Cathyサーバーの動作Logを表示させるエリアの追加
# ハリボテのメニューバーだったりヘッダーバーの追加
# 1-8 1-9 1-10 1-11 1-12

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.cathy.cathymain'


class Gtk4TestTest(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(
            self, application=app, title='Cathyapp-0.3',
            default_width=300, default_height=200)
        # Gtk.HeaderBarの定義
        headerbar = Gtk.HeaderBar()
        self.set_titlebar(headerbar)

        # Gtk.HeaderBarの左側に追加するWidgetの定義
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        button1 = Gtk.Button.new_from_icon_name(
            'pan-start-symbolic')
        button1.set_action_name('win.button1_clicked')
        box.append(button1)

        button2 = Gtk.Button.new_from_icon_name(
            'pan-end-symbolic')
        button2.set_action_name('win.button2_clicked')
        box.append(button2)

        headerbar.pack_start(box)

        # Gtk.HeaderBarの右側に追加するWidgetの定義
        button3 = Gtk.Button()
        button3.set_icon_name('open-menu-symbolic')
        button3.set_action_name('win.button3_clicked')

        headerbar.pack_end(button3)

        # グリッド全体の場所取り
        grid = Gtk.Grid(
            # 要求する幅及び高さの指定
            width_request=200, height_request=350,
            # Gtk.Grid周辺の余白を指定
            margin_top=20, margin_bottom=20,
            margin_start=20, margin_end=20,
            # 列方向の隙間と列方向のchildの幅を均等に割り振るかを指定
            column_spacing=70, column_homogeneous=True,
            # 行方向の隙間と行方向のchildの高さを均等に割り振るかを指定
            row_spacing=30, row_homogeneous=True,
            # 余白がある時に水平方向、垂直方向に拡張するかを指定
            hexpand=True, vexpand=True,
            )
        
        # ボタン要素の追加
        button1 = Gtk.CheckButton(label='Set Cathy to normal mode')
        button2 = Gtk.ToggleButton(label='Cathy server ON')
        button3 = Gtk.CheckButton(label='Set Cathy to debug mode', group=button1)
        button4 = Gtk.CheckButton(label='Output format CSV')
        button5 = Gtk.CheckButton(label='Output format Google Sheets', group=button4)
        keyBoxtext = Gtk.Label(
            label='Please Your API-Key Here',
            justify=Gtk.Justification.LEFT)
        keyBox = Gtk.Entry(
            placeholder_text='sk-********', visibility=False)
        cathylog = Gtk.Entry(editable=False, text='status of unimplemented Cathy.')
        credentialsBox = Gtk.Entry(placeholder_text='/home/User/Sheets/credentials.json')
        tokenBox = Gtk.Entry(placeholder_text='/home/User/Sheets/token.json')
        

        # ボタン要素の配置作業
        # 列{0,2,4,6}がイベントポイントで列{1,3,5,7}がイベントの説明
        grid.attach(button1, 0, 0, 1, 1)# Button1 : 列0、行0、幅1、高さ1
        grid.attach(button2, 2, 0, 1, 2)# Button2 : 列1、行0、幅2、高さ1
        grid.attach(button3, 0, 1, 1, 1)# Button3 : 列0、行1、幅2、高さ1
        grid.attach(button4, 0, 2, 1, 1)# Button4 : 列0、行2、幅2、高さ1
        grid.attach(button5, 0, 3, 1, 1)# Button5 : 列0、行3、幅2、高さ1
        grid.attach(keyBoxtext, 2, 2, 1, 1)
        grid.attach(keyBox, 2, 3, 1, 1)
        grid.attach(cathylog, 2, 4, 1, 5)
        grid.attach(credentialsBox, 0, 4, 1, 1)
        grid.attach(tokenBox, 0, 5, 1, 1)
        self.set_child(grid)

        # イベント処理（ボタンをクリックしたら）
        button1.connect('toggled', self.on_button1_clicked)
        button2.connect('toggled', self.on_button2_clicked)
        button3.connect('toggled', self.on_button3_clicked)
        button4.connect('toggled', self.on_button4_clicked)
        button5.connect('toggled', self.on_button5_clicked)


    def on_button1_clicked(self, button):
        print("button1が押されました")


    def on_button2_clicked(self, button):
        if button.get_active():
            print("button2はONです")
        else:
            print("button2はOFFです")

    def on_button3_clicked(self, button):
        print("button3が押されました")



    def on_button4_clicked(self, button):
        print("button4が押されました")



    def on_button5_clicked(self, button):
        print("button5が押されました")



class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()