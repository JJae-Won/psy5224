import streamlit as st
import cv2

st.write("""
         # 수열이네 필라테스
         할인중~
         상세문의는 010-5224-2920 전화문자 구독 좋아요 부탁드려용~
         """
         )

image = cv2.imread('./image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

st.image(image)