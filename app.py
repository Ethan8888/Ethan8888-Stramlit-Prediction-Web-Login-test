import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(layout="wide") #设置屏幕展开方式，宽屏模式布局更好

credentials = {'usernames': {
                'xiaoyw': {'email': 'xiaoyw****@gmail.com',
                            'name': '肖永威',
                            'password': '*************'},   
                'admin': {'email': 'admin***@gmail.com',
                            'name': '管理员',
                            'password': '************  '} 
                            }
               }

authenticator = stauth.Authenticate(credentials,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(location='Login')

if authentication_status:
    with st.container():
        cols1,cols2 = st.columns(2)
        cols1.write('欢迎 *%s*' % (name))
        with cols2.container():
            authenticator.logout(location='Logout')
            
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
