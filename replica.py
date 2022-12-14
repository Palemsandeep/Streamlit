import streamlit as st
from PIL import Image
from pynput.keyboard import Key,Controller

def main():
	st.set_page_config(layout="wide")
	# st.set_option('server.runOnSave', True)
	global select2
	global select3
	select2 = None 
	select3 = None
	def Reset_fun():
		pass
		st.session_state['key1']="Select the problem Statement"
		st.session_state['key2']="Home"
		st.session_state['key3']="Library Used"
		st.session_state['key4']="Model Implemented"
		st.session_state['key5']="GCP"



	col1, col2, col3 = st.columns([2,8,2])
	with col1:
		st.write("")
	with col2:
		img = Image.open("Deepsphere_image.png")
		st.image(img,width=800)
	with col3:
		st.write("")

	st.markdown("<h1 style='text-align: center; color: Black;font-size: 25px;'>Learn to Build Industry Standard Data Science Applications</h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: Blue;font-size: 25px;'>MLOPS Built On Google Cloud and Streamlit</h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 18px;'>Problem Statement : Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</h1>", unsafe_allow_html=True)
	st.markdown("______________________________________________________________________________________________________________________________________________")
	# st.write(":heavy_minus_sign:" * 34)

	c11,c12,c13 = st.columns((1,2.5,1))
	with c11:
		st.write("")
		st.write("")
		st.write("")
		st.markdown("**Problem Statement**")
	with c12:
		select1 = st.selectbox("",['Select the problem Statement','customer Churn : Who is going to churn?','Customer Churn : When will the churn occur?','Customer Churn : Why does the churn occurs?'],key = "key1")
	with c13:
		st.markdown("")

	st_list1 = ['customer Churn : Who is going to churn?','Customer Churn : When will the churn occur?','Customer Churn : Why does the churn occurs?']
	
	c21,c22,c23 = st.columns((1,2.5,1))

	with c21:
		if select1 in st_list1:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("**Problem type**")
	with c22:
		if select1 in st_list1:
			select2 = st.selectbox("",['Select the problem type','Classfication','Regression','Clustering','Continued Decision Making'])
	with c23:
			st.write("")


	st_list2 = ['Classfication','Regression','Clustering','Continued Decision Making']
	c31, c32, c33 = st.columns((1,2.5,1))
	with c31:
		if select2 in st_list2:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("**Model Selection**")
	with c32:
		if select2 in st_list2:
			select3 = st.selectbox("",['Select the Model','Decision Tree','Random Forest','Logistic Regression','Linear Regression','k Means Clustering'])
	with c33:
		st.write("")

	st_list3 = ['Decision Tree','Random Forest','Logistic Regression','Linear Regression','k Means Clustering']
	c41, c42, c43 = st.columns((1,2.5,1))
	with c41:
		if select3 in st_list3:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("**Upload File**")
	with c42:
		if select3 in st_list3:
			uploaded_file = st.file_uploader("Upload a csv file",type=['csv'])
	with c43:
		st.write("")

	st.sidebar.selectbox('Menu',["Home",'Model Validation','Download Model Outcome','Data Visualization','Deploy the Model'],key='key2')
	st.sidebar.selectbox("",['Library Used','Streamlit','Pandas','Ipython.display','sklearn.linear_model'],key='key3')
	st.sidebar.selectbox("",['Model Implemented','Decision Tree','Random Forest','Logistic Regression'],key='key4')
	st.sidebar.selectbox("",['GCP','VM Instance','Computer Engine','Cloud Storage'],key='key5')
	pressed = st.sidebar.button("clear/Reset",on_click=Reset_fun)
	

if __name__ == '__main__':
	main()