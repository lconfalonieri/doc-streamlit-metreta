import streamlit as st
import requests
import numpy as np
import pandas as pd
import requests
import time
from PIL import Image, ImageDraw
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# # Use HTML and CSS to position text on the left
# st.write("<div style='text-align: left;'>", unsafe_allow_html=True)
# st.write("This text is positioned on the left side.")
# st.write("</div>", unsafe_allow_html=True)

st.title("Uploader Tool")

col1, col2, col3 = st.columns(3, gap="small")

def load_image(uploaded_file):
	img = Image.open(uploaded_file)
	return img 
 
def run():
	st.write("")
doctype = st.sidebar.text_input('What kind of document are you uploading?', placeholder= 'eg. Restaurant menu, Bank statement...')
keyvalues = st.sidebar.text_input('What do you want to extract from the document?', placeholder= 'eg. Dish and prices, operations and value...')
image_file = st.sidebar.file_uploader("Select an image:",type=['png','jpeg','jpg'])

if image_file is not None:
	if st.sidebar.button("Send to Server", type="primary"):
		try:
			server_url = "https://example.com/upload"  # Replace with your server URL
			# Create a dictionary containing the data
			files = {"file": (image_file.name, image_file.getvalue())}
			data_doctype = {"text": doctype}
			data_keyvalues = {"text": keyvalues}
			# Send a POST request to the server with the file
			response = requests.post(server_url, files=files)
			# Check the response from the server
			if response.status_code == 200:
				st.sidebar.success("File successfully sent to the server.")
				with col2:
					if image_file is not None:
						with st.spinner('Running elaboration...'):
							time.sleep(5)
						st.success('Done!')
			else:
				st.sidebar.error("Error sending file to the server. Please try again later.")
			# Send a POST request to the server with the text data
			response = requests.post(server_url, data=data_doctype)
			# Check the response from the server
			if response.status_code == 200:
				st.sidebar.success("File successfully sent to the server.")
			else:
				st.sidebar.error("Error sending the document type to the server. Please try again later.")
			# Send a POST request to the server with the text data
			response = requests.post(server_url, data=data_keyvalues)
			# Check the response from the server
			if response.status_code == 200:
				st.sidebar.success("File successfully sent to the server.")
			else:
				st.sidebar.error("Error sending what you want to extract to the server. Please try again later.")
		except Exception as e:
			st.sidebar.error(f"An error occurred: {str(e)}")


	# # Initialize a session state variable to track the button state
	# if 'button_clicked' not in st.session_state:
 	# 	st.session_state.button_clicked = False
	# # Add a button to send the text to the server
	# if not st.session_state.button_clicked:
	# 	button_clicked = st.sidebar.button("Send to Server", key=2, type="primary")
	
	# 	if st.sidebar.button("Send to Server", key=1, type="primary"):
	# 		try:
	# 			server_url = "https://example.com/upload"  # Replace with your server URL
	# 			# Create a dictionary containing the data
	# 			files = {"file": (image_file.name, image_file.getvalue())}
	# 			data_doctype = {"text": doctype}
	# 			data_keyvalues = {"text": keyvalues}
	# 			# Send a POST request to the server with the file
	# 			response = requests.post(server_url, files=files)
	# 			# Check the response from the server
	# 			if response.status_code == 200:
	# 				st.sidebar.success("File successfully sent to the server.")
	# 			else:
	# 				st.sidebar.error("Error sending file to the server. Please try again later.")
	# 			# Send a POST request to the server with the text data
	# 			response = requests.post(server_url, data=data_doctype)
	# 			# Check the response from the server
	# 			if response.status_code == 200:
	# 				st.sidebar.success("File successfully sent to the server.")
	# 			else:
	# 				st.sidebar.error("Error sending the document type to the server. Please try again later.")
	# 			# Send a POST request to the server with the text data
	# 			response = requests.post(server_url, data=data_keyvalues)
	# 			# Check the response from the server
	# 			if response.status_code == 200:
	# 				st.sidebar.success("File successfully sent to the server.")
	# 			else:
	# 				st.sidebar.error("Error sending what you want to extract to the server. Please try again later.")
	# 		except Exception as e:
	# 			st.sidebar.error(f"An error occurred: {str(e)}")
	# 	# If the button is clicked, set the session state variable to True
	# 	if button_clicked:
	# 		st.session_state.button_clicked = True


with col1:
	st.header("Image preview")

	# # Per creare un rettangolo vuoto
	# # Create a transparent image with a white background
	# width, height = 300, 400
	# background_color = (255, 255, 255, 0)
	# image = Image.new("RGBA", (width, height), background_color)
	# # Create a drawing context
	# draw = ImageDraw.Draw(image)
	# # Define the rectangle's position and size
	# x1, y1 = 50, 50
	# x2, y2 = 190, 260
	# # Define the rectangle's color (red in RGBA format)
	# rectangle_color = (0, 0, 0, 255)
	# # Draw the rectangle on the image
	# draw.rectangle([x1, y1, x2, y2], outline=rectangle_color, width=1)
	# # Display the image with the rectangle in Streamlit
	# st.image(image, use_column_width=False)

	if image_file is not None:
		st.image(image_file, caption='File preview', width=400)
		file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
		st.write(file_details)
		img = load_image(image_file)
		# st.experimental_rerun()

with col2:
	if image_file is not None:
		with st.spinner('Running elaboration...'):
			time.sleep(5)
		st.success('Done!')
    
with col3:
	st.header("Elaboration results:")
	# read elaboration
	csv_url = "https://example.com/path/to/your/csvfile.csv"  # Replace with your CSV file URL
	# Fetch the CSV file from the server
	response = requests.get(csv_url)
	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Read the CSV content into a DataFrame
		df = pd.read_csv(pd.compat.StringIO(response.text))
		# Display the DataFrame
		st.write("CSV file contents:")
		st.write(df)
	else:
		st.error("Failed to fetch the CSV file. Please check the URL.")

if __name__ == "__main__":
	run()