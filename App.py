import streamlit as st




st.set_page_config(page_title='Application',layout="wide")


st.header('Welcome to Data Entery Form!')


sidebar=st.sidebar

with sidebar:
    st.title("Home Menu")
    home=st.radio('radioButtun',options=['Home', 'Search'],label_visibility='hidden',horizontal=True)







if home=='Home':
    col1,col2,col3=st.columns(3)
    col4,col5=st.columns(2)


    with st.container():

        with col1:
            name=st.text_input('Enter your Name')
            



        with col2:
            f_name=st.text_input('Enter your Father Name')



        with col3:
            m_number=st.text_input('Enter your Mobile Number')


        with col4:
            age=st.text_input('Enter your Age')
        with col5:
            gender=st.selectbox('Enter your Gender',['','Male','Female'])


    submit=st.button("Submit",type='primary')
    if submit:

        if len(name) == 0 or len(age) == 0 or len(f_name) == 0 or len(m_number) == 0 or len(gender) == 0:

                message=st.write('Please fill all the fields')
        else:
                # Database Connection
            message=st.write('Done......')





if home=='Search':


    col1,col2=st.columns(2)
    with st.container():


        with col1:
            name=st.text_input('Enter  Name')


        with col2:
            m_number=st.text_input('Enter Mobile Number')
    col1,=st.columns(1)
    with col1:
        search=st.button("Search",type='primary')
    
   




    if search:
        if len(name) == 0 or len(m_number) == 0:

            st.write('Please fill all the fields')
        else:
                # Database Connection load data
            st.write(name,m_number)

    
            col1,col2,col3=st.columns(3)
         

            with col1:
                name=st.text_input('Name')
                



            with col2:
                f_name=st.text_input('Father Name')



            with col3:
                m_number=st.text_input('Mobile Number')

            
            
            col1,col2=st.columns(2)


            with col1:
                age=st.text_input('Age')
            with col2:
                gender=st.selectbox('Gender',['','Male','Female'])
            
            col1,col2=st.columns([1,1])
            with col1:
               dele_btn=st.button('Delete')
            with col2:
                edit_btn=st.button('Edit')
            
            
            
            if dele_btn:
                st.write('Delete...')
            
            elif edit_btn:
                st.write('Edit...')



            


            


            
            




    
       




        

        
