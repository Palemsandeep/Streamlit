import streamlit as st
from PIL import Image


def main():
	st.set_page_config(layout="wide")
	global select2
	global select3
	select2 = None 
	select3 = None

	with open('style.css') as f:
		st.markdown (f"<style>{f.read()}</style>",unsafe_allow_html=True)

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
		st.image(img,width=1000)
	with col3:
		st.write("")

	st.markdown("<h1 style='text-align: center; color: Black;font-size: 29px;font-family:IBM Plex Sans;'>Learn to Build Industry Standard Data Science Applications</h1>", unsafe_allow_html=True)
	st.markdown("<p style='text-align: center; color: Blue;font-size: 29px;font-family:IBM Plex Sans;'>MLOPS Built On Google Cloud and Streamlit</p>", unsafe_allow_html=True)
	# st.markdown("<p style='text-align: center; color: Black;font-size: 22px;font-family:IBM Plex Sans;'>Problem Statement :</p>", unsafe_allow_html=True)
	st.markdown("<p style='text-align: center; color: black; font-size:22px;font-family:IBM Plex Sans;'><span style='font-weight: bold'>Problem Statement: </span>Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</p>", unsafe_allow_html=True)
	st.markdown("______________________________________________________________________________________________________________________________________________")
	
	c11,c12,c13,c14,c15 = st.columns((3,5,1,1,1))
	with c11:
		st.write("")
		st.write("")
		st.write("")
		st.markdown("##### **Problem Statement**")
	with c12:
		select1 = st.selectbox("",['Select the problem Statement','customer Churn : Who is going to churn?','Customer Churn : When will the churn occur?','Customer Churn : Why does the churn occurs?'],key = "key1")
	with c13:
		st.markdown("")
	with c14:
		st.markdown("")
	with c15:
		st.markdown("")

	st_list1 = ['customer Churn : Who is going to churn?','Customer Churn : When will the churn occur?','Customer Churn : Why does the churn occurs?']
	
	c21,c22,c23,c24,c25 = st.columns(((3,5,1,1,1)))
	with c21:
		if select1 in st_list1:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("##### **Problem type**")
	with c22:
		if select1 in st_list1:
			select2 = st.selectbox("",['Select the problem type','Classfication','Regression','Clustering','Continued Decision Making'])
	with c23:
		st.markdown("")
	with c24:
		st.markdown("")
	with c25:
		st.markdown("")


	st_list2 = ['Classfication','Regression','Clustering','Continued Decision Making']
	c31, c32, c33 ,c34,c35= st.columns(((3,5,1,1,1)))
	with c31:
		if select2 in st_list2:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("##### **Model Selection**")
	with c32:
		if select2 in st_list2:
			select3 = st.selectbox("",['Select the Model','Decision Tree','Random Forest','Logistic Regression','Linear Regression','k Means Clustering'])
	with c33:
		st.markdown("")
	with c34:
		st.markdown("")
	with c35:
		st.markdown("")

	st_list3 = ['Decision Tree','Random Forest','Logistic Regression','Linear Regression','k Means Clustering']
	c41,c42,c43,c44,c45 = st.columns(((3,5,1,1,1)))
	with c41:
		if select3 in st_list3:
			st.write("")
			st.write("")
			st.write("")
			st.markdown("##### **Upload File**")
	with c42:
		if select3 in st_list3:
			file_uploaded = st.file_uploader("Upload", type=["png","jpg","jpeg","jfif","zip",'tiff','gif','raw'],accept_multiple_files=True,)
	with c43:
		st.markdown("")
	with c44:
		st.markdown("")
	with c45:
		st.markdown("")

	st.sidebar.selectbox('Menu',["Home",'Model Validation','Download Model Outcome','Data Visualization','Deploy the Model'],key='key2')
	st.sidebar.selectbox("",['Library Used','Streamlit','Pandas','Ipython.display','sklearn.linear_model'],key='key3')
	st.sidebar.selectbox("",['Model Implemented','Decision Tree','Random Forest','Logistic Regression'],key='key4')
	st.sidebar.selectbox("",['GCP','VM Instance','Computer Engine','Cloud Storage'],key='key5')
	c51,c52,c53 = st.sidebar.columns((1,1,1))
	with c51:
		pass
	with c52:
		st.sidebar.button("clear/Reset",on_click=Reset_fun)
	with c53:
		pass



if __name__ == '__main__':
	main()
