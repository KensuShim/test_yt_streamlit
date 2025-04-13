import streamlit as st
# import numpy as np  
# import pandas as pd
# from PIL import Image
import time

st.title('stramlit 超入門')

st.write('DataFrame')

# df = pd.DataFrame({
#     '1':[1,2,3,4],
#     '2':[10,20,30,40]
# })

# st.write(df)
# # axis0=列　axis1＝行
# st.dataframe(df.style.highlight_max(axis=0) ,width=500, height = 100)
# # 静的なテーブル
# st.table(df)

# """
# # 章
# ## 節 
# ### 項

# ```phython
# import streamlit as st
# import numpy as np  
# import pandas as pd
# ```
# """

# ランダムで東京付近の緯度経度を疑似的に作成
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50.50] + [35.69,139.7],
#     columns=['lat', 'lon']
# )
# st.dataframe(df)
# # 折れ線グラフ
# # st.line_chart(df)
# # マッピング
# st.map(df)

st.write('進捗')
latest_iteration = st.empty()
bar = st.progress(0)

for i  in range(50):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress( (i + 1)*2)
    time.sleep(0.05)

'Done'


st.write('Int')

# if st.checkbox('show image'):
#     img = Image.open('sample.png')
#     st.image(img ,caption='APEX MAP', use_column_width=True)

# op = st.selectbox(
#     'あなたが好きなの',
#     list(range(1,11))
# )

'あなたが選んだのは',op,'です'

left_c, right_c = st.columns(2)
button = left_c.button('文字表示')
if button :
    right_c.write('文字')

expander1 = st.expander('問い合わせ1')
expander1.write('内容1')
expander2 = st.expander('問い合わせ1')
expander2.write('内容2')

txt_syumi = st.text_input('趣味2')
'あなたの趣味',txt_syumi,'です'

cond = st.slider('今の調子は',0,100,50)
'あなたの調子',cond,'です'
