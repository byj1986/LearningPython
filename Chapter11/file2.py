with open('sometext.txt', 'r') as st:
    while True:
        line = st.readline()
        print(line)
        if not line:
            break
    st.close()
