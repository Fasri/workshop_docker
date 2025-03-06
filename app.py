import streamlit as st

def hello():
    st.write("Hello World!")    

def main():
    st.write(hello())
st.title("Estou conseguindo rodar o Streamlit no Docker!")
if __name__ == "__main__":
    main()
