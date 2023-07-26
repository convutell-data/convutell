import streamlit as st
from streamlit_modal import Modal

import streamlit.components.v1 as components





def main():
    st.title("Exemplo de Modal com Streamlit")

    modal = Modal("Demo Modal", key="my_modal")
    open_modal = st.button("Open")
    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("Text goes here")

            html_string = '''
            <h1>HTML string in RED</h1>

            <script language="javascript">
              document.querySelector("h1").style.color = "red";
            </script>
            '''
            components.html(html_string)

            st.write("Some fancy text")
            value = st.checkbox("Check me")
            st.write(f"Checkbox checked: {value}")


if __name__ == "__main__":
    main()
