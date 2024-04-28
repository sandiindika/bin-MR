# LIBRARY / MODULE / PUSTAKA

import streamlit as st
from streamlit_option_menu import option_menu

import time, tempfile
from decimal import Decimal

from functions import *
from warnings import simplefilter

simplefilter(action= "ignore", category= FutureWarning)

# PAGE CONFIG

st.set_page_config(
    page_title= "App", layout= "wide", page_icon= "globe",
    initial_sidebar_state= "expanded"
)

## hide menu, header, and footer
st.markdown(
    """<style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .st-emotion-cache-z5fcl4 {padding-top: 1rem;}
    </style>""",
    unsafe_allow_html= True
)

## CSS on styles.css
with open("./css/style.css") as file:
    st.markdown(
        "<style>{}</style>".format(file.read()),
        unsafe_allow_html= True
    )

# MAIN PROGRAM
    
class MyApp():
    """Class dari MyApp

    Parameters
    ----------
    desc_ : bool
        Tampilkan keterangan error dalam Exceptions jika bernilai True dan
        sembunyikan jika False.

    Attributes
    ----------
    menu_ : list
        Daftar menu yang ada pada sistem.

    icons_ : list
        Daftar icon menu.
    """

    def __init__(self, desc_= False):
        self.desc_ = desc_
        self.menu_ = ["Embed Message", "Read Message"]
        self.icons_ = ["file-earmark-image", "file-earmark-text"]

    def _exceptionMessage(self, e):
        """Cetak keterangan error

        Parameters
        ----------
        e : exception object
            Obyek exception yang berisi deskripsi error terjadi.
        """
        ms_20()
        with ml_center():
            st.error("Terjadi masalah...")
            if self.desc_:
                st.exception(e)

    def _navigation(self):
        """Navigasi sistem
        
        Returns
        -------
        selected : str
            Selected item menu.
        """
        with st.sidebar:
            selected = option_menu(
                "", self.menu_, icons= self.icons_,
                styles= {
                    "container": {
                        "padding": "0 !important",
                        "background-color": "#E6E6EA"
                    },
                    "icon": {"color": "#020122", "font-size": "18px"},
                    "nav-link": {
                        "font-size": "16px", "text-align": "left",
                        "margin": "0px", "color": "#020122"
                    },
                    "nav-link-selected": {"background-color": "#F4F4F8"}
                }
            )

            ms_60()
            show_caption("Copyright © 2024 | ~", size= 5)
        return selected
    
    def _pageEmbedMsg(self):
        """Halaman untuk menyematkan pesan ke dalam gambar
        """
        try:
            ms_20()
            show_text("Embed Message", underline= True)

            alert = st.empty()
            cond = False

            left, right = ml_split()
            with left:
                message = st.text_area("Pesan", key= "Untuk pesan user")
                img = st.file_uploader(
                    "Upload gambar", type= ["png", "jpg"],
                    key= "Untuk gambar tempat pesan disembunyikan"
                )

                _, center, _ = st.columns([1,1,1])
                with center:
                    ms_20()
                    btn_process = st.button(
                        "Submit", use_container_width= True,
                        key= "Trigger embed message"
                    )

            with alert.container():
                with ml_center():
                    if btn_process:
                        if message == "" or message == " ":
                            st.warning("Setidaknya harus ada pesan yang akan disematkan!", icon= "⚠️")
                        elif img is None:
                            st.warning("Pilih gambar terlebih dahulu!", icon= "⚠️")
                        else:
                            cond = True

            with right:
                ms_20()
                env_process = st.empty()
                with env_process.container():
                    if img is not None:
                        st.image(
                            img, caption= img.name, use_column_width= True
                        )

                if cond:
                    env_process.empty()

                    with env_process.container():
                        with st.spinner("Sedang proses..."):
                            start_time = time.time()

                            p, q, r, s, e, t, n, u, d = generate_keys()
                            keys = f"p, q, r, s, e, t, n, u, d = [{Decimal(p)}, {Decimal(q)}, {Decimal(r)}, {Decimal(s)}, {Decimal(e)}, {Decimal(t)}, {Decimal(n)}, {Decimal(u)}, {Decimal(d)}]"
                            to_docx(keys, "keys.docx")

                            text = convert_data_size(message)
                            text_ascii = to_ascii(text)

                            chipertext = []
                            for char in range(len(text_ascii)):
                                sym = text_ascii[char] * e % n
                                chipertext.append(sym)

                            chipertext = str(chipertext)
                            to_docx(chipertext, "chipertext.docx")

                            temp_file = tempfile.NamedTemporaryFile(delete= False)
                            temp_file.write(img.read())
                            temp_file.close()
                            filepath = temp_file.name
                            res_img = embed_msg(filepath, message)

                            finish_time = time.time()
                            times = duration_count(start_time, finish_time)
                        st.image(res_img, caption= "result.png", use_column_width= True)
                        st.info(times)

        except Exception as desc:
            self._exceptionMessage(desc)

    def _pageReadMsg(self):
        """Halaman untuk membaca pesan di dalam gambar
        """
        try:
            ms_20()
            show_text("Read Message", underline= True)

            alert = st.empty()
            cond = False

            left, right = ml_split()
            with left:
                img = st.file_uploader(
                    "Upload gambar", type= ["png", "jpg"],
                    key= "Untuk gambar yang memiliki pesan"
                )

                keys = st.file_uploader(
                    "Upload keys", type= ["docx"],
                    key= "Untuk keys yang disimpan"
                )

                _, center, _ = st.columns([1,1,1])
                with center:
                    ms_20()
                    btn_read = st.button(
                        "Read", use_container_width= True,
                        key= "Trigger read message"
                    )

            with alert.container():
                with ml_center():
                    if btn_read:
                        if img is None:
                            st.warning("Gambar tidak ditemukan!", icon= "⚠️")
                        elif keys is None:
                            st.warning("Dokumen \"Keys\" tidak tersedia!", icon= "⚠️")
                        else:
                            cond = True

            with right:
                ms_20()
                env_process = st.empty()
                with env_process.container():
                    if img is not None:
                        st.image(
                            img, caption= img.name, use_column_width= True
                        )

                if cond:
                    env_process.empty()

                    with env_process.container():
                        with st.spinner("Sedang proses..."):
                            start_time = time.time()
                            chipertext_doc = get_docx("./data/keys/chipertext.docx")

                            temp_img = tempfile.NamedTemporaryFile(delete= False)
                            temp_img.write(img.read())
                            temp_img.close()
                            imgpath = temp_img.name
                            text = read_msg(imgpath)

                            temp_doc = tempfile.NamedTemporaryFile(delete= False)
                            temp_doc.write(keys.read())
                            temp_doc.close()
                            docpath = temp_doc.name
                            p, q, r, s, e, t, n, u, d = read_key(docpath)

                            chipertext_val = [int(x.group()) for x in re.finditer(r'\d+', chipertext_doc)]

                            plaintext_ascii = []
                            for i in range(len(chipertext_val)):
                                x = chipertext_val[i] * d % n
                                plaintext_ascii.append(x)
                            message = "".join([chr(i) for i in plaintext_ascii])
                            
                            finish_time = time.time()
                            times = duration_count(start_time, finish_time)
                        st.image(
                            img, caption= img.name, use_column_width= True
                        )
                        
                        ms_20()
                        st.text_area(
                            "Pesan", value= message, disabled= True,
                            key= "Tampilkan pesan"
                        )
                        st.info(times)

        except Exception as desc:
            self._exceptionMessage(desc)

    def main(self):
        """Main Program
        """

        with st.container():
            selected = self._navigation()

            if selected == self.menu_[0]:
                self._pageEmbedMsg()
            elif selected == self.menu_[1]:
                self._pageReadMsg()

if __name__ == "__main__":
    app = MyApp(desc_= True)
    app.main()