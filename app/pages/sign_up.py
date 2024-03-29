import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os

# 新規アカウント作成ページ
st.title("新規ユーザ登録")

with st.form("new_account_form", clear_on_submit=True):
    username = st.text_input("ユーザネーム")
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")

    submit_button = st.form_submit_button("ユーザ作成")

    if submit_button:
        # ここでユーザー情報の処理を行う
        hashed_password = stauth.Hasher([password]).generate()[0] # パスワードをハッシュ化
        
        #設定ファイルに新規ユーザーを追加
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
        
        # 新しいユーザー情報を追加
        config['credentials']['usernames'][username] = {
            'email': email,
            'name': username,
            'password': hashed_password
        }

        # 変更をファイルに保存
        with open("config.yaml", "w") as file:
            yaml.dump(config, file)
            
        st.success("Your account has been created!! Please login")
