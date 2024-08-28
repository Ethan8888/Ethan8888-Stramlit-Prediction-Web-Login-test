import yaml
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 

# Loading config file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Creating a login widget
try:
    authenticator.login()
except LoginError as e:
    st.error(e)

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

# Creating a password reset widget
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
            config['credentials']['usernames'][username_of_forgotten_password]['pp'] = new_random_password
    except ResetError as e:
        st.error(e)
    except CredentialsError as e:
        st.error(e)
    st.write('_If you use the password reset widget please revert the password to what it was before once you are done._')

# Saving config file
with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)
