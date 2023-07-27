import streamlit as st
from random import randint
import pandas as pd#데이터프레임으로 표현하는 라이브러리

state = st.session_state.get('dice',[0,0,0,0,0,0])#영구적으로 저장되는 거

st.title('주사위 확률')
trial = st.button('주사위 굴리기')
if trial:
    num = randint(1,6)
    st.write(num)
    state[num-1] += 1
    st.session_state.dice = state#state 업데이트
    print(state)
    
prob = []
print(sum(state))
try:
    for i in state:
        prob.append(i/sum(state))
except:
    pass
print(prob)
index = [1,2,3,4,5,6]

table = pd.DataFrame({'횟수': state, 
                      '확률값':prob},
                     index = index)
print(table)
st.subheader('시행결과')
st.dataframe(table)
