with open('sometext.txt', 'r') as st:
    while True:
        line = st.readline()
        if not line:
            break
    st.close()
