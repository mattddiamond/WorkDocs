import boto3
 
DIRECTORY_ID = "YOUR_DIRECTORY_ID"  # See Directory Service console
 
client = boto3.client("workdocs")
 
# Looking for the user, getting dict including Root FolderID 
response = client.describe_users(
    OrganizationId=DIRECTORY_ID,
    Query="YOUR_WORKDOCS_ADMIN_USER" #Workdoc Username
)

# Using Root Folder ID, get dict of folders at root
print("User Identified:",response["Users"][0]["Surname"])
user_root_folder_id = response["Users"][0]["RootFolderId"]
 
response = client.describe_folder_contents(
  FolderId=user_root_folder_id,
  Type="FOLDER",
  Include="FolderToDelete"
)

#loop through folders and delete
i=0
while i < len(response["Folders"]):
    print("Deleting Folder: ",response["Folders"][i]["Name"])
    delresponse = client.delete_folder(
        FolderId=response["Folders"][i]["Id"]
    )
    i += 1

    
    print("Response Returned:",delresponse["ResponseMetadata"]["HTTPStatusCode"])
print("Process Complete")
