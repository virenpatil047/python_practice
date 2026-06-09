import requests
from datetime import datetime as dt

TOKEN = "hfaoiu3909f3whi33fwfes"
USERNAME = "wren047"
PIXELA_URL = "https://pixe.la/"
GRAPH_ID = "graph1"
DATE = dt.now().strftime("%Y%m%d")


# # Create User
create_user = f"{PIXELA_URL}v1/users"
create_user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# try:
#     create_user_r = requests.post(url=create_user, json=create_user_params)
#     create_user_r.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print(f"Error : {e}")
#     raise

# print(create_user_r.status_code)
# print(create_user_r.text)


# # Create Graph
# create_graph = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN" : TOKEN
}
# graph_config = {
#     "id" : GRAPH_ID,
#     "name" : "Walking Tracker",
#     "unit" : "Kms",
#     "type" : "int",
#     "color" : "ajisai",
# }

# try:
#     create_graph_r = requests.post(create_graph, json=graph_config, headers=header)
#     create_graph_r.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print(f"Error : {e}")
#     raise

# print(create_graph_r.status_code)
# print(create_graph_r.text)


# # Post Pixel
# post_pixel = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# post_pixel_config = {
#     "date" : DATE,
#     "quantity" : "6"
# }

# try:
#     post_pixel_r = requests.post(post_pixel, json=post_pixel_config, headers=header)
#     post_pixel_r.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print(f"Error : {e}")
#     raise

# print(post_pixel_r.status_code)
# print(post_pixel_r.text)


# # Update Pixel
# pixel_update = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
# pixel_update_params = {
#     "quantity" : "8"
# }

# try:
#     pixel_update_r = requests.put(pixel_update, json=pixel_update_params, headers=header)
#     pixel_update_r.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print(f"Error : {e}")
#     raise
    
# print(pixel_update_r.status_code)
# print(pixel_update_r.text)


# Delete Pixel
pixel_delete = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

try:
    pixel_delete_r = requests.delete(pixel_delete, headers=header)
    pixel_delete_r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
    raise
    
print(pixel_delete_r.status_code)
print(pixel_delete_r.text)
